import cv2

videoCapture = cv2.VideoCapture('resource/exp-video.mkv')
fps = videoCapture.get(cv2.CAP_PROP_FPS)

print(fps)

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(size)

frame_count = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)

print("video len:", frame_count/fps)

videoWriter = cv2.VideoWriter('resource/MyOutPut.flv', cv2.VideoWriter_fourcc('F','L','V','1'), fps, size)

success, frame = videoCapture.read()
print("wait....")
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()

print("Done!")



