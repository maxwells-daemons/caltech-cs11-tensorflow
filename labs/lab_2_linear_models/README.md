# Lab 2: Linear Models
This week completes our initial description of model-building in TensorFlow, covering three core topics: loading data and feeding it to the model, saving and restoring models, and using TensorBoard to visualize and debug your code.
Along the way, we cover minibatch gradient descent and backpropagation, the two most important algorithms in modern machine learning, and linear and logistic regression.
These simple, common, and powerful models are useful for many kinds of machine learning problems, and insights gained from coding them will extend to the neural networks we spend the rest of the course on.
From this point on, increasing complexity will come more from new types of models and new operations than from TensorFlow language features.

Concepts this week:
 - Regression and classification problems
 - Loss functions (squared error and cross-entropy)
 - Linear models (linear regression and logistic regression)
 - Stochastic gradient descent algorithm, batching and batch size
 - Backpropagation algorithm

TensorFlow features this week:
 - Iterating over data with Datasets and Iterators
 - Saving and restoring variables
 - Using TensorBoard to visualize computational graphs and learning plots
 
 Optional material:
  - ["Calculus on Computational Graphs: Backpropagation" (Chris Olah)](https://colah.github.io/posts/2015-08-Backprop/) quickly and intuitively derives backpropagation.
  - ["Hacker's guide to Neural Networks" (Andrej Karpathy)](https://karpathy.github.io/neuralnets/) derives the chain rule and backpropagation from scratch, from the perspective of math as combining "circuits" (operations) and from a "hacking" or "coding" perspective
  - [The ML Cheatsheet guide to logistic regression](https://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html)
  - The TensorFlow official guide on [saving and restoring models](https://www.tensorflow.org/guide/saved_model), [graph visualization](https://www.tensorflow.org/guide/graph_viz), and [scalar visualization](https://www.tensorflow.org/guide/summaries_and_tensorboard)
