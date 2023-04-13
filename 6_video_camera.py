# Opening camera device and save a video for
# 10 seconds.
#

import cv2

cameraCapture = cv2.VideoCapture(0)
fps = cameraCapture.get(cv2.CAP_PROP_FPS)
print(fps)

size = ( int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
         int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(size)

videoWriter = cv2.VideoWriter("resource/cameraOutput.avi",
                              cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

success, frame = cameraCapture.read()

numFrameRemaining = 10*fps -1 

print("wait...")
while success and numFrameRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFrameRemaining -= 1

print("Done!")
cameraCapture.release()
