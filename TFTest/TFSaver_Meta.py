# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'


import tensorflow as tf
import os

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)

saver = tf.train.Saver()

tf.add_to_collection('x', x)
tf.add_to_collection('y', y)

for i in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

print("Training OK")

model_dir = "MNIST_data1"
model_name = "test.ckpt"
if not os.path.exists(model_dir):
    os.mkdir(model_dir)

saver.save(sess, os.path.join(model_dir, model_name))

print("Save OK")









