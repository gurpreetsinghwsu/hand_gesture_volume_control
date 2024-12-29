Hand Gesture Volume Control for macOS

This Python program allows you to control the system volume on macOS using hand gestures detected through your webcam. It utilizes Mediapipe for hand tracking and the osascript command to adjust the system volume.

Features
	•	Volume Control with Hand Gestures:
	•	1 Finger Raised: Increases the system volume.
	•	2 Fingers Raised: Decreases the system volume.
	•	Real-time hand tracking and feedback using your webcam.

 Setup and Installation

Prerequisites
	•	Operating System: macOS (required for the volume control functionality).
	•	Python Version: 3.7 or higher.
	•	Dependencies:
	•	OpenCV
	•	Mediapipe


Installation
	1.	Clone the Repository:
 git clone https://github.com/gurpreetsinghwsu/hand_gesture_volume_control.git
cd hand_gesture_volume_control

2.	Install the Required Libraries:
pip install opencv-python mediapipe

Run the Program:
python volume_control.py

How to Use
	1.	Start the Program:
	•	Connect your webcam and run the script.
	2.	Control Volume Using Gestures:
	•	Raise 1 Finger: Increases the system volume by 10%.
	•	Raise 2 Fingers: Decreases the system volume by 10%.
	3.	Exit the Program:
	•	Press the q key to quit.

How It Works
	1.	Hand Tracking with Mediapipe:
	•	Detects hand landmarks in real time and identifies finger positions.
	2.	Finger Counting Logic:
	•	Recognizes the number of raised fingers based on the position of their tips relative to their joints.
	3.	System Volume Adjustment:
	•	Uses the macOS osascript command to modify the system volume:
	•	Increase Volume: Adds 10% to the current volume.
	•	Decrease Volume: Subtracts 10% from the current volume.
