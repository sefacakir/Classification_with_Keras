import cv2
import tensorflow
from keras.preprocessing import image
import numpy as np  

model = tensorflow.keras.models.load_model(r".\Models\ThreeClassModel6_model.h5")


test_path = r'.\Data\ThreeClassDataBase\Test'

test_datagen = tensorflow.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255
        )

test_generator = test_datagen.flow_from_directory(
        test_path,
        target_size=(224, 224),
        batch_size=16,
        )

test_loss, test_acc = model.evaluate_generator(test_generator, steps=50)
print('test acc:', test_acc)
print('lost acc:', test_loss)