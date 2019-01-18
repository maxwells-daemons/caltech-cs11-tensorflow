# Lab 1: TensorFlow Basics
This lab will introduce the basics of writing programs with TensorFlow, as well as some course structure.

## Course structure
All of the labs will have the same basic structure:
  1. A README like this one with a high-level overview of the week's content
  2. Some reading on the week's material
  3. A `lab_*.ipynb` file to be filled out as the week's assignment 

Make sure you read the **entire** README before starting the assignment, since it might have important information or setup steps.

## Reading
TODO

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
With the virtual environment active, run
~~~
jupyter notebook
~~~
to host the notebook server.
If you haven't used Jupyter notebooks before, [here's a pretty good guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

## Submitting assignments
TODO
