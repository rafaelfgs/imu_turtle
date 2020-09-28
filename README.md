# imu_turtle

Control turtlesim with a smartphone.

## Create workspace for the package:
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/rafaelfgs/imu_turtle.git
cd ..
catkin_make
source devel/setup.bash
```

## Configure the smartphone:

* Install the application for Android "ROS All Sensors Driver"
* Verify computer IP address (ifconfig)
* Start master for ROS (roscore)
* Go into "ROS All Sensors Driver", set your IP adress, check Sensors and Connect

## Run the launches:

### Mimic teleop (for test):
```bash
roslaunch imu_turtle mimic_teleop.launch
```

### Control with auto lemniscate:
```bash
roslaunch imu_turtle only_lemn.launch
```

### Control with smartphone:
```bash
roslaunch imu_turtle only_phone.launch
```

### Control with both:
```bash
roslaunch imu_turtle both_control.launch
```
