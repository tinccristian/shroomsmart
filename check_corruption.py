import os
import tensorflow as tf

shroomNames=['Agaricus',
            'Amanita',
            'Boletus',
            'Cortinarius',
            'Entoloma',
            'Hygrocybe',
            'Lactarius',
            'Russula',
            'Suillus']
num_skipped = 0
for folder_name in shroomNames:
    folder_path = os.path.join("mushrooms_train", folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
        finally:
            fobj.close()

        if not is_jfif:
            num_skipped += 1
            print(f"Removed {fname} as it is corrupted.")
            # Delete corrupted image
            os.remove(fpath)

print("Deleted %d images" % num_skipped)
