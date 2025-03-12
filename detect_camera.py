import cv2
from ultralytics import YOLO
model = YOLO("D:/exam_cheating/runs/detect/train/weights/best.pt")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không thể mở camera. Kiểm tra lại thiết bị!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể đọc frame từ camera!")
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Cheating Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()