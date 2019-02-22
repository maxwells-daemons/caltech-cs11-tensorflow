# Lab 3: Fully-Connected Neural Networks
This week we introduce neural networks, which are the core of "deep learning" and the model we'll focus on for the rest of the class.
Fully-connected, feedforward networks are their simplest variation, but fully-connected sections are common in modern networks, and they'll give us important intuition for how things like hidden representations, activation functions, and high-dimensional optimization work.

This week will be more theory-heavy, without all that much new TensorFlow content.
In part this is because we've already covered the basics of model-building in TensorFlow.
It's also important to understand the theory behind neural networks in order to be able to build them well in practice.

Concepts this week:
 - Fully-connected neural networks
 - Nonlinear modeling
 - Intemediate representations through hidden layers
 - Effects of depth
 - Activation functions:
    - Logistic sigmoid
    - ReLU
 - Hidden layer initialization
 - Interpretations of neural networks:
    - Hierarchical pattern-matching
    - Representation learning
    - Function composition
 - Momentum in SGD

TensorFlow features this week:
 - TensorBoard visualizations:
    - Learning dynamics
    - Hidden layer activations
 - Various initializers
 - Keras API (sequential models)
 - Using tfdbg to debug TensorFlow code

Optional material:
 - Google's ["neural network playground"] is an in-browser interactive "toy" feedforward network you can train under different conditions to visualize how layer activations change over the input space
 - [The Deep Learning Book, Chapter 6: Deep Feedforward Networks](http://www.deeplearningbook.org/contents/mlp.html) is a long but excellent introduction 
 - ["Neural Networks, Manifolds, and Topology" (Chris Olah)](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/) is a good explanation of the "manifold interpretation" of neural networks
 - ["Neural Networks, Types, and Functional Programming" (Chris Olah)](https://colah.github.io/posts/2015-09-NN-Types-FP/) is the source of this fascinating view on differentiable programming as "learned functional programs"
 - [The Keras sequential model guide](https://keras.io/getting-started/sequential-model-guide/)
 - The [TensorFlow official guide on histograms](https://www.tensorflow.org/guide/tensorboard_histograms)
