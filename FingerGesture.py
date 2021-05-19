import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=2,
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
                ## finger statement
                # thumb = False
                # flippedThumb = False
                # index = False
                # flippedindex = False
                # middle = False
                # flippedmiddle = False
                # ring = False
                # flippedring = False
                # pinky = False
                # flippedpinky = False

                # Thumb Finger
                if (hand_landmarks.landmark[8].x < hand_landmarks.landmark[6].x and hand_landmarks.landmark[7].x < hand_landmarks.landmark[6].x
                    and hand_landmarks.landmark[12].x < hand_landmarks.landmark[10].x and hand_landmarks.landmark[11].x < hand_landmarks.landmark[10].x
                    and hand_landmarks.landmark[16].x < hand_landmarks.landmark[14].x and hand_landmarks.landmark[15].x < hand_landmarks.landmark[14].x
                    and hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y and hand_landmarks.landmark[17].y > hand_landmarks.landmark[0].y):
                    cv2.putText(
                        image, text='Everglow', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                if (hand_landmarks.landmark[4].x < hand_landmarks.landmark[2].x and hand_landmarks.landmark[3].x < hand_landmarks.landmark[2].x
                    and hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y and hand_landmarks.landmark[7].y > hand_landmarks.landmark[6].y
                    and hand_landmarks.landmark[5].y > hand_landmarks.landmark[0].y):
                    cv2.putText(
                        image, text='NCT', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                if (hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y and hand_landmarks.landmark[19].y < hand_landmarks.landmark[18].y
                    and hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y and hand_landmarks.landmark[15].y < hand_landmarks.landmark[14].y
                    and hand_landmarks.landmark[17].y < hand_landmarks.landmark[0].y):
                    cv2.putText(
                        image, text='MadMonster', org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=255, thickness=2)

                
                # # Thumb Finger
                # if (hand_landmarks.landmark[3].x < hand_landmarks.landmark[2].x and hand_landmarks.landmark[4].x < hand_landmarks.landmark[2].x
                #     and hand_landmarks.landmark[2].x < hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[5].y):
                #     thumb = True

                # if (hand_landmarks.landmark[3].x > hand_landmarks.landmark[2].x and hand_landmarks.landmark[4].x > hand_landmarks.landmark[2].x
                #     and hand_landmarks.landmark[2].x > hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[5].y):
                #     flippedThumb = True

                # # Index Finger
                # if (hand_landmarks.landmark[7].y < hand_landmarks.landmark[6].y and hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
                #     and hand_landmarks.landmark[2].x < hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[5].y):
                #     index = True

                # if (hand_landmarks.landmark[7].y < hand_landmarks.landmark[6].y and hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
                #     and hand_landmarks.landmark[2].x > hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[5].y):
                #     flippedIndex = True

                # # Middle Finger
                # if (hand_landmarks.landmark[11].y < hand_landmarks.landmark[10].y and hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
                #     and hand_landmarks.landmark[2].x < hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[9].y):
                #     middle = True

                # if (hand_landmarks.landmark[11].y < hand_landmarks.landmark[10].y and hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
                #     and hand_landmarks.landmark[2].x > hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[9].y):
                #     flippedMiddle = True

                # # Ring Finger
                # if (hand_landmarks.landmark[15].y < hand_landmarks.landmark[14].y and hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
                #     and hand_landmarks.landmark[2].x < hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[13].y):
                #     ring = True

                # if (hand_landmarks.landmark[15].y < hand_landmarks.landmark[14].y and hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
                #     and hand_landmarks.landmark[2].x > hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[13].y):
                #     flippedRing = True

                # # Pinky Finger
                # if (hand_landmarks.landmark[19].y < hand_landmarks.landmark[18].y and hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y
                #     and hand_landmarks.landmark[2].x < hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[17].y):
                #     pinky = True

                # if (hand_landmarks.landmark[19].y < hand_landmarks.landmark[18].y and hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y
                #     and hand_landmarks.landmark[2].x > hand_landmarks.landmark[17].x
                #     and hand_landmarks.landmark[0].y > hand_landmarks.landmark[17].y):
                #     flippedPinky = True

                # # Normal
                # if (thumb and index and middle and ring and pinky):
                #     cv2.putText(
                #         image, text='Five', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not thumb and index and middle and ring and pinky):
                #     cv2.putText(
                #         image, text='Four', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not thumb and index and middle and ring and not pinky):
                #     cv2.putText(
                #         image, text='Three', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not thumb and index and middle and not ring and not pinky):
                #     cv2.putText(
                #         image, text='Two', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not thumb and index and not middle and not ring and not pinky):
                #     cv2.putText(
                #         image, text='One', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # # Flipped
                # if (flippedThumb and flippedIndex and flippedMiddle and flippedRing and flippedPinky
                #     and not thumb and not index and not middle and not ring and not pinky):
                #     cv2.putText(
                #         image, text='Flipped Five', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not flippedThumb and flippedIndex and flippedMiddle and flippedRing and flippedPinky
                #     and not thumb and not index and not middle and not ring and not pinky):
                #     cv2.putText(
                #         image, text='Flipped Four', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not flippedThumb and flippedIndex and flippedMiddle and flippedRing and not flippedPinky
                #     and not thumb and not index and not middle and not ring and not pinky):
                #     cv2.putText(
                #         image, text='Flipped Three', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not flippedThumb and flippedIndex and flippedMiddle and not flippedRing and not flippedPinky):
                #     cv2.putText(
                #         image, text='Flipped Two', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)

                # if (not flippedThumb and flippedIndex and not flippedMiddle and not flippedRing and not flippedPinky):
                #     cv2.putText(
                #         image, text='Flipped One', org=(10, 30),
                #         fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                #         color=255, thickness=2)


                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('image', image)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()