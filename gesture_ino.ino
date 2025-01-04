#include <Servo.h>

// Create servo objects for each finger
Servo thumbServo;
Servo indexServo;
Servo middleServo;
Servo ringServo;
Servo pinkyServo;

void setup() {
  // Attach each servo to a pin
  thumbServo.attach(9);   // Thumb connected to pin 9
  indexServo.attach(8);   // Index connected to pin 8
  middleServo.attach(7);  // Middle connected to pin 7
  ringServo.attach(6);    // Ring connected to pin 6
  pinkyServo.attach(5);   // Pinky connected to pin 5

  // Begin serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if data is available
  if (Serial.available() > 0) {
    // Read the incoming string of angles
    String data = Serial.readStringUntil('\n');

    // Parse the angles from the string
    int thumbAngle = data.substring(0, data.indexOf(',')).toInt();
    data = data.substring(data.indexOf(',') + 1);
    int indexAngle = data.substring(0, data.indexOf(',')).toInt();
    data = data.substring(data.indexOf(',') + 1);
    int middleAngle = data.substring(0, data.indexOf(',')).toInt();
    data = data.substring(data.indexOf(',') + 1);
    int ringAngle = data.substring(0, data.indexOf(',')).toInt();
    data = data.substring(data.indexOf(',') + 1);
    int pinkyAngle = data.toInt();

    // Move the servos to the corresponding angles
    thumbServo.write(thumbAngle);
    indexServo.write(indexAngle);
    middleServo.write(middleAngle);
    ringServo.write(ringAngle);
    pinkyServo.write(pinkyAngle);
  }
}