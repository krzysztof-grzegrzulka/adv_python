import time

import cv2
import numpy as np


def person_counter(img_file_path):
    # argument i uzyte zmienne
    img = cv2.imread(img_file_path)
    req_width = 608
    req_height = 608
    box_color = (0, 0, 255)

    yolo_weight = "models/yolov3.weights"  # yolov3-608
    yolo_config = "models/yolov3.cfg"
    coco_labels = "models/coco.names"
    net = cv2.dnn.readNet(yolo_weight, yolo_config)

    # poczatek obliczania czasu przetwarzania
    start = time.time()

    # zmniejszenie pliku do rozmiaru wymaganego przez wersje YOLO
    # i konwersja do Bloba
    img = cv2.resize(img, (req_width, req_height))
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 1 / 255, (req_width, req_height),
                                 (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # okreslenie nazw warstw wyjsciowych
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    outs = net.forward(output_layers)

    # wyciaganie info z detekcji
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            # rodzaj obiektu
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # zaznaczanie tylko ludzi
            if confidence > 0.5 and class_id == 0:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))

    # ominircie nachodzacych na siebie ramek
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), box_color, 2)

    # koniec obliczania czasu przetwarzania
    end = time.time()

    print('Liczba wykrytych osob: ', len(indexes), '\nczas obrobki: ', end - start)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
