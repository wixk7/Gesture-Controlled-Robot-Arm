# Gesture-Controlled Robot Arm

## Overview

This project showcases a gesture-controlled robotic arm that utilizes real-time hand tracking for intuitive control. Using MediaPipe for gesture recognition and an Arduino for servo motor manipulation, the system maps finger movements to precise servo angles, enabling seamless control of the robotic arm.

## Features

*   **Real-Time Hand Gesture Tracking**: Powered by MediaPipe and OpenCV.
*   **Servo Motor Control**: Maps finger gestures to servo movements.
*   **Plug-and-Play**: Simple setup with Python and Arduino code.
*   **Customizable**: Easily extendable for additional gestures and features.

## Demo

Watch the robot arm in action:

[View Demo Video](Assets/demo.mp4)

## Hardware Requirements

*   **Arduino Board** (e.g., Arduino Uno or Nano)
*   **Servo Motors** (5 recommended)
*   **USB Camera**
*   **Jumper Wires**
*   **Power Supply**

## Software Requirements

*   Python 3.7 or higher
*   Arduino IDE

### Python Libraries

Install the required libraries using pip:

pip install opencv-python mediapipe pyserial

## Wiring Diagram

Connect the servo motors to the appropriate PWM pins on the Arduino. Refer to the following table for connections:

| Servo       | Arduino Pin |
|-------------|-------------|
| Thumb       | D9          |
| Index       | D8          |
| Middle      | D7          |
| Ring        | D6          |
| Pinky       | D5         |


## Setup and Installation

### 1\. Clone the Repository

```bash
git clone https://github.com/wixk7/Gesture-Controlled-Robot-Arm.git
cd Gesture-Controlled-Robot-Arm
```

### 2\. Load the Arduino Code

1.  Open `gesture_ino.ino` in the Arduino IDE.
2.  Select the correct board and port from the **Tools** menu.
3.  Upload the code to your Arduino board.

### 3\. Run the Python Script

1.  Ensure your USB camera is connected.
2.  Update the `COM` port in `arm.py` to match your Arduino port.
3.  Run the script:

python arm.py

## Usage Instructions

1.  Position your hand in view of the camera.
2.  Move your fingers to control the corresponding servos on the robotic arm.
3.  Press `q` to exit the program.

## Project Structure

```bash
Gesture-Controlled-Robot-Arm/
├── assets/               # Images and demo videos
├── src/                  # Source code
│   ├── arm.py            # Python script for hand tracking and communication
│   └── gesture\_ino.ino   # Arduino code for servo control
├── README.md             # Project documentation
└── LICENSE               # License file (optional)
```

## How It Works

1.  **Hand Tracking**:

*   Uses MediaPipe to detect hand landmarks in real-time.
*   Extracts finger tip positions to determine gestures.

1.  **Mapping to Servo Angles**:

*   Converts y-coordinates of finger tips to servo angles (0–180 degrees).
*   Sends the angles to Arduino via serial communication.

1.  **Servo Control**:

*   Arduino receives the angles and moves the servos accordingly.

## Troubleshooting

*   **No Camera Feed**: Check that your webcam is properly connected.
*   **Serial Port Errors**: Verify the COM port in `arm.py` matches your system.
*   **Servo Not Responding**: Ensure proper wiring and power to the servos.

## Future Enhancements

*   Add support for additional gestures.
*   Implement 3D hand tracking for enhanced control.
*   Optimize servo movements for smoother transitions.

---
## Contribution

Feel free to submit issues and pull requests for enhancements or bug fixes. Contributions are welcome!
