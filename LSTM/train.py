import tensorflow as tf
import numpy as np
import time
import csv

# PARAMETERS
state_size = 10
input_size = 1
output_size = 1
num_steps = 10#20
num_layers = 2
batch_size = 2#200
nb_epochs = 80000
treshold = 0.20
learning_rate = 0.01
np.random.seed(10)


#--------------------#
# DATA CLASS
#--------------------#

class Data:
    def __init__(self, filename, normalise = False, ratiotrte=0.90):
        self.train_test_ratio = ratiotrte
        self.file = filename
        self.SPs = None
        self.tendencies = None
        self.N = None
        self.normalise = normalise

    # normalise a sequence of strike prices. First value is 0 and the others are the relative variance
    def normalise_window(self, window):
        normalised_window = [[((float(p[0]) / float(window[0][0])) - 1)] for p in window]
        return normalised_window

    # load strike prices inside a list of format [[SP1], [SP2], ... , [SPN]]
    def load(self):
        with open(self.file, 'r') as f:
            data = [row for row in csv.reader(f.read().splitlines(), delimiter = ";")][1:]
            data = [[float(dat[-1])] for dat in data]
            self.SPs = data
            self.N = len(self.SPs)

    # computes the tendency. tendencies[t] =
    #  +1 if SP[t+1] > SP[t]
    #  -1 if SP[t+1] > SP[t]
    #  0 if SP[t+1] = SP[t]
    def compute_tendency(self):
        self.tendencies = []
        for i in range(self.N-1):
            if self.SPs[i+1] > self.SPs[i]:
                self.tendencies.append(1)
            elif self.SPs[i+1] < self.SPs[i]:
                self.tendencies.append(-1)
            else:
                self.tendencies.append(0)
        del self.SPs[-1] # We remove the last strike price as we can't evaluate tendency.
        self.N -= 1

    def gen_batchs(self, nb_batchs, st):
        batches = []
        nbelements = batch_size
        for i in range(nb_batchs):
            dataX = np.reshape(self.SPs[st+i*nbelements:st+(i+1)*nbelements], [batch_size, num_steps, input_size])
            dataY = np.reshape(self.tendencies[st+i*nbelements:st+(i+1)*nbelements], [batch_size, num_steps, output_size])
            batches.append([dataX, dataY])
        return batches

    def gen_datasets(self):
        # We determine number of sequences (= windows) that we can create out of the dataset
        nbwindows = self.N // num_steps

        # We reshape the strike prices and the tendencies in nbwindows * num_steps * input_size matrices.
        self.SPs = np.reshape(self.SPs[:nbwindows*num_steps], [nbwindows, num_steps, input_size])
        self.tendencies = np.reshape(self.tendencies[:nbwindows*num_steps], [nbwindows, num_steps, output_size])

        # Normalisation of the strike prices
        if self.normalise:
            for i in range(nbwindows):
                self.SPs[i] = self.normalise_window(self.SPs[i])

        # Shuffling of the windows
        arr = np.random.permutation(nbwindows)
        self.SPs = self.SPs[arr]
        self.tendencies = self.tendencies[arr]

        # Numbers of windows dedicated to training and testing
        nb_train_windows = int(nbwindows * self.train_test_ratio - (nbwindows * self.train_test_ratio)%batch_size)
        nb_test_windows = int(nbwindows - nb_train_windows)

        # Numbers of batchs dedicated to training and testing
        nb_batchs = nbwindows // batch_size
        nb_batchs_train = int(self.train_test_ratio * nb_batchs)
        nb_batchs_test = nb_batchs - nb_batchs_train

        # Extract the batches from the dataset according to the number of batches and the starting index where to start extraction.
        self.batchs_train = self.gen_batchs(nb_batchs_train, 0)
        self.batchs_test  = self.gen_batchs(nb_batchs_test, nb_batchs_train*batch_size)


#--------------------#
# TENSORFLOW MODEL
#--------------------#
def tf_count(t, val):
    elements_equal_to_value = tf.equal(t, val)
    as_ints = tf.cast(elements_equal_to_value, tf.int32)
    count = tf.reduce_sum(as_ints)
    return count

# input/output placeholders
inputs = tf.placeholder(tf.float32, [batch_size, num_steps, input_size])
outputs = tf.placeholder(tf.float32, [batch_size, num_steps, output_size])

# definition of the RNN

try:
    cell = tf.contrib.rnn.LSTMCell(state_size, state_is_tuple=True)
    cell = tf.contrib.rnn.MultiRNNCell([cell] * num_layers, state_is_tuple=True)
