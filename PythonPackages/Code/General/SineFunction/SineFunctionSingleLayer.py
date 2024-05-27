# sine sequence

import numpy as np
import matplotlib.pyplot as plt
from keras import models, layers, optimizers, datasets, utils, losses

# sine data with 10 steps/cycle
seq = np.array([np.sin(2*np.pi*i/10) for i in range(10)])
print(seq)

num_seq = 200
x_train = np.array([])
y_train = np.array([])

for i in range(num_seq):
    ran = np.random.randint(10)
    x_train = np.append(x_train, seq[ran])
    y_train = np.append(y_train, seq[np.mod(ran+1, 10)])

x_test = np.array(seq)
y_test = np.array(np.roll(seq, -1))



# MLP2
inputs = layers.Input(shape = (2, ))
h = layers.Dense(2, activation = 'relu')(inputs)
outputs = layers.Dense(1, activation = 'tanh')(h)
model = models.Model(inputs, outputs)

model.compile(loss = 'mean_squared_error', optimizer = 'adam')
print(model.summary())
model.fit(x_train, y_train, epochs = 1000, batch_size = 100, verbose = 0)

# evaluate
y_pred = model.predict(x_test, batch_size = 10, verbose = 1)
plt.plot(y_test, 'x')
plt.plot(y_pred, 'o')

