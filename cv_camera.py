from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2


def main():
    camera = PiCamera()
    camera.rotation = 180
    resolution = (1024, 768)
    camera.resolution = resolution

    raw_capture = PiRGBArray(camera, size=resolution)
    sleep(1) # let camera warm up

    for frame in camera.capture_continuous(raw_capture, format='bgr', use_video_port=True):
        image = frame.array
        cv2.imshow('press Q to exit', image)

        key = cv2.waitKey(delay=1) & 0xff

        # clear the stream in preparation for the next frame
        raw_capture.truncate(0)

        # if 'q' was pressed exit
        if key == ord('q'):
            break


if __name__ == '__main__':
    main()
