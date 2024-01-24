---
title: "BotROS: Painting with a Franka arm"
author_profile: true
excerpt: |
  ‣ MoveIt <br>
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
<iframe src="https://player.vimeo.com/video/905050367?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="1920" height="1080" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Franka Painter!"></iframe>

## Project Components

### Motion Planning
<!-- TODO: hyperlink frankastein API -->
A custom MoveIt wrapper `frankastein` was developed in Python for interfacing with the Franka. This API facilitated the planning and executing of robot trajectories by making requests to MoveIt's `GetPositionIK` and `GetCartesianPath` services.

<div align="center">
    <table style="border-collapse: collapse; width: 70%;">
        <tr>
            <th style="border: 0.75px solid white; padding: 3.5px;">API Function:</th>
            <th style="border: 0.75px solid white; padding: 3.5px;">Input</th>
        </tr>
        <tr>
            <td style="border: 0.75px dashed white; padding: 3.5px;"><code>plan_path_to_position</code></td>
            <td style="border: 0.75px dashed white; padding: 3.5px;">goal position (x,y,z)</td>
        </tr>
        <tr>
            <td style="border: 0.75px dashed white; padding: 3.5px;"><code>plan_path_to_orientation</code></td>
            <td style="border: 0.75px dashed white; padding: 3.5px;">goal quaternion (x,y,z,w)</td>
        </tr>
        <tr>
            <td style="border: 0.75px dashed white; padding: 3.5px;"><code>plan_path_to_position_orientation</code></td>
            <td style="border: 0.75px dashed white; padding: 3.5px;">goal position(x,y,z) + quaternion (x,y,z,w)</td>
        </tr>
        <tr>
            <td style="border: 0.75px dashed white; padding: 3.5px;"><code>plan_path_cartesian</code></td>
            <td style="border: 0.75px dashed white; padding: 3.5px;">list of position (x,y,z) waypoints</td>
        </tr>
    </table>
</div>

### Computer Vision
1. April Tags
2. Color Detection
3. Point Generation

## Collage





