Import cv2
Import numpy As np

screen_size=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("dsdkosscreenrecordervideo.mp4,fourcc,20.0,(screen_size))

While True:
img=pyautogui.screenshot()
frame=np.array(img)
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
out.write(frame)
cv2.imshow("show",frame)
if cv2.waitKey(1)==ord("q") :
Break
