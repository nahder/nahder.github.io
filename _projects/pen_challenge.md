---
title: "Pen stealing with an Interbotix PincherX"
author_profile: true
excerpt: |
  • Blob tracking <br>
  • Pick and place <br>
key: 5
header:
  teaser: /assets/pen.gif

---

This project was part of a hackathon for Northwestern University's MS in robotics program. The objective was straightforward: use an Intel Realsense and PincherX100 robot arm to locate a pen, pick it up, and release it off a table.

## Video Demo
<iframe width="1920" height="1080" src="https://www.youtube.com/embed/1cq_gBXmGJQ?si=fW__JE6o9GXtKAUv" title="Hackathon pen challenge" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## System Overview
<div align="center" style="margin-bottom: -100px; margin-top: -100px"> <!-- Adjust the px value as needed -->
    <img src="/assets/images/pen_challenge_block.svg" alt="Simon Says block diagram" width="90%" />
</div>

## Perception
The Intel RealSense camera simultaneously captures RGB images and a depth point cloud. Color masking is used in the HSV color space to isolate the pen from the background. This frame is aligned with the depth map to ensure spatial correspondence, providing the 3D location of the pen in the camera frame.

An initial calibration routine calculates the spatial offsets between the camera and robot coordinate frames. A kalman filter with a linear motion model is integrated to smoothen the live position updates.

## Action

The `modern_robotics` library is leveraged by the Interbotix SDK for both forward and inverse kinematics. The `FKinSpace` function calculates the robot arm's current end-effector pose by generating a transformation matrix using the robot's home configuration `M`, the screw axes `Slist`, and the current joint angles. This transformation matrix accurately represents the arm's spatial position within the robot frame.

Once the pen's position is accurately mapped in the robot frame, the `set_ee_pose_components` function from the Interbotix SDK is invoked to command the robot arm. This function calls `IKinSpace` to compute the necessary joint angles required to achieve the desired end-effector pose based on the target pen pose. 

Check out the project &#8594; <a href="https://github.com/nahder/pen_stealing" class="github-button" target="_blank" >GitHub</a>
