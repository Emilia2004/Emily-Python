import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense,Dropout
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

(x_train, y_train),(x_test, y_test)=cifar10.load_data()
x_train=x_train/ 255.0
x_test=x_test/255.0
y_train=to_categorical(y_train,10)
y_test=to_categorical(y_test,10)

model=Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
    MaxPooling2D((2,2)),
    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(128,(3,3),activation='relu'),
    Flatten(),
    Dense(128,activation='relu'),\
    Dropout(0.5),
    Dense(10,activation='softmax')
])

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10,batch_size=64,validation_split=0.2)

test_loss, test_acciracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acciracy * 100:.2f}%")
print(f"Test Loss:{test_loss:.2f}")


