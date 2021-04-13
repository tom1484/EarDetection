from utils.YOLO import YOLO
from utils.CNN import CNN_Model, CNN
import cv2

# load models
yolo = YOLO("cfg/yolov4-tiny-obj.cfg", "cfg/ear.data", "models/yolov4-tiny-obj_final.weights")
cnn = CNN("models/EarDetectionModel")

# start streaming
cap = cv2.VideoCapture(4)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # get yolo detection results
            detections = yolo.detect(frame)
            for left, top, right, bottom in detections:
                # crop ear and detect identity
                crop = frame[top:bottom, left:right]
                name, value = cnn.detect(crop)

                # draw results on frame
                frame = cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                frame = cv2.putText(frame, f"{name}, {value}",
                                    (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        except:
            pass

        cv2.imshow('frame', cv2.resize(frame, None, fx=3.5, fy=3.5))
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
