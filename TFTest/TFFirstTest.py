# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 初始化输入参数
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3
# 可见输入参数是一组给定值，我们需要修正
# plt.scatter(x_data, y_data)
# plt.show()

############### 定义结构 ###########
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
############### 定义结构 ###########


# tf输入变量的初始化，并且开始激活Session
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

# 开始训练
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(y)   # sess.run的值一定要是个tensor！！！
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)   # 红色，线宽为5
        plt.pause(0.5)
