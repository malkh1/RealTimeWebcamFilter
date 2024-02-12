import cv2

cap = cv2.VideoCapture(0) # 0 for default webcam

if not cap.isOpened():
    print("Error: unable to access the webcam. exiting")
    exit()

while True: 
   #frame capture 
    ret, frame = cap.read()

    #if frame was not captured successfully, break
    if not ret:
        print("Error: unable to capture frame.")
        break
    
    # Display the captured frame
    cv2.imshow("Webcam", frame) 
   
   #check for a q press to break loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
