# ired_ws

For Robot-Arm https://github.com/Mark-Teeratorn/ired_ws/tree/main/examples


For Realsense Camera https://github.com/IntelRealSense/realsense-ros

You need to install Intel Realsense permission scripts located in librealsense source directory.
  For that, first, git clone the librealsense to a local folder

git clone https://github.com/IntelRealSense/librealsense

Next, run the following commands to copy the 99-realsense-libusb.rules files to the rules.d folder

sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/

And, then udevadm control to modify the internal state of the running udev dameon to reload rules. Also, udevadm trigger to request device events from the kernel.

sudo udevadm control --reload-rules
sudo udevadm trigger

sudo apt update
sudo apt install -y ros-jazzy-realsense2-camera ros-jazzy-realsense2-description

pip3 install --break-system-packages opencv-python opencv-contrib-python transforms3d

pip3 uninstall -y numpy
pip3 install --break-system-packages "numpy==1.26.4"

https://github.com/AIRLab-POLIMI/ros2-aruco-pose-estimation.git

update Topic and Firware of Realsense
