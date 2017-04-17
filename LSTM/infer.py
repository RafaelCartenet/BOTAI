import tensorflow as tf
import numpy as np


state_size = 10
input_size = 1
output_size = 1
num_steps = 10
num_layers = 1

batch_size = 2

inputs = tf.placeholder(tf.float32, [batch_size, num_steps, input_size])
outputs = tf.placeholder(tf.float32, [batch_size, num_steps])

cell = tf.nn.rnn_cell.LSTMCell(state_size, state_is_tuple=True)
cell = tf.nn.rnn_cell.MultiRNNCell([cell] * num_layers, state_is_tuple=True)
init_state = cell.zero_state(batch_size, tf.float32)
rnn_outputs, final_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=init_state)

with tf.variable_scope('tanh'):
    W = tf.get_variable('W', [state_size, output_size])
    b = tf.get_variable('b', [output_size], initializer=tf.constant_initializer(0.0))

rnn_outputs = tf.reshape(rnn_outputs, [-1, state_size])

logits = tf.nn.tanh(tf.matmul(rnn_outputs, W) + b)

testX = np.array(batch_size*[[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]])


saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, "./model.ckpt")
    print("Model restored.")
    print(logits.eval(feed_dict={inputs:testX}))
