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

<iframe width="1920" height="1080" src="https://youtu.be/0_qbWtACnMs" title="Motorized mouse tracker" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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
<div style="text-align: left; margin-top: -10px;">
    <i>Left: Benchmarked average error for different microstepping settings. Right: Graph of error over time for 1/32 microstepping, chosen to be the best.</i>
</div>


## Computer Vision 
The previous iteration of this project had corners of the mouse workspace as tracked features; this was deemed unnecessarily taxing on the inference speed of the live model. To replace it, a corner detector using OpenCV was added. The steps can be summarized as follows:

<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 20px;">
    <!-- Numbered Bullets -->
    <div style="flex: 1;">
        <ol>
            <li>Image capture</li>
            <li>Contrast and brightness adjustment</li>
            <li>Median blurring</li>
            <li>Adaptive thresholding</li>
            <li>Morphological operations (dilation followed by erosion)</li>
            <li>Contour detection</li>
            <li>Polygon approximation on the largest contour</li>
        </ol>
    </div>

    <!-- Image -->
    <div style="flex: 1;">
        <img src="/assets/images/corners.png" alt="Corner Detection" width="100%" />
    </div>
</div>
<div style="text-align: left; margin-top: -10px;">
  <i>The hyperparameters involved in this detection are put on trackbars for adjustability in different lighting conditions. In the case where the low lighting proves accurate detections to be difficult, a manual corner clicker is also available.</i>
</div>

<div style="padding: 15px;"></div>

The detected corners are then used to estimate the homography between the camera image plane and cage plane. This is used for perspective correction, since it is known that the corners should form a non-slanted square:

<div align="center"> 
    <img src="/assets/images/homography.png" alt="Homography for perspective correction" width="70%" />
</div>



## Deep Learning
All models used for mouse feature prediction were trained using <a href="http://www.mackenziemathislab.org/deeplabcut" target="_blank">DeepLabCut</a>.. Since this is a live setup, achieving high inference speed was crucial. To optimize performance, different pre-trained network architectures were tested for the purposes of tracking the ears of mice. 

The previous setup used a Jetson Nano with a 128-core Maxwell architecture. This was able to achieve an inference speed of ~16 fps at best. The benchmarking done below shows that this was a significant bottleneck, as the inference speed could increase by 8x with the higher end GPUs. This would also suggest that obtaining a camera with a higher framerate would enable faster tracking. 

<div align="center">
    <table style="border-collapse: separate; width: 100%; text-align: left; border-spacing: 0.5;">
        <!-- First Row: Main Headers -->
        <tr>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40; border-top-left-radius: 10px;">Model</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40;">Engine</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40;"># Params</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40;">Training loss (last iter)</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40;">Testing RMSE (pixels)</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40;">Inference Speed (FPS) RTX 4060</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40; border-top-right-radius: 10px;">Inference Speed (FPS) RTX 6000</th>
        </tr>

        <!-- Data Rows with GPU Performance -->
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">mobilenet_v2_1.0</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">2,327,207</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0018</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">2.05</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">125.44</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">332.29</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">mobilenet_v2_0.75</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">1,451,287</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0019</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">2.16</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">154.30</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">334.08</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">mobilenet_v2_0.50</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">775,447</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0022</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">2.48</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">182.60</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">324.2</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">mobilenet_v2_0.35</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">479,431</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0024</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">3.04</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">192.11</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">327.71</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">efficientnet-b0</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">3,652,310</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0018</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">1.99</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">138.75</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">283.48</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px; border-bottom-left-radius: 10px;">efficientnet-b3</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">10,208,531</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0024</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">2.05</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">86.86</td>
            <td style="border: 0.75px solid gray; padding: 3.5px; border-bottom-right-radius: 10px;">243.18</td>
        </tr>

        <!-- Data Rows without GPU Performance (N/A) -->
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">resnet_50</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">PyTorch</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">23,618,630</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.00009</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">1.5</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">resnet_50</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">23,672,033</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0016</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">2.11</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">resnet_101</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">TensorFlow</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">42,716,385</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0015</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">1.91</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;">mobilenet_v2_1.0</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">PyTorch</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">1,401,903</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">0.0011</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">1.9</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">N/A</td>
        </tr>
    </table>
</div>

## Collaborators
Thanks to Matt Elwin, Mang Gao, John Barrett, Gordon Shepherd, for guidance and collaboration.

Check out the project &#8594; <a href="https://github.com/nahder/mouse-tracker" class="github-button" target="_blank">GitHub</a>
