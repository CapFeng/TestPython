# -*- coding: utf-8 -*-
"""
Create on Wednesday April 25 0:34:45 2018
@aurthor SHK
"""

import tensorflow as tf
import numpy as np

# the following constants are all examples, these numbers can be change to any number you like

# input sample has x dimension features, than INPUT_NODE = x, here use 10 as example
# the observed label has y different values, than OUTPUT_NODE = y, here user 10 as example
INPUT_NODE = 30
OUTPUT_NODE = 1

# define 2 hide-layers
LAYER1_NODE = 30
LAYER2_NODE = 10

LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 2000
MOVING_AVERAGE_DECAY = 0.99


# define forward-propagation process;
# avg_class is a trainable-smooth-class, here specially is ExponentialMovingAverage, so we can use avg_class.average() function to smooth w & b
def inference(input_tensor, avg_class, w1, b1, w2, b2, w3, b3):
    if avg_class is None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, w1) + b1)
        layer2 = tf.nn.relu(tf.matmul(layer1, w2) + b2)
        return tf.nn.relu(tf.matmul(layer2, w3) + b3)
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(w1)) + avg_class.average(b1))
        layer2 = tf.nn.relu(tf.matmul(layer1, avg_class.average(w2)) + avg_class.average(b2))
        return tf.nn.relu(tf.matmul(layer2, avg_class.average(w3)) + avg_class.average(b3))


# neural network's train process
def train(data, train_rate):
    # you determine whether to shuffle the data's sequence or not
    # np.random.shuffle(data)

    # get train-test split point
    train_num = int(len(data) * train_rate)

    # less than train-test split point is for training, otherwise is for testing
    # every line in data has INPUT_NODE + OUTPUT_NODE dimension values, including the first INPUT_NODE dimensions as features, and last OUTPUT_NODE dimensions as labels
    train_x = data[: train_num, : INPUT_NODE]
    train_y = data[: train_num, (OUTPUT_NODE * -1):]
    test_x = data[train_num:, : INPUT_NODE]
    test_y = data[train_num:, (OUTPUT_NODE * -1):]

    # because the following values are viables, so that need to use tf.placeholder to hold the space
    x = tf.placeholder(tf.float32, shape=[None, INPUT_NODE], name='x_input')
    y_ = tf.placeholder(tf.float32, shape=[None, OUTPUT_NODE], name='y_input')

    # orderly define weights between current layer and last layer, which are also known as nns' parameters. here initialize them by using Gaussian-Distribution function(tf.truncated_normal)
    w1 = tf.Variable(tf.truncated_normal(shape=[INPUT_NODE, LAYER1_NODE], stddev=0.1))
    b1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))

    w2 = tf.Variable(tf.truncated_normal(shape=[LAYER1_NODE, LAYER2_NODE], stddev=0.1))
    b2 = tf.Variable(tf.constant(0.1, shape=[LAYER2_NODE]))

    w3 = tf.Variable(tf.truncated_normal(shape=[LAYER2_NODE, OUTPUT_NODE], stddev=0.1))
    b3 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    # calculate non-moving-average model's forward-propagation result
    y = inference(x, None, w1, b1, w2, b2, w3, b3)

    # current training iterations
    global_step = tf.Variable(0, trainable=False)

    # define avg_class as ExponentialMovingAverage
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # apply moving-average to all Trainable variables
    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    # calculate moving-average model's forword-propagation result
    average_y = inference(x, variable_averages, w1, b1, w2, b2, w3, b3)

    # define cross-entropy and its loss
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.arg_max(y_, 1))
    cross_entropy_loss = tf.reduce_mean(cross_entropy)

    # define L2 regularizer to regularize weights
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    regularization = regularizer(w1) + regularizer(w2) + regularizer(w3)
    # total loss is cross entropy loss add regularization
    loss = cross_entropy_loss + regularization

    # define learning_rate, third parameter is decay_steps, here use a constant 1000, which can be replaced by data.size / batch_size
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, 1000, LEARNING_RATE_DECAY)
    # define backward-propagation method, here is GradientDescent
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    # combine two step operations
    train_op = tf.group(train_step, variable_averages_op)

    # define correct_rate
    # the final prediction is calculated by moving-average result
    correct_prediction = tf.equal(tf.arg_max(average_y, 1), tf.arg_max(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # initialize session, and start train
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        # initial train data
        validate_feed = {x: train_x, y_: train_y}
        print(type(train_x[0][0]))
        test_feed = {x: test_x, y_: test_y}

        for i in range(TRAINING_STEPS):
            if i % 100 == 0:
                validate_accuracy = sess.run(accuracy, feed_dict=validate_feed)
                print('After %d training steps, validation accuracy using moving-average model is %f' % (i, validate_accuracy))
                print(sess.run(w1), sess.run(b1))
            # due to lacking of data, every round use the same test_feed to train
            sess.run(train_op, feed_dict=validate_feed)

        test_accuracy = sess.run(accuracy, feed_dict=test_feed)
        print('After %d train steps, test accuracy using moving-average model is %f' % (i, test_accuracy))


data = np.loadtxt('C:\\Users\\wbl\\Desktop\\KDDCup\\20160504.txt', dtype='float32', delimiter=',')
train(data, 0.8)
