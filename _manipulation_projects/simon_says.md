---
title: "Simon says with an Allegro hand (*In Progress!*)"
author_profile: true
excerpt: |
  • ROS2, MoveIt <br>
  • Gesture Recognition <br>

key: 8
header:
  teaser: /assets/allegro_initial.gif
  
---
The Allegro Hand is a robotic hand with four fingers and 16 degrees of freedom. In this project, it is used to play a challenging Simon Says game with a human player. The hand performs increasingly longer sequences of gestures that the player must mimic in the correct order. 

## Video Demo

<!-- TODO: update game video demo -->
<iframe width="1920" height="1080" src="https://www.youtube.com/embed/JjlHqf-6iAA?si=YEV3slOnF0c7TsMo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Disclaimer: The ring finger of the hand currently has a broken gearbox at its base joint. Once it is repaired the video will be re-filmed with some more interesting gestures!
## Project Components

### I. System Overview
<div align="center" style="margin-bottom: -120px;"> <!-- Adjust the px value as needed -->
    <img src="/assets/images/simon_block.svg" alt="Simon Says block diagram" width="90%" />
</div>

### II. Planning & Control

The MoveIt setup assistant was used to generate the `allegro_moveit_config` package. For generating collision-free point-to-point (PTP) trajectories, the PILZ Industrial Motion Planner was used. The planning is performed in `moveit_controller` within the `control_hand` package and then interfaces with `can_communicator`. 

In `can_communicator`, the BHand library generates desired torques using PD control to drive the error between the desired and current joint positions down. Since one of the fingers of the hand was not functioning, some joints were enforced to have zero torque. This was restructured from a [fork](https://github.com/simlabrobotics/allegro_hand_linux) from SimLab robotics and wrapped in `can_communicator` within the ROS2 package.

### III. Perception

The [MediaPipe Hand Landmarker](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) detects 21 hand-knuckle coordinates from a camera stream. A hand gesture classifier (re-trained with custom configurations) then computes the most probable right-hand gesture. This model and classifier were integrated into the `gesture_classifier` node with a publisher. Stability criterion were added to ignore spurious classifications.

### IV. Game




Check out the project &#8594; <a href="https://github.com/nahder/Allegro-ROS2" class="github-button" target="_blank">GitHub</a>



