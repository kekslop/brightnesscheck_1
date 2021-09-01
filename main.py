import numpy as np
import cv2
import glob

def img_estim(img, thrshld):



    black = np.count_nonzero(img < thrshld)
    confidence = black/img.size * 100
    #print(img < 50)
    #print(img)
    #print(black)
    return confidence

for file in glob.glob("jpg/*"):
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #print(img_estim(gray, 40))
    conf = img_estim(gray, 60)
    if conf > 55:
        cv2.imshow('ImageWindow', img)
        cv2.imwrite(file.replace("jpg","dark", 1), img)
        print(conf)
    cv2.waitKey(1)
