#Library Data Manipulation
import numpy as np
import pandas as pd
import csv

#Library DL
from keras.models import Sequential
from keras.layers import Dense

#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#

#Reading csv files
num_range = 100000 #number of set of points

file_points = pd.read_csv('train_100k.csv')
dataset_points = file_points.values
points = dataset_points[0:num_range,1:].astype('float') #Removing id of each row

file_line = pd.read_csv('train_100k_truth.csv')
dataset_line = file_line.values
line = dataset_line[0:num_range,1:].astype('float') #Removing id of each row

file_test = pd.read_csv('test_100k.csv')
dataset_test = file_test.values
test = dataset_test[0:num_range,1:].astype('float') #Removing id of each row

#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#

#Determining the number of   
num_inputs = len(points[0,:])
num_outputs = len(line[0,:])

#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#

#using "dense" or "fully connected layer"
model = Sequential()
model.add(Dense(4, input_dim=num_inputs,activation='linear', kernel_initializer='glorot_uniform')) #criou o modelo
model.add(Dense(num_outputs))
model.compile(optimizer='adam', loss='mean_squared_error', metrics= ['accuracy'])
model.fit(points,line,epochs=2,batch_size=1) 

result = model.predict(np.asmatrix(test)) #Predcting Test_Data

#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#

#Creating file csv 
with open('submission_train_100k.csv','w', newline='') as f:
    fieldnames = ['id' , 'slope' , 'intercept']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for l in range(0,num_range):
        writer.writerow({ fieldnames[0] : l ,fieldnames[1] :  result[l][0] , fieldnames[2] :  result[l][1] })

#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#-------#








