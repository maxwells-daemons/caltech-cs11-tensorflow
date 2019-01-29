# caltech-cs11-tensorflow
Repository for the CS11 Tensorflow track. Course outline [here](https://docs.google.com/document/d/1TSouogmnP0fgxwrlOyasWnNaG0aKX3i9tmuzZKjct1Y/edit?usp=sharing).

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
  2. Some reading on the week's material, presented as a `notes_*.ipynb` Jupyter notebook that can be read online or run locally. It will have lots of exposition, plus graphs and code snippets here and there.
  3. A `lab_*.ipynb` file to be filled out as the week's assignment

While doing the assignments, expect to spend some amount of time reading the TensorFlow documentation, especially pages on functions I mention you might need for a problem.
This will be true every time you use TensorFlow.
To quickly search for what you need, I recommend using https://devdocs.io/, which re-hosts the TensorFlow documentation in an easy-to-search way.
The regular documentation is available here: https://www.tensorflow.org/api_docs/python/.

## Environment setup
For this class, we'll using Python 3.
The easiest way to complete the setup is in a virtual environment, which I walk you through below.
Note that TensorFlow currently _only supports Python 3.4, 3.5, and 3.6_, so I will assume you have one of those versions installed, with pip set up correctly.
I'm also assuming you're setting this up on a standard Linux system.
If not, proceed carefully.

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
pip install numpy scipy matplotlib ipython jupyter pandas scikit-learn tensorflow
~~~
Then, try running `python -c "import tensorflow"` in your shell.
If the line executes successfully (printing nothing), your setup is probably fine.
If you get an error message like `ModuleNotFoundError: No module named 'tensorflow'` then something went wrong.


#### Downloading the code
You'll be doing assignments by modifying `.ipynb` notebook files and submitting them via git, so you need your own copy of the code.
Fork the repository (most easily, by clicking the "fork" button in the upper-right corner of the GitHub page), then make a local copy by cloning your fork.

## Running the code
#### Locally
With the virtual environment active, run
~~~
jupyter notebook
~~~
to host the notebook server.
If you haven't used Jupyter notebooks before, [here's a pretty good guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

## Colaboratory
Apart from running a Jupyter notebook locally, Google also provides free "hosted notebooks" with [Colaboratory](https://colab.research.google.com/).
They're a particularly good choice if your computer is not too powerful (they offer free compute time on GPUs as long as you're not using them for too long at once) or if you're having a hard time setting up the dependencies (they come pre-loaded with all of the libraries we'll use).
The tradeoff is that loading and saving data and files will follow a different procedure than if you're running it locally, running TensorBoard is more complicated (look up the TensorBoardColab library), and the notebook is online so you may experience more latency.
I'm writing this class with the intent that everyone runs the notebooks locally, so if you want to use Colaboratory you may have to figure a lot of it out on your own.
For any assignment that takes serious processing power, I'll write with Colaboratory and its free acceleration in mind.

Brownie points to anyone who gets their code running on a TPU.

## Submitting assignments
TODO

## Resources:
 - Documentation:
   - [Tensorflow official API](https://www.tensorflow.org/api_docs/python/): The official documentation; hard to search effectively but the individual pages are good
   - [Tensorflow official API (devdocs version)](https://devdocs.io/tensorflow~python/): An easier-to-search rehost of the official documentation, which I usually prefer to use
   - [Tensorflow official guide](https://www.tensorflow.org/guide/): A short, high-quality tutorial series by the TF developers
 - Derivatives on a computational graph:
   - [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/): Intuitively building up backpropagation on a graph from simple calculus
   - [Hacker's Guide to Neural Networks](https://karpathy.github.io/neuralnets/): The first part of this (awesome!) article explains backpropagation with examples in code and logic circuits
 - Differentiable programming concepts:
   - [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35): An ambitious piece by the director of AI at Tesla in which differential programming is the way most (all?) future software will be written
   - [2016 Microsoft Research Slides](http://www.cs.nuim.ie/~gunes/files/Baydin-MSR-Slides-20160201.pdf): Slide deck from a research presentation contrasting automatic differentiation (AD) to differentiable programming and covering some topics in both fields
 - Cool stuff:
   - [Neural Networks, Types, and Functional Programming](https://colah.github.io/posts/2015-09-NN-Types-FP/)
   - [Neural Networks, Manifolds, and Topology](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)
   - [Christopher Olah's entire blog](https://colah.github.io/)
