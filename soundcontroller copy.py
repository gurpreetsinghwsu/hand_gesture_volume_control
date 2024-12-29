import cv2
import mediapipe as mp
import os

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)


# Function to count raised fingers
def count_fingers(landmarks):
    # Tip landmarks for each finger
    finger_tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb: Check if it's raised
    if landmarks[finger_tips[0]].x < landmarks[finger_tips[0] - 2].x:  # Thumb moves left (for right hand)
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers: Check if their tips are above the second joint
    for tip in finger_tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:  # Tip is above the PIP joint
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)  # Total number of raised fingers


# Function to set volume on macOS
def set_volume_mac(increase=True):
    if increase:
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
    else:
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")


# Start capturing from the webcam
cap = cv2.VideoCapture(1)  # Use camera 0 (adjust if needed)

print("Use gestures to control volume:")
print("1. Show 1 finger - Increase volume")
print("2. Show 2 fingers - Decrease volume")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame for a mirrored effect
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get normalized landmark positions
            landmarks = hand_landmarks.landmark

            # Count raised fingers
            raised_fingers = count_fingers(landmarks)

            if raised_fingers == 1:
                # Increase volume
                set_volume_mac(increase=True)
                print("Volume increased")
            elif raised_fingers == 2:
                # Decrease volume
                set_volume_mac(increase=False)
                print("Volume decreased")

    # Show the frame
    cv2.imshow("Hand Gesture Control for Volume", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()