# Lab 4: Convolutional Neural Networks
This week is focused on one of the most important varieties of neural network layers, which form the core of some of the most successful networks: convolutional layers.
Convolutional neural networks are now ubiquitous when working with image data, getting far and away the best results on just about everything with image or video input.
They're also starting to see more use in modeling sequences, such as audio, like the modern WaveNet architecture for speech.
Convolutions also see use in reinforcement learning to allow agents to understand the world or game board -- see AlphaGo, for instance.

Concepts this week:
 - Convolutions:
    - 1D
    - 2D
 - Convolutional neural networks
 - Benefits of convolutions
 - Interpretations of convolution:
    - Learning filters
    - Locally-connected dense layers with weight sharing
 - Stride
 - Pooling
 - Common architecture choices

TensorFlow features this week:
 - TensorFlow convolution functions
 - Summary images with TensorBoard

Optional resources:
 - [The Deep Learning Book, Chapter 9: Convolutional Networks](http://www.deeplearningbook.org/contents/convnets.html) is the definitive resource here, if you have the time to read it
 - ["A guide to convolution arithmetic for deep learning"](https://arxiv.org/abs/1603.07285)
 - [This (long-ish) tutorial on CNNs in TensorFlow by Hvass Labs](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/02_Convolutional_Neural_Network.ipynb) is quite good
 - [This interactive visualization of image kernels](http://setosa.io/ev/image-kernels/) is fun to play around with and can give you some intuition for how 2-D convolution works
 - ["Conv Nets: A Modular Perspective"](https://colah.github.io/posts/2014-07-Conv-Nets-Modular/) is a good blog post on the "convolution as reused functions" perspective
 - ["Visualizing Convolutional Neural Networks"](https://www.oreilly.com/ideas/visualizing-convolutional-neural-networks) is another tutorial on CNNs in TensorFlow, this time with a little more detail on the visualization side
