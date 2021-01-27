import cv2
import numpy as np
from keras.models import load_model
new_model = load_model('ImageClassifier.h5')
new_model.compile('adam', 'sparse_categorical_crossentropy', ['accuracy'])
import glob

L=0
R=0
images = glob.glob('L/*.*')
for img in images:
    img = cv2.imread(img)
    img = cv2.resize(img,(16,16))
    img = np.reshape(img,[1,16,16,3])

    cls = new_model.predict_classes(img)
    
    if cls==0:
        L+=1
    elif cls==1:
        R+=1
        
print(L)
print(R)
