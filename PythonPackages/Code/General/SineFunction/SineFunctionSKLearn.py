from sklearn.neural_network import MLPRegressor
import numpy as np

f = lambda x: [[x_] for x_ in x]
noise_level = 0.1
X_train_ = np.arange(0, 10, 0.2)
real_sin = np.sin(X_train_)
y_train = real_sin+np.random.normal(0,noise_level,len(X_train_))    

N = 100

regr = MLPRegressor(hidden_layer_sizes= tuple([N]*5)).fit(f(X_train_), y_train)

predicted_sin = regr.predict(f(X_train_))