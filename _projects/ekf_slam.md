---
title: "Extended Kalman Filter SLAM from scratch"
author_profile: true
excerpt: |
  • Differential Drive Kinematics<br>
  • Extended Kalman Filter (EKF) <br>
  • Simultaneous Localization and Mapping (SLAM) <br>

key: 5
header:
  teaser: /assets/slam1.gif

---
This project involved implementing Extended Kalman Filter (EKF) for Simultaneous Localization and Mapping (SLAM) on a TurtleBot3 using C++ with ROS2. 

## EKF SLAM Video Demo
  <!-- <i style="display: block; text-align: left; margin-bottom: 20px;">
        <span style="color: red; font-weight: bold;">Red robot:</span> Initial points projected using an initial guess for the pose. <br>
        <span style="color: blue; font-weight: bold;">Blue robot:</span> Points projected using the true 3D pose with a small amount of Gaussian noise added. <br>
        <span style="color: green; font-weight: bold;">Green robot:</span> Points projected using the optimized cube pose.
    </i> -->

As this was done from scratch, several packages were developed:

- `turtlelib`: Defines SE(2) transformation methods, forward and inverse kinematics for a differential drive robot, visualizes .svg files, and implements EKF SLAM.
- `nuturtle_description`: Visualizes multiple TurtleBot3 models of different colors in RViz.
- `nusim`: Initializes the simulation environment with walls and obstacles.
- `nuturtle_control`: Controls the TurtleBot3 and updates its internal odometry estimate, with integration testing included.
- `nuslam`: Applies EKF SLAM to estimate the robot's pose and maintain the current map of the environment.


## System Diagram

## Movement Demo
<iframe width="1920" height="1080" src="https://www.youtube.com/embed/A6Nuhwcevig?si=f-d0e8cCbUXAU8Zg" title="Turtlebot ROS2 Controller + Odometry Movement Demo " frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Check out the project &#8594; <a href="https://github.com/ME495-Navigation/slam-project-nahder" class="github-button" target="_blank">GitHub</a>
