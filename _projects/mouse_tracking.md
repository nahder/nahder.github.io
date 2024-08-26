---
title: "Motorized tracking and following a mouse"
author_profile: true
excerpt: |

key: 1
header:
  teaser: /assets/hi.gif
---

<!-- Introduction section about project -->
## Motivation
This project is in collaboration with the <a href="https://www.shepherdlab.net/" target="_blank">Shepherd Lab</a> at the Feinberg School of Medicine. The goal is to study the multi-motor and sensorimotor coordination in mice feeding behavior. Previous setups aimed at examining this held the mice stationary while recording feeding footage from below them. 

This new setup was developed in order to capture this camera footage while allowing the mice to roam freely. Two stepper motors are used along with a trained network (using DeepLabCut) to move and keep the camera under the mouse at all times.

<!-- Block diagram -->
<div align="center" style="margin-bottom: -0px;"> <!-- Adjust the px value as needed -->
    <img src="/assets/images/setup_img.jpg" alt="Physical setup" width="70%" />
</div>

## Video Demo
<!-- reference video link -->

## System Diagram

<!-- Block diagram -->
<div align="center"> 
    <img src="/assets/images/mouse_block_diag.svg" alt="Mouse tracking block diagram" width="120%" />
</div>

## Mechatronics
<!-- Circuit diagram -->
<div align="center" style="margin-bottom: 75px">
    <img src="/assets/images/colorkit.svg" alt="Circuit Diagram" width="100%" />
    <br>
</div>

Two Nema 23 bipolar stepper motors are mounted perpendicularly onto linear actuator belts for controlling the motion of the bottom camera. They are driven by two-phase DM542 microstepping drivers and powered by a 48V, 10A ACDC converter. 

For calibrating the stepper motor range, limit switches are placed at the ends of each belt. The motors move towards one switch per axis to zero out. After calibration, the system switches to a tracking state where it will move to given goal positions coming in over a serial port. This is done with open-loop controller configured with the <a href="https://www.airspayce.com/mikem/arduino/AccelStepper/" target="_blank">`AccelStepper`</a> library that can be interrupted when new goal positions are parsed.

As a safety mechanism, the signal from the normally open switches are attached to interrupt service routines. If an interrupt is generated in the tracking state, the motor rapidly accelerates in the other direction to prevent any collision. The system then begins calibrating again. The Arduino's internal pull-up resistors ensure that the normally open switches are in a high state (rather than floating). When the signal is pulled to low, interrupts are triggered. Capacitors are also connected in parallel with the switches to debounce and act as low pass filters.

The DM542 drivers have 8 toggleable bits to configure its RMS, peak, and standstill current as well as its level of microstepping. To assess performance with different levels of microstepping, a benchmarking tool was developed. A fiducial marker is attached to the load, enabling error metrics (the distance between the desired and current position) to be measured. Speeds and accelerations were maximized up until the motors started missing steps.
<div style="display: flex; justify-content: center; align-items: flex-start; gap: 20px;">
    <!-- Table -->
    <div style="flex: 1;">
        <table style="border-collapse: separate; width: 100%; text-align: left; border-spacing: 0;">
            <tr>
                <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40; border-top-left-radius: 10px;">Microstepping Resolution</th>
                <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40; border-top-right-radius: 10px;">Average Error (cm) with Moving Average Filter (window_size=3)</th>
            </tr>
            <tr>
                <td style="border: 0.75px solid gray; padding: 3.5px;">1/8</td>
                <td style="border: 0.75px solid gray; padding: 3.5px;">0.72</td>
            </tr>
            <tr>
                <td style="border: 0.75px solid gray; padding: 3.5px;">1/16</td>
                <td style="border: 0.75px solid gray; padding: 3.5px;">0.65</td>
            </tr>
            <tr>
                <td style="border: 0.75px solid gray; padding: 3.5px;">1/32</td>
                <td style="border: 0.75px solid gray; padding: 3.5px;">0.53</td>
            </tr>
            <tr>
                <td style="border: 0.75px solid gray; padding: 3.5px;">1/64</td>
                <td style="border: 0.75px solid gray; padding: 3.5px;">0.57</td>
            </tr>
            <tr>
                <td style="border: 0.75px solid gray; padding: 3.5px; border-bottom-left-radius: 10px;">1/128</td>
                <td style="border: 0.75px solid gray; padding: 3.5px; border-bottom-right-radius: 10px;">0.59</td>
            </tr>
        </table>
    </div>

    <!-- Image -->
    <div style="flex: 1;">
        <img src="/assets/images/microstepping_error.png" alt="1/32 microstepping error" width="100%" style="margin-bottom: 15px;" />
    </div>
</div>

<!-- Caption -->
<div style="text-align: center; margin-top: -10px;">
    <i>Left: Benchmarked average error for different microstepping settings. Right: Graph of error over time for 1/32 microstepping, chosen to be the best.</i>
</div>






<!-- graph of error -->



<!-- 
- nema23 bipolar stepper motors, etc...
- drivers, microstepping, dm542 microstep settings & power consumption can be configured with x,y,z pins...
- power supply, voltage & current requirements
- discuss previous setup, performance improvement?
- limit switches, RC filtering, reference GRBL, 
- interrupt service routine
- calibration routine, internal pull ups
- benchmarking 
- finger tracking? -->


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

## Future Work
<!-- - move out of prototyping by making a PCB -->

## Collaborators