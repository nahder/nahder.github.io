---
title: "Object tracking with an event camera"
author_profile: true
excerpt: |
  • Event-based vision <br>
  • Hough transforms  <br>
  • Optimization
key: 4
header:
  teaser: /assets/EC.gif
---

In this project, the Prophesee EVK4, an event-based camera based on the IMX636ES HD sensor developed in collaboration between Sony and Prophesee, was used to create a proof of concept for a 3-D cube tracking system. Hough space shape detection was employed to track cube edges, and an optimization-based algorithm determined the cube pose. A ghosting effect was observed on the trailing event edges, and a sensor simulation model was developed to investigate this phenomenon.

## What are event cameras?
Event cameras are vision sensors that capture changes in light intensity at each pixel as they occur, instead of capturing frames at a fixed rate like traditional cameras. Each detected change, or "event," includes a timestamp, pixel location, and polarity, indicating whether the intensity increased or decreased. This asynchronous operation enables them to capture high-speed activity with sub-millisecond latency and minimal motion blur.

<div style="text-align: center; width: 70%; margin: 0 auto;">
    <img src="../assets/EC.gif" alt="Event Camera Example" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">Waving at the EVK4. Blue and white dots represent positive and negative events respectively (increases/decreases in intensity). When attempting to stay still, less events are generated. </i>
</div>


## Tracking a disc
The first step towards 3D object tracking involved tracking a 2D object, such as a coin, using recorded events from the EVK4. The Hough Circle Transform was applied to fit circles to the perimeter of the coin. An accumulator was used to represent possible circle centers and radii. Each event, lying on the disk's edge, cast votes for circles with various potential centers and radii that could pass through it. By aggregating these votes, the peaks in the accumulator space indicated the most likely circle parameters, and the circle with the highest number of votes was selected as the best estimate for the disk’s position.

<div style="text-align: center; width: 70%; margin: 0 auto;">
    <img src="../assets/images/fallingdisk.png" alt="2D Disk Tracking" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">Left: Hough circle detections (green) and their centroid (blue)
    Right: Events generated from coin falling in free space. Notably, the negative events (white) trail behind quite a bit. This ghosting effect prompted the development of a sensor model to gauge what was happening. </i>
</div>

## Creating a sensor model
A sensor model was developed to investigate the ghosting issues seen in the event camera footage. The datasheet for this sensor is proprietary, and SONY was unable to provide further information regarding it. However, some basic information could be gleaned from the promotional content on their event-based sensors. Namely, it was possible to obtain a high-level schematic of the analog system, displayed below, which demonstrates the process through which light rays are used to generate events.

<div style="text-align: center; width: 70%; margin: 0 auto; margin-top: 20px; margin-bottom:20px;">
    <img src="../assets/sensor_diagram.png" alt="Sensor Diagram" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">Abstract schematic of the IMX-636ES sensor at the pixel level. Taken from <a href="https://www.prophesee.ai/event-camera-evk4/">Prophesee</a></i>
</div>

One key thing to note about the schematic above is that the analog sensor takes time to
charge and discharge at the pixel level. This reality limits how quickly events can be generated
relative to changes in incident brightness. Although an ideal event camera has no motion blur,
this idealization breaks down in certain situations because of the sensor’s inevitable analog
limitations.
We suspected that this charging and discharging had an associated time constant similar
in nature to a first-order RC circuit. To replicate this effect, we passed incident light intensity
data through a first-order low-pass filter, which acted to smooth out the input signal in the time
domain. A first-order Butterworth filter was chosen to preserve the accuracy of the input given
its relatively flat passband. To test if the sensor’s analog limitations were responsible for the ghosting, the sensor model was made to be tested on synthetic light intensity data: a rectangle moving across the image space. The Butterworth filter was then applied to the intensity data, and the logarithm of the result was taken to get the voltage. Events were then fired probabilistically based on the difference between the reference and actual voltage. The results of the sensor model were promising:


<div style="text-align: center; width: 80%; margin: 0 auto;">
    <img src="../assets/simulated_events.gif" alt="Sensor Model" style="width: 100%; height: auto;">
</div>


<!-- <!-- <div style="text-align: center; width: 70%; margin: 0 auto;">
    <img src="../assets/cube_events.gif" alt="Rubiks cube" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">temp1 </i>
</div> -->
 



## Hough line detector
<!-- overlay rubix cube over gif -->

## Optimization and Cube Tracking
