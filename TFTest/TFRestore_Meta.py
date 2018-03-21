# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'

import tensorflow as tf
from  tensorflow.examples.tutorials.mnist import  input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

sess = tf.Session()

new_saver = tf.train.import_meta_graph('MNIST_data1/test.ckpt.meta')
new_saver.restore(sess, 'MNIST_data1/test.ckpt')

x = tf.get_collection('x')[0]
y = tf.get_collection('y')[0]

print("restore meta")

idx = 8800
img = mnist.test.images[idx]

ret = sess.run(y, feed_dict={x: img.reshape(1, 784)})

print("预测结果：%d"%(ret.argmax()))
print("实际结果：%d"%(mnist.test.labels[idx].argmax()))