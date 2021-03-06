import cv2
import argparse
import datetime
import time
import os

from report import report

import gtts
import playsound



from detect import detect

start = gtts.gTTS("pres escape to exit",lang="en")
start.save("start.mp3")
playsound.playsound("start.mp3")
os.remove("start.mp3")

cam = cv2.VideoCapture(0)




f = open("before.txt","w")
f.close()



parser = argparse.ArgumentParser()
parser.add_argument('--weights', nargs='+', type=str, default='yolov3.pt', help='model.pt path(s)')
parser.add_argument('--source', type=str, default='data/images', help='source')  # file/folder, 0 for webcam
parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
parser.add_argument('--max-det', type=int, default=1000, help='maximum number of detections per image')
parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--view-img', action='store_true', help='display results')
parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true', help='augmented inference')
parser.add_argument('--update', action='store_true', help='update all models')
parser.add_argument('--project', default='runs/detect', help='save results to project/name')
parser.add_argument('--name', default='exp', help='save results to project/name')
parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
opt = parser.parse_args()



currtime = datetime.datetime.now()


while True:
    cv2.namedWindow("test")
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)


    
    if((datetime.datetime.now()-currtime).seconds >= 30):
        currtime = datetime.datetime.now()
        img_name = "data\\images\\opencv_frame.png"
        cv2.imwrite(img_name, frame)

        print("{} written!".format(img_name))
        cv2.destroyAllWindows()
        detect(opt=opt)
        s = report()

        if(s):
            dosya = "ses.mp3"
            a = gtts.gTTS(s,lang="en")
            a.save(dosya)
            playsound.playsound("ses.mp3")
            os.remove("ses.mp3")


    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        esc = gtts.gTTS("Escape pressed. Closing.",lang="en")
        esc.save("esc.mp3")
        playsound.playsound("esc.mp3")
        os.remove("esc.mp3")
        break
  


cam.release()

cv2.destroyAllWindows()