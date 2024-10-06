---
title: "Pen stealing with an Interbotix PincherX"
author_profile: true
excerpt: |
  • Blob tracking <br>
  • Pick and place <br>
key: 4
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


Check out the project &#8594; <a href="https://github.com/nahder/pen_stealing" class="github-button" target="_blank" >GitHub</a>
