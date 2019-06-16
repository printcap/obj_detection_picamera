from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2


def main():

    label_dict = {}
    with open('models/ssd_mobilenet/labels.txt','r') as f:
        for l in f:
            arr = l.strip().split(':')
            label_dict[int(arr[0])] = arr[1].strip()

    model = cv2.dnn.readNetFromTensorflow(
                'models/ssd_mobilenet/frozen_inference_graph.pb',
                'models/ssd_mobilenet/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    camera = PiCamera()
    camera.rotation = 180
    resolution = (640, 480)
    cols, rows = resolution
    camera.resolution = resolution

    raw_capture = PiRGBArray(camera, size=resolution)
    sleep(1) # let camera warm up

    color = (23, 230, 210)

    for frame in camera.capture_continuous(raw_capture, format='bgr', use_video_port=True):
        image = frame.array

        model.setInput(cv2.dnn.blobFromImage(image, size=resolution, swapRB=True, crop=False))
        net_out = model.forward()

        for detection in net_out[0,0,:,:]:
            score = float(detection[2])
            if score > 0.5: 
                label = int(detection[1])
                label_str = label_dict.get(label, 'unknown')
                print(label_str)

                left = detection[3] * cols
                top = detection[4] * rows
                right = detection[5] * cols
                bottom = detection[6] * rows
                cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), color, thickness=2)
                cv2.putText(image, label_str, (int(left) + 3, int(bottom) - 3), cv2.FONT_HERSHEY_SIMPLEX, 
                            1.0, color)
        
        cv2.imshow('press Q to exit', image)

        key = cv2.waitKey(delay=1) & 0xff

        # clear the stream in preparation for the next frame
        raw_capture.truncate(0)

        # if 'q' was pressed exit
        if key == ord('q'):
            break


if __name__ == '__main__':
    main()
