# Eye Blinking CAPTCHA (GUI Based)

This project is a GUI-based human verification system using eye blink detection.  
It uses a webcam and a live window instead of text or image puzzles.

## What this project does
The program opens the system camera.  
It asks the user to blink their eyes a random number of times.  
Blinking is tracked in real time on the screen.  
On success, a GUI popup confirms verification.

## How verification works
The camera captures live video frames.  
Frames are converted to grayscale.  
Eye detection is done using Haar Cascade.  
If eyes disappear for a few frames, it is treated as a blink.  
Blink count increases only after proper eye open-close cycles.

## Key logic in this code
Random blink requirement between 2 and 5.  
First few frames are ignored for camera stabilization.  
Blink detection avoids false positives.  
A timeout of 20 seconds is applied.  
ESC key allows manual exit.

## User experience
Live window shows blink count progress.  
Clear instruction is printed in console.  
Successful verification shows a popup message.  
Failure happens on timeout or exit.

## Tech used
Python  
OpenCV  
Tkinter for GUI popup  
Haar Cascade for eye detection  
Real-time video processing

## Current limitations
Works best in good lighting.  
Single-user detection only.  
Desktop webcam required.

## Future improvements
Better low-light handling  
Face alignment checks  
Mobile-friendly version  
Web or API version later

## Why this project matters
It shows computer vision basics.  
It replaces annoying CAPTCHAs.  
It proves human verification logic.  
Good showcase for CV and Python skills.

## Note
This project is built for learning and demonstration.  
It focuses on logic clarity and real-time behavior.  
