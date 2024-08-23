---
title: "Motorized tracking and following a mouse"
author_profile: true
excerpt: |

key: 1
header:
  teaser: /assets/hi.gif
---

<!-- Introduction section about project -->

## Video Demo
<!-- reference video link -->

## System Overview

<!-- Block diagram -->

## Mechatronics

<!-- Circuit diagram -->
<div align="center">
    <img src="/assets/images/colorkit.svg" alt="Circuit Diagram" width="100%" />
    <br>
</div>

<!-- 
- nema23 bipolar stepper motors, etc...
- drivers, microstepping, dm542 microstep settings & power consumption can be configured with x,y,z pins...
- power supply, voltage & current requirements
- discuss previous setup, performance improvement?
- limit switches, RC filtering, reference GRBL, 
- interrupt service routine
- calibration routine, internal pull ups
- benchmarking -->

## Computer Vision 
<!-- 
- homography
- mrcal calibration to correct for distortion
- corner detection  -->

## Deep Learning
<!-- 
- intro about deeplabcut
- deeplabcut creates X model, that can be exported to Y, that can be used for live processing
- goal to increase inference speed as much as possible for live mouse following

- model benchmarking (add my computer performance, machine specs. )
- processing: option for kalman filter and moving average filter
- processing module written for realsense, and mouse simulation performed by feeding in frames to DLC live 


-performance graph with moving average filter + extreme outliers removed  -->