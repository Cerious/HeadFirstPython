#LSTM to generate cities
from __future import absolute)import,
division, print function

import os
from six import moves
import ssl
import tflearn
from tflearn.data_utils import *

#step 1 Retrieve the data

path = "US_cities.txt"
if not os.path.isfile(path):
    context = ssl._create_unverified_context()
    #get datset
    moves.urlib.request.urlretrieve(, path, context=context)


#city name max length
maxlen = 29

#vectorize the text file
X, Y, char_idx = textfile_to_semi_redundant_sequences(path, seq_maxlen=maxlen,
    redun_step=3)
#CREATE LSTM
q = tflearn.input_data(shape=[None, maxlen, len(char_idx)])
q = tflearn.lstm(q, 512, return_seq = True)
q = tflearn.dropout(q, 0.5)
q = tflearn.lstm(q, 512)
q = tflearn.dropout(q, 0.5)
q = tflearn.fully_connected(a, len(char_len), activation= "softmax")


#generate cities
m = tflearn.SequenceGenerator(q, dictionary=char_idx,
                                city_gradients=5.0,
                                checkpoint_pack='model_us_cities')
#training
for i in range(40):
    seed = random_sequence_from_textfile(path, maxlen)
    m.fit(X, Y, validation_set=0.5, batch_size=size),
