import time
import numpy as np
import tensorflow as tf
#importing input_data fuction
from tensorflow.examples.tutorials.mnist import input_data

#Loading the data
MNIST = input_data.read_data_sets("/data/mnist", one_hot=True)

# Defining the model parameters
learning_rate = 0.005
batch_size = 128
n_epochs = 100

#creating placeholders for features(here each image(28*28pixel) is loaded into
# 1d tensor of size 784)
#dependent variable is 10 classes(1 to 10) hence one hot vector of size 10
X = tf.placeholder(tf.float32, [batch_size, 784])
Y = tf.placeholder(tf.float32, [batch_size, 10])

#defining weight and bias tensors, they are defined as variables
#because their value get updated as we train the model with data.
#size of w depends on size of features(X) and lables(Y) since Y is matrix multiplicationof X and W
w = tf.Variable(tf.random_normal(shape=[784, 10], stddev=0.01), name="weights")
b = tf.Variable(tf.zeros([1, 10]), name="bias")

#logistic linear eqauation with x as tensor of features, w as tensor of parameters, b as tensor of bias, and Y logits 
#tensor of outputs(prediction)
logits = tf.matmul(X, w) + b

#computes probabilities of failures
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y)
#computes mean of failures over the batch
loss = tf.reduce_mean(entropy) 

# optimizes the loss by GradientDescent alogorithm 
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

#object(init) for variable initialization
init = tf.global_variables_initializer()


with tf.Session() as sess:
    # initializing the variables
    sess.run(init)
    #number of batches in training data
    nOFbatches = int(MNIST.train.num_examples/batch_size)
    for i in range(n_epochs): # train the model n_epochs times
        for _ in range(nOFbatches):
            #taking the training data
            X_batch, Y_batch = MNIST.train.next_batch(batch_size)
            #feeding training data to optimizer and minimizing the loss
            sess.run([optimizer, loss], feed_dict={X: X_batch, Y:Y_batch})
    #number of batches in test data
    nOFbatches = int(MNIST.test.num_examples / batch_size)#number of batches
    total_correct_preds = 0
    for j in range(nOFbatches):
        X_batch, Y_batch = MNIST.test.next_batch(batch_size)
        _,loss_batch,logits_batch = sess.run([optimizer, loss, logits],feed_dict={X: X_batch, Y:Y_batch})
        preds = tf.nn.softmax(logits_batch)
        correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(Y_batch, 1))
        accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))
        total_correct_preds += sess.run(accuracy)
    print("Accuracy {0}".format(total_correct_preds/MNIST.test.num_examples))
writer = tf.summary.FileWriter('./graphs/Lab1', sess.graph)
writer.close()