except AttributeError:
    cell = tf.nn.rnn_cell.LSTMCell(state_size, state_is_tuple=True)
    cell = tf.nn.rnn_cell.MultiRNNCell([cell] * num_layers, state_is_tuple=True)

init_state = cell.zero_state(batch_size, tf.float32)
rnn_outputs, final_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=init_state)


# last fully connected layer on top of the RNN
with tf.variable_scope('tanh'):
    W = tf.get_variable('W', [state_size, output_size])
    b = tf.get_variable('b', [output_size], initializer=tf.constant_initializer(0.0))

# reshaping of the outputs and the ground truth label for comparison
y_reshaped = tf.reshape(outputs, [-1, num_steps, output_size])
rnn_outputs = tf.reshape(rnn_outputs, [-1, state_size])

# activation function : tanh
logits = tf.nn.tanh(tf.matmul(rnn_outputs, W) + b)
logits = tf.reshape(logits, [-1, num_steps, output_size])
final_result = tf.round(logits)

real_next = y_reshaped[:, -1]
next_pred = final_result[:, -1]

# loss function
total_loss = tf.reduce_sum(tf.pow(outputs - logits,2))/(num_steps)

# accuracy function
correct_prediction = tf.equal(final_result, outputs)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

nextpred_correct_prediction = tf.equal(real_next, next_pred)
nextpred_accuracy = tf.reduce_mean(tf.cast(nextpred_correct_prediction, tf.float32))

# maximizer
train_step = tf.train.AdamOptimizer(learning_rate).minimize(total_loss)


test = y_reshaped[:, :, 0]


#--------------------#
# DATA LOADING
#--------------------#
dataset = Data("../data/EURUSD.csv", normalise = True)
dataset.load()
dataset.compute_tendency()
dataset.gen_datasets()


#--------------------#
# DEBUGGING
#--------------------#
# test data

testX = np.array(batch_size*[[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]])
testY = np.array(batch_size*[[[1], [-1], [0], [1], [1], [0], [1], [-1], [1], [1]]])

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    fd = feed_dict={inputs: testX, outputs: testY}
    print("y_reshaped")
    print(y_reshaped.eval(fd))
    print("test")
    print(test.eval(fd))
    #print(tf_count(y_reshaped.eval(fd), 0))
    print("final result")
    print(final_result.eval(fd))
    print(real_next.eval(fd))
    print(next_pred.eval(fd))
    print(accuracy.eval(fd))
    print(nextpred_accuracy.eval(fd))

assert()

#--------------------#
# TRAINING
#--------------------#
saver = tf.train.Saver()

displaystep = 30

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epochID in range(nb_epochs):
        epoch_loss = 0
        epoch_accu = 0
        epoch_top1accu = 0
        nb_batchs = len(dataset.batchs_train)
        t = time.time()
        for batch in dataset.batchs_train:
            dataX, dataY = batch
            loss = sess.run([total_loss, train_step], feed_dict={inputs: dataX, outputs: dataY})
            t = time.time() - t
            accu = accuracy.eval(feed_dict={inputs: dataX, outputs: dataY})
            top1accu = nextpred_accuracy.eval(feed_dict={inputs: dataX, outputs: dataY})
            epoch_loss += loss[0]/(nb_batchs*batch_size)
            epoch_accu += 100*(accu)/nb_batchs
            epoch_top1accu += 100*(top1accu)/nb_batchs
        sp = nb_batchs * batch_size / (time.time() - t)
        if epochID % 1 == 0:
            print "train epoch: ", epochID, "\terr: ",epoch_loss,"\taccu : %.2f \t@1accu : %.2f \tspeed : %.2f win/s" % (epoch_accu, epoch_top1accu, sp)
        if epochID % 10 == 0:
            epoch_loss = 0
            epoch_accu = 0
            epoch_top1accu = 0
            nb_batchs = len(dataset.batchs_test)
            for batch in dataset.batchs_test:
                dataX, dataY = batch
                loss = total_loss.eval(feed_dict={inputs: dataX, outputs: dataY})
                accu = accuracy.eval(feed_dict={inputs: dataX, outputs: dataY})
                top1accu = nextpred_accuracy.eval(feed_dict={inputs: dataX, outputs: dataY})
                epoch_loss += loss/(nb_batchs*batch_size)
                epoch_accu += 100*(accu)/nb_batchs
                epoch_top1accu += 100*(top1accu)/nb_batchs
            print "test  epoch: ", epochID, "\terr: ",epoch_loss,"\taccu : %.2f \t@1accu : %.2f" % (epoch_accu, epoch_top1accu)
