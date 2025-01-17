import cv2

# Create a VideoCapture object and read the video
# Its argument can be either the device index or the name of a video file.
# Device index is just the number to specify which camera.
cap = cv2.VideoCapture("./images/sample_video.avi")

# Check if video opened sucessfully
if not cap.isOpened():
    print("Open video file error!")

# Get the frame property
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("The frame width: {}, height: {}".format(width, height))

# Save the video after some specific processing
# https://www.zhihu.com/question/49558804
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./images/output.avi', fourcc, 20.0, (width, height))

frame_num = 0
while True:
    # Capture frame by frame
    frame_num += 1
    ret, frame = cap.read()

    if not ret:
        print("Can't recieve frame. Exiting...")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", frame_gray)
    # Write the video
    out.write(frame_gray)

    # Save each frame during processing
    # cv2.imwrite("./images/{}.png".format(frame_num), frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
