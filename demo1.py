from ultralytics import YOLO
from PIL import Image


model = YOLO('/home/mamata/Desktop/data_pipeline/runs/detect/train/weights/best.pt')
#model=YOLO('/home/mamata/Desktop/data_pipeline/yolov8n.pt')

# Load the image
image_path = '/home/mamata/Desktop/data_pipeline/front/front_7.jpg'
image = Image.open(image_path)

# Initialize YOLOv5 model

#model = YOLO('yolov5s')  # You can use yolov5s, yolov5m, yolov5l, or yolov5x

# Run YOLOv5 object detection
results = model(image, conf=0.3)
print("++++++++++++++++++++++++++++++++++++++",type(results))
yolo_labels = [model.names[cls] for cls in results[0].boxes.cls.cpu().tolist()]

# Plot the detected objects
print("Results**********",results)
print(yolo_labels)

