import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    size = (150,150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resize =(cv2.resize(img, dsize=(75, 75),
    interpolation=cv2.INTER_CUBIC))/255.
    img_reshape = img_resize[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
st.image(image, use_column_width=True)
prediction = import_and_predict(image, model)
if np.argmax(prediction) == 0:
    st.write("Benign!")
elif np.argmax(prediction) == 1:
    st.write("Malignant")
else:
    st.write("No Skin Cancer!")
st.text("Probability (0: Benign, 1: Malignant, 2: No Skin Cancer")
st.write(prediction)