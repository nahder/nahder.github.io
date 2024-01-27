---
title: "BotROS: Painting with a Franka arm"
author_profile: true
excerpt: |
  ‣ ROS2, MoveIt <br>
  ‣ April tags <br>
  ‣ Pick and place <br>
key: 1
header:
  teaser: /assets/botROS4.gif
---

In this project, robotics meets art! A 7 DOF Franka Panda arm, "BotROS", was programmed to autonomously create pointilist-style artwork. 

BotROS is provided with a canvas, paint brushes, and a palette.
It will pick up a brush, dip it in a color, and will begin painting some dots! It will return for more paint every 8 dots. Once the first color is complete, it will return its brush and pick up a new one before initiating a second round of color.

## Video Demo
<iframe width="1920" height="1080" src="https://www.youtube.com/embed/Pt7TTiF4OoU?si=0yTIfrHiUnRS2hOc" title="BotROS: Franka Painter" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



## Project Components

### I. Motion Planning
A custom MoveIt wrapper [`frankastein`](https://github.com/ME495-EmbeddedSystems/final-project-Group5/blob/main/mattagascar/mattagascar/submodules/frankastein.py) was developed in Python for interfacing with the Franka. This API facilitated the planning and executing of robot trajectories by making requests to MoveIt's `GetPositionIK` and `GetCartesianPath` services.

<div align="center">
    <table style="border-collapse: separate; width: 70%; text-align: left; border-spacing: 0;">
        <tr>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40; border-top-left-radius: 10px;">API Function:</th>
            <th style="border: 0.75px solid gray; padding: 3.5px; background-color: #305b40; border-top-right-radius: 10px;">Input</th>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;"><code>plan_path_to_position</code></td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">goal position (x,y,z)</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;"><code>plan_path_to_orientation</code></td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">goal quaternion (x,y,z,w)</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px;"><code>plan_path_to_position_orientation</code></td>
            <td style="border: 0.75px solid gray; padding: 3.5px;">goal position(x,y,z) + quaternion (x,y,z,w)</td>
        </tr>
        <tr>
            <td style="border: 0.75px solid gray; padding: 3.5px; border-bottom-left-radius: 10px;"><code>plan_path_cartesian</code></td>
            <td style="border: 0.75px solid gray; padding: 3.5px; border-bottom-right-radius: 10px;">list of position (x,y,z) waypoints</td>
        </tr>
    </table>
</div>




### II. Computer Vision
April tags are used to locate the brushes and palette. The `listener` node establishes the transformation between the camera and robot and publishes the paint brush and palette locations. The `colordetection` node then color thresholds the image to determine the specific paint dip locations with respect to the robot frame. 

The `PictureTaking` package creates a service `take_picture` which performs the following operations:
- Snaps a picture from an Intel Realsense (images can also be supplied)
- Applies morphological operations (dilation + erosion) 
- Applies a Canny edge detector
- Discretizes the edge map into points
- Maps the points to the task space of the Franka end effector

| !["Swarthmore S"](/assets/images/S_canny.png) | 
|:--:| 
| *Swarthmore S points.* |

### III. Collage
Our team decided to make a collage representing all of our undergraduate institutions: 

<table>
    <tr>
        <td style="background-color: transparent;">
        <div align="center">
            <img src="/assets/images/collage.jpg" width="50%" height="50%" style="background-color: transparent;">
        </div>
        </td>
    </tr>
    <tr>
        <td style="background-color: transparent; text-align: center;">
            <i>College logos: Northwestern, Swarthmore, Notre Dame, Georgia Tech, Tennessee, and Maryland</i>
        </td>
    </tr>
</table>

Team: Nader Ahmed, Demiana Barsoum, Shail Dalal, Fiona Neylon, Courtney Smith

Check out the project &#8594; <a href="https://github.com/nahder/BotROS-Franka/tree/main" class="github-button">GitHub</a>
