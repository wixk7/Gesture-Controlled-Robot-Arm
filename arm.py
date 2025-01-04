import cv2
import mediapipe as mp
import serial  # For communication with Arduino
import time

# Set up serial communication (update COM port for your system)
arduino = serial.Serial('COM6', 9600)  # '/dev/ttyUSB0' for Linux, 'COMx' for Windows
time.sleep(2)  # Give time for the connection to establish

# Initialize MediaPipe hand tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Initialize video capture
cap = cv2.VideoCapture(0)

def map_value(value, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract the coordinates of the finger tips
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            pinky_tip = hand_landmarks.landmark[20]

            # Map the y-coordinates of the tips (finger position) to servo angles (0-180)
            thumb_angle = map_value(thumb_tip.y, 0, 1, 0, 180)
            index_angle = map_value(index_tip.y, 0, 1, 0, 180)
            middle_angle = map_value(middle_tip.y, 0, 1, 0, 180)
            ring_angle = map_value(ring_tip.y, 0, 1, 0, 180)
            pinky_angle = map_value(pinky_tip.y, 0, 1, 0, 180)

            # Send the servo angles to Arduino as a comma-separated string
            angles = f'{thumb_angle},{index_angle},{middle_angle},{ring_angle},{pinky_angle}\n'
            arduino.write(angles.encode())
            print(f'Sent angles: {angles}')

            # Draw hand landmarks for visualization
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

    # Show the webcam frame
    cv2.imshow('Hand Tracking', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()