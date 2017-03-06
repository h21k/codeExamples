x = 'a'
y = 'b'
z = 'c'

from keras.models import Sequential

model = Sequential()

x = 'model done'
print(x)

from keras.layers import Dense, Activation

model.add(Dense(output_dim=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(output_dim=10))
model.add(Activation("softmax"))

y = 'adds done'
print(y)

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

z = 'compile done'
print(z)

from keras.optimizers import SGD

#If you need to, you can further configure your optimizer. A core principle of Keras is to make things reasonably simple, while allowing the user to be fully in control when they need to (the ultimate control being the easy extensibility of the source code).

from keras.optimizers import SGD
model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))

#You can now iterate on your training data in batches:

model.fit(X_train, Y_train, nb_epoch=5, batch_size=32)

#Alternatively, you can feed batches to your model manually:

model.train_on_batch(X_batch, Y_batch)

#Evaluate your performance in one line:

loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)

#Or generate predictions on new data:

classes = model.predict_classes(X_test, batch_size=32)
proba = model.predict_proba(X_test, batch_size=32)
