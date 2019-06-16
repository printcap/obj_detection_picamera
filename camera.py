from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()
    camera.rotation = 180

    camera.start_preview()
    sleep(10)
    camera.stop_preview()


if __name__ == '__main__':
    main()
