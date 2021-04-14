import cv2

from utils.YOLO import YOLO
from utils.CNN import CNN


class Recognizer:
    def __init__(self):
        self.yolo = YOLO("cfg/yolov4-tiny-obj.cfg", "cfg/ear.data", "models/yolov4-tiny-obj_final.weights")
        self.cnn = CNN("models/EarDetectionModel")

    def detect(self, frame):
        try:
            # get yolo detection results
            detection = self.yolo.detect(frame)
            if detection is not None:
                left, top, right, bottom = detection

                # crop ear and detect identity
                crop = frame[top:bottom, left:right]
                name, value = self.cnn.detect(crop)

                # draw results on frame
                frame = cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                frame = cv2.putText(frame, f"{name}, {value}",
                                    (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            return name, frame

        except:
            return None, frame


