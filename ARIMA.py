
# coding: utf-8

# In[16]:

from pandas import Series
series = Series.from_csv('C:/Users/admin/Desktop/project4-4/data_p1/2016040S12094.csv', header=0)
split_point = len(series) - 10
dataset, validation = series[0:split_point], series[split_point:]
print('Dataset %d, Validation %d' % (len(dataset), len(validation)))
dataset.to_csv('dataset.csv')
validation.to_csv('validation.csv')


# In[17]:

X = series.values
X = X.astype('float32')
train_size = int(len(X) * 0.50)
train, test = X[0:train_size], X[train_size:]


# In[18]:

from pandas import Series
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from math import sqrt


# In[19]:

history = [x for x in train]
predictions = list()
for i in range(len(test)):
	# predict
	model = ARIMA(history, order=(0,1,0))
	model_fit = model.fit(disp=0)
	yhat = model_fit.forecast()[0]
	predictions.append(yhat)
	# observation
	obs = test[i]
	history.append(obs)
	print('>Predicted=%.3f, Expected=%3.f' % (yhat, obs))
# report performance
mse = mean_squared_error(test, predictions)
rmse = sqrt(mse)
print('RMSE: %.3f' % rmse)


# In[12]:

import pandas as pd

my_df = pd.DataFrame(predictions)
my_df.to_csv('p23047.csv', index=False, header=False)


# In[24]:

import numpy
max = numpy.amax(predictions)
print max


# In[26]:

def categorization(maxwinds):
     if(maxwinds<=17):
        print("The winds fall into tropical depression category.")
        
     elif(maxwinds>17 and maxwinds<32):
        print("The winds fall into tropical storm category.")
             


# In[27]:

categorization(max)


# In[ ]:



