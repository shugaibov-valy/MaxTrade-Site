from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import argparse


def predict_text(path):
    parser  = argparse.ArgumentParser()
    parser.add_argument('--img_path', type=str, default=f'{path}')
    parser.add_argument('--model_path', type=str, default='trash_detect.h5')
    args = parser.parse_args()

    model = load_model(args.model_path)

    W, H, D = 224, 224, 3

    img = image.load_img(args.img_path, target_size=(W,H,D))
    img_tensor = image.img_to_array(img)
    img_tensor /= 255.
    pred = model.predict(np.expand_dims(img_tensor, axis=0))
    if pred[0][0] > 0.5:
        return 'Много мусора'
    else:
        return 'Бак не заполнен' 