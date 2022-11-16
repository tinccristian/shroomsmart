import tensorflow as tf
from tensorflow import keras
from keras import layers

# data  
shroomPath='D:\projects\mushrooms\mushrooms_train'
shroomNames=['Agaricus',
            'Amanita',
            'Boletus',
            'Cortinarius',
            'Entoloma',
            'Hygrocybe',
            'Lactarius',
            'Russula',
            'Suillus']
#6039 pictures
#endregion

image_size = (180, 180)
batch_size = 32

train_ds, val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "mushrooms_train",
    labels="inferred",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
