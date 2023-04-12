import cv2

cameraVideo = cv2.VideoCapture(0)

fps = cameraVideo.get(cv2.CAP_PROP_FPS)

print(dir(cameraVideo))

print(cameraVideo.isOpened())
print(fps)

size = (int(cameraVideo.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cameraWrite = cv2.VideoWriter('resource/cameragrab.avi',
                              cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

print(size)

success = cameraVideo.grab()

print(success)

while success:
    success, frame = cameraVideo.retrieve()
    cv2.imshow("my_vid.png", frame)

cv2.waitKey()

