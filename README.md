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

Use pipx

pipx lets you install and run Python applications in isolated environments. This is the recommended way to install PyPI packages that represent command-line applications.

To install pipx, run:

sudo apt install pipx

pipx needs ~/.local/bin/ to be in your PATH. You can automatically modify your shell configuration (such as ~/.bashrc) to modify PATH appropriately by running:

 pipx ensurepath
(You may need to close your terminal application and open it again for the changes to take effect.)

Now you can install a package from PyPI, like this:

 pipx install pycowsay
