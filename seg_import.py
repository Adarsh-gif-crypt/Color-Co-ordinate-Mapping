from ultralytics import YOLO
import numpy as np

class segment:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, img):

        h, w, c = img.shape

        results = self.model.predict(source = img.copy(), save = False, save_txt = False)
        result = results[0]

        seg_contours_id = []

        for seg in result.masks.segments:

            seg[:, 0] *= w
            seg[:, 1] *= h
            segment = np.array(seg, dtype = np.int32)
            seg_contours_id.append(segment)

        bboxes = np.array(result.boxes.xyxy.cpu(), dtype = 'int')
        bboxes1 = np.array(result.boxes.xywh.cpu(), dtype = 'int')
        score = np.array(result.boxes.conf.cpu(), dtype = 'float')

        return bboxes, bboxes1, seg_contours_id, score