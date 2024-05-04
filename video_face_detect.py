import cv2
import sys

# Load the Haarcascade for face detection

faceCascade = cv2.CascadeClassifier('haar_face.xml')

# Set video source to the default webcam (index 0)
def capture_face():
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    count = 0  

    # for (x, y, w, h) in faces:
    #     face = frame[y:y+h, x:x+w]  # Extract the face region
    #     cv2.imwrite(f'face_{count}.jpg', face)  # Save the face image
    #     path = (f'face_{count}.jpg')
    #     count += 1
    # path = (f'face_{count}.jpg')
    for (x, y, w, h) in faces:
    # Increase the size of the frame around the face
        x_offset = 50  # Increase the x-coordinate by 50 pixels
        y_offset = 50  # Increase the y-coordinate by 50 pixels
        w_offset = 100  # Increase the width by 100 pixels
        h_offset = 100  # Increase the height by 100 pixels

    # Extract the larger face region
        face = frame[max(0, y-y_offset):min(frame.shape[0], y+h+y_offset),
                 max(0, x-x_offset):min(frame.shape[1], x+w+x_offset)]

    # Save the face image
        cv2.imwrite(f'face_{count}.jpg', face)
        path = (f'face_{count}.jpg')
        count += 1


    # Release the webcam and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
    print(f"this is the path variable: {path}")
    return path



