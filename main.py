import cv2
from seg_import import segment
from PIL import Image
import numpy as np
from extractor import extract

seg = segment('Models/yolov8/train/weights/best.pt')
ext = extract()

img = cv2.imread('input/inp5.jpg')

mask = np.zeros_like(img)

bboxes, bboxdim, segmentations, scores = seg.detect(img)

cv2.fillPoly(mask, segmentations, (255,255,255))
mask_inv = cv2.bitwise_not(mask)

masked_img = cv2.bitwise_and(img, mask)

background = np.ones_like(img, np.uint8)*255
background_masked = cv2.bitwise_and(background, mask_inv)

result = cv2.add(masked_img, background_masked)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

#cv2.imshow('target',result)

reform_img = Image.fromarray(result)
colors = ext.extract_color(reform_img)
print(colors)