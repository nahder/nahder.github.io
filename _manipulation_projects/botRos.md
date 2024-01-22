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
A custom MoveIt API was developed in Python for interfacing with the Panda arm. This API facilitated the planning and executing of the following robot trajectories:

<div align="center">
    <table style="border-collapse: collapse; width: 50%;">
        <tr>
            <th style="border: 1px solid white; padding: 10px;">Path Planning:</th>
            <th style="border: 1px solid white; padding: 10px;">Description</th>
        </tr>
        <tr>
            <td style="border: 1px solid white; padding: 10px;">Position</td>
            <td style="border: 1px solid white; padding: 10px;">[Description of the path to Target 1]</td>
        </tr>
        <tr>
            <td style="border: 1px solid white; padding: 10px;">Orientation</td>
            <td style="border: 1px solid white; padding: 10px;">[Description of the path to Target 2]</td>
        </tr>
        <tr>
            <td style="border: 1px solid white; padding: 10px;">Position + Orientation</td>
            <td style="border: 1px solid white; padding: 10px;">[Description of the path to Target 2]</td>
        </tr>
        <tr>
            <td style="border: 1px solid white; padding: 10px;">Cartesian</td>
            <td style="border: 1px solid white; padding: 10px;">[Description of the path to Target 3]</td>
        </tr>
    </table>
</div>

### Computer Vision
-April Tags
-Color Detection
-Point Generation

## Collage





