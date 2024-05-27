import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import BatchNormalization, LeakyReLU
from tensorflow.keras.layers import Dense, Reshape, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

# Modul mit Statistikfunktionen
from statistics import Statistics

IMAGE_ROWS = 28
IMAGE_COLS = 28
CHANNELS = 1
IMAGE_SHAPE = (IMAGE_ROWS, IMAGE_COLS, CHANNELS)
Z_DIM = 100

SAMPLE_INTERVAL = 10
stat = Statistics(SAMPLE_INTERVAL)


def build_generator():
    model = Sequential()

    model.add(Dense(256, input_dim=Z_DIM))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(1024))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(np.prod(IMAGE_SHAPE), activation='tanh'))
    model.add(Reshape(IMAGE_SHAPE))

    return model


def build_discriminator():
    model = Sequential()

    model.add(Flatten(input_shape=IMAGE_SHAPE))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(256))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(1, activation='sigmoid'))

    return model


def train(iterations, batch_size=128):

    (X_train, _), (_, _) = mnist.load_data()

    X_train = X_train / 127.5 - 1. # Werte zwischen -1 und 1
    X_train = np.expand_dims(X_train, axis=3)

    stat.orig_images(X_train)

    valid = np.ones((batch_size, 1)) # labels
    gen = np.zeros((batch_size, 1))

    for iteration in range(iterations):

        # Train Discriminator

        idx = np.random.randint(0, X_train.shape[0], batch_size)
        imgs = X_train[idx]

        noise = np.random.normal(0, 1, (batch_size, Z_DIM))
        gen_imgs = generator.predict(noise)

        d_loss_real = discriminator.train_on_batch(imgs, valid)
        d_loss_gen = discriminator.train_on_batch(gen_imgs, gen)
        d_loss = 0.5 * np.add(d_loss_real, d_loss_gen)

        # Train Generator

        noise = np.random.normal(0, 1, (batch_size, Z_DIM))
        g_loss = combined.train_on_batch(noise, valid)

        stat.add(iteration, d_loss[0], 100 * d_loss[1], g_loss, generator, Z_DIM)


optimizer = Adam(0.0002, 0.5)

discriminator = build_discriminator()
discriminator.compile(loss='binary_crossentropy',
optimizer=optimizer,
metrics=['accuracy'])

generator = build_generator()
discriminator.trainable = False
combined = Sequential([generator, discriminator])
combined.compile(loss='binary_crossentropy', optimizer=optimizer)


ITERATIONS = 10000
BATCH_SIZE = 32

train(iterations=ITERATIONS, batch_size=BATCH_SIZE)

stat.print_plot()