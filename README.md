# CS11: TensorFlow
Repository for the Caltech CS11 TensorFlow track. Course outline [here](https://docs.google.com/document/d/1TSouogmnP0fgxwrlOyasWnNaG0aKX3i9tmuzZKjct1Y/edit?usp=sharing).

This course is intended as a fast-paced introduction to machine learning with TensorFlow and Keras, focused particularly on neural networks.
It gives a whirlwind tour of several types of models, and brief coverage of several machine learning topics, but its primary goal is first and foremost to _get you comfortable with writing, training, and deploying sophisticated models in TensorFlow._
Along the way, we'll look at concepts from differentiable programming, an exciting new programming paradigm.
By the end of this class, you should be able to write deep models to solve many kinds of problems.

What this course is **not**:
 - An intro class in machine learning. You should probably take [one of those](https://work.caltech.edu/telecourse.html) first.
 - A statistics or linear algebra class. To write models and understand what they're doing, you need both of these, but this class doesn't have time to cover them. You should take a class in each of those first.
 - A class in neural network theory. They're the main model we'll focus on, but the focus is _how to build them_, not why they work.
 - Going to cover all of the most recent models. We just don't have time.

The class is three units, pass-fail.
That means that readings and labs should take total three hours per week, for ten weeks.
There are seven labs, plus some setup time.
I've tried my very best to hit the 3-unit mark, so if a week is too short or too long, please let me know!
That being said, some weeks may be longer than you're used to for a 3-unit because the ten weeks are divided into seven sections, and because we're trying to cover a _lot_ of material in a limited time.

If you're planning to take the course, please read this *entire* document.
It has some important info!

## "Requirements"
It goes without saying that you should be comfortable writing lots of Python code.

I'll also assume some working familiarity with machine learning (equivalent to [CS156, "Learning From Data"](https://work.caltech.edu/telecourse.html)), linear algebra, multivariable calculus, and the Python scientific computing stack (mostly `jupyter`, `numpy` and `pyplot`).
As a result I'll spend less time than some courses might explaining certain concepts (e.g. matrix operations, gradient descent, linear regression) in order to cover more interesting and useful concepts in a short time.
I'll mention it whenever I'm glossing over a concept, and provide links to explanations I like, but be prepared to do plenty of outside reading if you're not fresh on these concepts.
There are some incredible tutorials and explanations online, much better than I could give, so it makes more sense for you to read those blog posts than to read my own worse explanations.

That being said, "requirements" can be fake if you don't mind putting in the extra hours to learn.
The only things you really _need_ are solid Python skills and a working understanding of `numpy` arrays.
(But then, this course will be more than 3 units...)

## Course structure
All of the labs will have the same basic structure:
  1. A README with a high-level overview of the week's content
  2. Some reading on the week's material, presented as a `notes_*.ipynb` Jupyter notebook that can be read online or run locally. It will have lots of exposition, plus images and code snippets here and there.
  3. A `lab_*.ipynb` file to be filled out as the week's assignment

While doing the assignments, expect to spend some amount of time reading the TensorFlow documentation, especially pages on functions I mention you might need for a problem.
This will be true every time you use TensorFlow.
To quickly search for what you need, I recommend using https://devdocs.io/, which re-hosts the TensorFlow documentation in an easy-to-search way.
The regular documentation is available here: https://www.tensorflow.org/api_docs/python/.

## Environment setup
You should do this setup before the first lab.

For this class, we'll using Python 3.
The easiest way to complete the setup is in a virtual environment, which I walk you through below.
Note that TensorFlow currently _only supports Python 3.4, 3.5, and 3.6_, so I will assume you have one of those versions installed, with pip set up correctly.
I'm also assuming you're setting this up on a standard Linux system.
If not, proceed carefully.

I don't really have the bandwidth to help with setup issues, so if you're having trouble, you can try:
 - Using a clean virtualenv
 - Using a clean Linux VM
 - Asking a friend
 - Using Colaboratory (see below)

#### Virtual environments
Virtual environments simulate a "clean" Python install on your system so you don't need to worry about library conflicts and dependency issues.
Therefore I recommend dedicating a virtual environment to this class.
First, install virtualenv and virtualenvwrapper:
~~~
pip install virtualenv
pip install virtualenvwrapper
~~~
[You might want to do additional setup here](http://roundhere.net/journal/virtualenv-ubuntu-12-10/).
Then, create and check the virtual environment:
~~~
mkvirtualenv -p /usr/bin/python3.6 cs11-tensorflow  # Point to the Python binary you'll be using
workon cs11-tensorflow
python --version  # Should print "Python 3.x.y" where x is 4, 5, or 6
~~~
To activate the environment, use `workon cs11-tensorflow`.
To deactivate it when you're done, use `deactivate`.

#### Required libraries
Once you're in the virtual environment, run
~~~
pip install numpy scipy matplotlib ipython jupyter pandas scikit-learn tensorflow==1.13.1 keras
~~~
Then, try running `python -c "import tensorflow"` in your shell.
If the line executes successfully (printing nothing), your setup is probably fine.
If you get an error message like `ModuleNotFoundError: No module named 'tensorflow'` then something went wrong.


#### Downloading the code
You'll be doing assignments by modifying `.ipynb` notebook files and submitting them via git, so you need your own copy of the code.
[Duplicate the repository](https://help.github.com/en/articles/duplicating-a-repository) (don't fork it, since forks can't be private), host it on GitHub, and add me (and the TAs, whose email addresses I'll send to you).

## Running the code
#### Locally
With the virtual environment active, run
~~~
jupyter-notebook
~~~
to host the notebook server.
If you haven't used Jupyter notebooks before, [here's a pretty good guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

#### Colaboratory
Apart from running a Jupyter notebook locally, Google also provides free "hosted notebooks" with [Colaboratory](https://colab.research.google.com/).
They're a particularly good choice if your computer is not too powerful (they offer free compute time on GPUs as long as you're not using them for too long at once) or if you're having a hard time setting up the dependencies (they come pre-loaded with all of the libraries we'll use).

The tradeoff is that loading and saving data and files will follow a different procedure than if you're running it locally, running TensorBoard is more complicated (look up the TensorBoardColab library), and the notebook is online so you may experience more latency.

I'm writing this class with the intent that everyone runs the notebooks locally, so if you want to use Colaboratory you may have to figure a lot of it out on your own.
For the most part, any modern computer should be able to handle the processsing required in a reasonable amount of time.
For any assignment that takes serious processing power, I'll write with Colaboratory and its free acceleration in mind.

Brownie points to anyone who gets their code running on a TPU.

## Submitting assignments
To submit assignments, make a private GitHub repository forking this one.
Give read access to me and the TAs for the term you're taking it, then for each assignment, email me the commit hash for your submission.
I'll send out the relevant information (GitHub usernames, email addresses, etc) once people have registered for the class.

## Due dates
The labs are due at the following times (11 PM Friday) each term:
 - Lab 1: End of the second week.
 - Lab 2: End of the third week.
 - Lab 3: End of the fourth week.
 - Lab 4: End of the sixth week (take week 5 off for midterms for your other classes).
 - Lab 5: End of the seventh week.
 - Lab 6: End of the eighth week.
 - Lab 7: End of the ninth week.
 
At the start of term, I'll send out exact due dates.

## Collaboration policy, honor code
Feel free to collaborate on concepts, algorithms, etc, but please don't share code in any way.
This includes looking up code snippets that do what you're trying to do.

However: this is a programming language class, and sometimes the difficulty is in finding the right Operations to use.
So, feel free to get help from me and others for searching the documentation, understanding syntax and common language forms, knowing which Operations to use, etc.
You can also look up TensorFlow code snippets that do similar, but not the same, thing.
It's the difference between getting help on a mini-project to "write linear regression" by searching Stack Exchange for "how to write linear regression in TensorFlow" (bad) vs "how to do matrix multiplication in TensorFlow" (good).
Ask me if you have questions.

Ultimately, this is a pass-fail course and you're here to learn useful things, so only do what helps you do that.

## Resources:
 - Documentation and TensorFlow resources:
   - [TensorFlow official API](https://www.tensorflow.org/api_docs/python/): The official documentation; hard to search effectively but the individual pages are good
   - [TensorFlow official API (devdocs version)](https://devdocs.io/tensorflow~python/): An easier-to-search rehost of the official documentation, which I usually prefer to use
   - [TensorFlow official guide](https://www.tensorflow.org/guide/): A short, high-quality tutorial series by the TF developers
   - ["Tensorflow: The Confusing Parts"](https://jacobbuckman.com/post/tensorflow-the-confusing-parts-1/) is a short and very readable guide to the key abstractions behind TensorFlow
   - ["A Practical Guide for Debugging TensorFlow Codes"](https://wookayin.github.io/tensorflow-talk-debugging/#1) is exactly what it sounds like
 - Derivatives on a computational graph:
   - [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/): Intuitively building up backpropagation on a graph from simple calculus
   - [Hacker's Guide to Neural Networks](https://karpathy.github.io/neuralnets/): The first part of this (awesome!) article explains backpropagation with examples in code and logic circuits
 - Machine learning:
   - [The "Deep Learning Book"](https://www.deeplearningbook.org/) is in my mind the comprehensive reference on deep learning, from ML first principles to modern approaches. It's a must-read for anyone wanting to seriously get into deep learning. And it's free!
   - [Practical Deep Learning for Coders (fast.ai)](https://www.fast.ai/) is an incredibly popular online course in deep learning.
 - Cool stuff:
   - [Neural Networks, Types, and Functional Programming](https://colah.github.io/posts/2015-09-NN-Types-FP/)
   - [Neural Networks, Manifolds, and Topology](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)
   - [Christopher Olah's entire blog](https://colah.github.io/)


## What about TensorFlow 2.0?
As you may have heard, [TensorFlow 2.0 is coming soon](https://www.tensorflow.org/alpha).
This will involve some significant changes to the code, and even the content, of this course.
However, many of the changes are not finalized and the release date is still uncertain.
I'll update the course for TensorFlow 2.0 as soon as I can once it's reached a stable release, but for now we're standardizing on TensorFlow 1.
