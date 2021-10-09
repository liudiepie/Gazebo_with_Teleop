# Gazebo_with_Teleop
This is a project of ENPM662.   
The main purpose is to practice how to design the car model on SolidWorks and spawn the model in Gazebo.  
Utilizing ROS frame, the car model can control the joints with Teleop.  
Here are the display videos:  
[Gazebo with Teleop, own car and laser model](https://www.youtube.com/watch?v=5N5hD4imLy4)  
[Gazebo with Publisher and Subscriber](https://www.youtube.com/watch?v=G4sIyFC-L4w)  
## To run the Package:
  * First (source the file):  
    Type
    ```bash 
    source /devel/setup.bash
    ``` 
    under the terminal with the Package path.
	  Or type 
    ```bash
    gedit ~/.bashrc
    ```
    and add the setup.bash path under the buttom.
  * Second (Run Gazebo):  
    Open a terminal and type
    ```bash 
    roslaunch car_gazebo car_world.launch
    ```
    The world map and the car would display in gazebo.
  * Third (Run Teleop):  
    Open another terminal and type 
    ```bash
    roscd car_control
    ```
    It should appear the path to the package car_control.
    Then type 
    ```bash
    python3 teleop_template.py
    ```
    , the car could be controlled with 
    {u i o j k l m , .}
## To run the Publisher and the Subscriber:
  * First (Run Gazebo):  
    Open a terminal and type 
    ```bash
    roslaunch car_gazebo car_world.launch
    ```
    (make sure the file have been source)
  * Second (Run Publisher):  
    Open another terminal and type
    ```sh
    roscd car_control
    ```
    It should appear the path to the package car_control.
    Then type 
    ```bash
    python3 publisher.py
    ```
    The car would start to move and the terminal will show the command.
  * Third (Run Subscriber):  
    Open another terminal and type 
    ```bash
    roscd car_control
    ```
    It should appear the path to the package car_control.
    Then type 
    ```bash
    python3 subscriber.py
    ```
    The terminal would show the command from the topic which the publisher sends to the topic.
