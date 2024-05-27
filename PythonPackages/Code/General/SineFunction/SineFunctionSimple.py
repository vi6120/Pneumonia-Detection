# https://stackoverflow.com/questions/51091758/learning-a-sin-function

from math import sin

xs = np.arange(-10, 40, 0.1)
squarer = lambda t: sin(t)
vfunc = np.vectorize(squarer)
ys = vfunc(xs)

model= Sequential()
model.add(Dense(units=256, input_shape=(1,), activation="tanh"))
model.add(Dense(units=256, activation="tanh"))
#..a number of layers here
model.add(Dense(units=256, activation="tanh"))
model.add(Dense(units=1))
model.compile(optimizer="sgd", loss="mse")
model.fit(xs, ys, epochs=500, verbose=0)

test_xs = np.arange(-15, 45, 0.01)
test_ys = model.predict(test_xs)
plt.plot(xs, ys)
plt.plot(test_xs, test_ys)
