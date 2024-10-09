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
    <img src="/assets/EC.gif" alt="Event Camera Example" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">Waving at the EVK4. White and blue dots represent positive and negative events respectively (increases/decreases in intensity). When attempting to stay still, less events are generated. </i>
</div>


## Tracking a disc
The first step towards 3D object tracking involved tracking a 2D object, such as a coin using recorded events from the EVK4. 


<div style="text-align: center; width: 70%; margin: 0 auto;">
    <img src="/assets/images/disk_events.png" alt="2D Disk Tracking" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">temp1 </i>
</div>

<div style="text-align: center; width: 70%; margin: 0 auto;">
    <img src="/assets/images/disk_tracking_plot.png" alt="2D Disk Tracking" style="width: 100%; height: auto;">
    <i style="display: block; text-align: left;">temp1 </i>
</div>

## Creating a sensor model


## Hough line detector
<!-- overlay rubix cube over gif -->

## Optimization and Cube Tracking
