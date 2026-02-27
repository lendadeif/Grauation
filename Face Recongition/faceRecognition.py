import cv2
import matplotlib.pyplot as plt
from simple_facerec import SimpleFacerec

sfr=SimpleFacerec()
sfr.load_encoding_images(".\\Images\\Known_people")

CAP=cv2.VideoCapture(0)
while True:
    ret,frame=CAP.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(0,0),fx=0.75,fy=0.75)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    face_locations,face_names=sfr.detect_known_faces(rgb_frame)
    for (top,right,bottom,left),name in zip(face_locations,face_names):
        cv2.rectangle(frame,(left,top),(right,bottom),(255,255,0),2)
        cv2.putText(frame,str(name),(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0),2)


    cv2.imshow("Webcam",frame)
    key=cv2.waitKey(1)
    if key & 0xFF==ord("q"):
        break
CAP.release()
cv2.destroyAllWindows()
