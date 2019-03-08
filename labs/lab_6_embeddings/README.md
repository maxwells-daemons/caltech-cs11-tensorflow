# Lab 6: Embeddings
This week is focused on how to effectively use and interpret discrete variables through a powerful technique known as embeddings.
Embeddings can teach your models valuable things about your input, learn to encode similarity and distance, and make models much more statistically efficient.
What's more, they can often be learned unsupervised.
When dealing with discrete variables, and especially text, embeddings are a must.

Concepts:
 - Benefits of distributed representation
 - Sparse vs dense tensors
 - Discrete input and one-hot encodings
 - Converting sparse discrete input to dense, distributed representation through embeddings

TensorFlow features:
 - TensorFlow and Keras embedding functions
 - Approximate softmax training
 - Visualizing embeddings with TensorBoard

 Optional resources:
  - ["Deep Learning, NLP, and Representations" on Chris Olah's blog](https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/) ties embeddings to transferrable representations in a really compelling way, and shows off some of the cool things you can do with embeddings
  - [The TensorFlow official guide on embeddings](https://www.tensorflow.org/guide/embedding) covers what embeddings are and how to visualize them in TensorFlow
  - ["Vector Representations of Words"](https://www.tensorflow.org/tutorials/representation/word2vec), another TensorFlow official guide, discusses embeddings and the Word2Vec model in depth, including examples with code
  - [The Deep Learning Book chapter on representation learning](https://www.deeplearningbook.org/contents/representation.html) is a great resource for understanding distributed representations, how to learn them, and why they help, but it's again dense and long
  - [The TensorFlow official guide on candidate sampling](https://www.tensorflow.org/extras/candidate_sampling.pdf) discusses approximate (sampling-based) loss functions in depth
