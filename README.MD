# MobileNet SSD Object Detection

## with Raspberry Pi 3 with PiCamera

Runs object detection on a Raspberry Pi 3 using input from an attached Pi Camera. Implementation in Python using OpenCV2 is based on a
[MobileNet-SSD v2]() model in TensorFlows ProtoBuf format.

Description of how to access Pi Camera from Python see 
[Picamera Documentation](https://picamera.readthedocs.io/en/release-1.13/quickstart.html).
The explanation of how to perform inference in OpenCV2 on a TensorFlow model can be found in the [OpenCV Wiki](https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API).

### Setup

Install [TensorFlow on Raspberry Pi](https://www.tensorflow.org/install/pip) through pip.

```bash
sudo apt update
sudo apt install python3-dev python3-pip
sudo apt install libatlas-base-dev        # required for numpy
sudo pip3 install -U virtualenv           # system-wide install
```

```bash
virtualenv --system-site-packages -p python3 ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install --upgrade tensorflow

# Test TensorFlow
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000,1000])))"
```

The installation of OpenCV2 described in [here](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/blob/master/README.md) seemed to have worked too.

 ```bash
sudo apt install libtiff5-dev libjasper-dev libpng12-dev
pip install pillow jupyter matplotlib cython
pip install opencv-python
```

Download MobileNet-SSD v2 [weights](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz) and [config](https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/ssd_mobilenet_v2_coco_2018_03_29.pbtxt).

### Programs

1. `python camera.py` camera output directly into frame buffer
(fullscreen, without image capture and further processing).

2. `python cv_camera.py` camera image is captured into a buffer and
drawn inside a X window using `cv2.imshow`. No further processing of
the image.

3. `python ssd_camera.py` capture image from camera, performan
object detection, draw recognized objects with labels into image and
display image in an X window.
