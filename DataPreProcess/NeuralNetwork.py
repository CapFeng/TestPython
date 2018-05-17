import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

INPUT_NODE = 30
OUTPUT_NODE = 1

data = np.loadtxt('C:\\Users\\wbl\\Desktop\\KDDCup\\20160504.txt', dtype='float32', delimiter=',')


def add_layer(inputs, in_size, out_size, activation_function=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs, weights) + biases
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs

train_num = int(len(data) * 0.8)

train_x = data[: train_num, : INPUT_NODE]
train_y = data[: train_num, (OUTPUT_NODE * -1):]
test_x = data[train_num:, : INPUT_NODE]
test_y = data[train_num:, (OUTPUT_NODE * -1):]


xs = tf.placeholder(tf.float32, [None, 30])
ys = tf.placeholder(tf.float32, [None, 1])
# add hidden layer l1
L1 = add_layer(xs, 30, 10, activation_function=tf.nn.relu)
# add hidden layer l2
L2 = add_layer(L1, 10, 10, activation_function=tf.nn.relu)

prediction = add_layer(L2, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

# define Optimizer
# train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
train_step = tf.train.AdamOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
# iterations
num_boost = 4500

with tf.Session() as sess:
    sess.run(init)
    # plot the real data

    for i in range(num_boost):
        # training
        sess.run(train_step, feed_dict={xs: train_x, ys: train_y})
        if i % 1000 == 0:
            # to visualize the result and improvement

            prediction_value = sess.run(prediction, feed_dict={xs: train_x})
            # plot the prediction

            print(sess.run(loss, feed_dict={xs: train_x, ys: train_y}))

    print(test_x)
    result = sess.run(prediction, feed_dict={xs: test_x})
    print(result)
    plt.plot(test_y)
    plt.plot(result)
    plt.show()
