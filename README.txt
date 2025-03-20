1. Chuẩn bị môi trường
Cài đặt Python: Đảm bảo bạn đã cài Python
Cài đặt Ultralytics: YOLOv8 được cung cấp qua thư viện ultralytics. 
Cài đặt bằng lệnh:
pip install ultralytics
opencv-python
2. Chuẩn bị dữ liệu
a. Tạo dataset
Thu thập ảnh: Chuẩn bị các hình ảnh chứa đối tượng bạn muốn phát hiện.
Gán nhãn (Labeling): Sử dụng công cụ như LabelImg, Roboflow
b. Cấu trúc thư mục
3. Tải mô hình YOLOv8 và huấn luyện
Ultralytics cung cấp các mô hình YOLOv8 pre-trained (nano, small, medium, large, extra-large)
YOLOv8n (nano): Nhẹ nhất, nhanh nhưng độ chính xác thấp.
YOLOv8x (extra-large): Nặng nhất, chính xác nhất.
