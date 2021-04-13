import darknet as dn
import cv2


class YOLO:
    def __init__(self, cfg_path, data_path, weights_path):
        self.network, self.class_names, self.class_colors = dn.load_network(cfg_path, data_path, weights_path)
        self.width = dn.network_width(self.network)
        self.height = dn.network_height(self.network)

    def detect(self, frame):
        darknet_image = dn.make_image(self.width, self.height, 3)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, (self.width, self.height),
                                 interpolation=cv2.INTER_LINEAR)

        # get image ratios to convert bounding boxes to proper size
        img_height, img_width, _ = frame.shape
        width_ratio = img_width / self.width
        height_ratio = img_height / self.height

        # run model on darknet style image to get detections
        dn.copy_image_from_bytes(darknet_image, img_resized.tobytes())
        detections = dn.detect_image(self.network, self.class_names, darknet_image)
        dn.free_image(darknet_image)

        results = []
        for label, confidence, bbox in detections:
            if float(confidence) <= 90.0:
                continue

            left, top, right, bottom = dn.bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(
                right * width_ratio), int(bottom * height_ratio)

            results.append((left, top, right, bottom))

        return results