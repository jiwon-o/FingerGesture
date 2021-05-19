import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # finger statement
                thumb = False
                index = False
                middle = False
                ring = False
                pinky = False

                pseudoFixKeyPoint = hand_landmarks.landmark[2].x
                if (hand_landmarks.landmark[3].x < pseudoFixKeyPoint and hand_landmarks.landmark[4].x < pseudoFixKeyPoint):
                    thumb = True

                pseudoFixKeyPoint = hand_landmarks.landmark[6].y
                if (hand_landmarks.landmark[7].y < pseudoFixKeyPoint and hand_landmarks.landmark[8].y < pseudoFixKeyPoint):
                    index = True

                pseudoFixKeyPoint = hand_landmarks.landmark[10].y
                if (hand_landmarks.landmark[11].y < pseudoFixKeyPoint and hand_landmarks.landmark[12].y < pseudoFixKeyPoint):
                    middle = True

                pseudoFixKeyPoint = hand_landmarks.landmark[14].y
                if (hand_landmarks.landmark[15].y < pseudoFixKeyPoint and hand_landmarks.landmark[16].y < pseudoFixKeyPoint):
                    ring = True

                pseudoFixKeyPoint = hand_landmarks.landmark[18].y
                if (hand_landmarks.landmark[19].y < pseudoFixKeyPoint and hand_landmarks.landmark[20].y < pseudoFixKeyPoint):
                    pinky = True

                if (thumb and index and middle and ring and pinky):
                    cv2.putText(
                        image, text='Five', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                if (not thumb and index and middle and ring and pinky):
                    cv2.putText(
                        image, text='Four', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                if (not thumb and index and middle and ring and not pinky):
                    cv2.putText(
                        image, text='Three', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                if (not thumb and index and middle and not ring and not pinky):
                    cv2.putText(
                        image, text='Two', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                if (not thumb and index and not middle and not ring and not pinky):
                    cv2.putText(
                        image, text='One', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('image', image)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()