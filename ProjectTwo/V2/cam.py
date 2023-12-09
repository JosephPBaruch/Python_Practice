import cv2
from ultralytics import YOLO
import ultralytics
ultralytics.checks()
import os
import PIL
from PIL import Image
# import albumentations as A
os. chdir('/Users/joseph.baruch/REPO/Practical_Python/ProjectTwo/V2') 
# unzip data.zip

train_path = './data/train/Archie/'
test_path = './data/test/Archie/'
val_path = './data/val/Archie/'

train_path2 = './data/train/Grayson/'
test_path2 = './data/test/Grayson/'
val_path2 = './data/val/Grayson/'

train_path3 = './data/train/Joe/'
test_path3 = './data/test/Joe/'
val_path3 = './data/val/Joe/'

train_path4 = './data/train/Kaley/'
test_path4 = './data/test/Kaley/'
val_path4 = './data/val/Kaley/'

train_path5 = './data/train/Connor/'
test_path5 = './data/test/Connor/'
val_path5 = './data/val/Connor/'

path_lists = [train_path, test_path, val_path,
              train_path2, test_path2, val_path2,
              train_path3, test_path3, val_path3,
              train_path4, test_path4, val_path4,
              train_path5, test_path5, val_path5]

for path in path_lists:
    file_list = os.listdir(path)
    file_list = [file for file in file_list if '.jpeg' or '.JPG' or '.jpg' in file]
    for file in file_list:
        img = PIL.Image.open(path + file)
        img = img.resize((512, 512))
        img.save(path + file)

def predict(chosen_model, img, classes=[], conf=0.5):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf)
    else:
        results = chosen_model.predict(img, conf=conf)

    return results

def predict_and_detect(chosen_model, img, classes=[], conf=0.5):
    results = predict(chosen_model, img, classes, conf=conf)

    for result in results:
        for box in result.boxes:
            cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                          (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), 2)
            cv2.putText(img, f"{result.names[int(box.cls[0])]}",
                        (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
    return img, results
# yolov8n.pt
model = YOLO("yolov8n-cls.pt")
model.train(data='./data', epochs=200)
new_model = YOLO('./runs/classify/train/weights/best.pt')

cap = cv2.VideoCapture(0)

while True: 
	ret, frame = cap.read()
	if ret==True:
		result_img, _ = predict_and_detect(new_model, frame, classes=[], conf=0.5)
		cv2.imshow("YOLOv8 Detection", result_img)
        
		key=cv2.waitKey(1)
		if key==ord("q"):
			break
cap.release()
cv2.destroyAllWindows()


