import os
import yaml
from coco_names import coco_names
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import json_function

def label_images():
    # Initialize YOLOv8 model
    model = YOLO('yolov8n.pt')

    # Initialize Faster R-CNN model
    faster_rcnn_model = fasterrcnn_resnet50_fpn(pretrained=True)
    faster_rcnn_model.eval()

    # Set local folder paths
    raw_images_folder = './front/'
    train_folder = './train/'  # Add train folder path
    val_folder = './val/'      # Add val folder path

    # Function to get file paths from local folder
    def get_file_paths(folder):
        file_paths = []

        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path):
                file_paths.append(file_path)

        return file_paths

    # Get file paths from raw_images folder
    raw_image_paths = get_file_paths(raw_images_folder)
    
    # Images Imported    #datapipeline
    data=json_function.read_json()    
    data['Image_imported'] = "True"
    data['cloud_status'] ="Images Imported"  
    json_function.write_json(data)

    # Initialize data dictionary
    data_dict = {'train': '/home/saiteja/dell_data_pipeline/train', 'val': '/home/saiteja/dell_data_pipeline/val/', 'nc': 0, 'names': {}}

    label_count = 0

    # Calculate the number of images for the train and val folders
    num_train_images = int(len(raw_image_paths) * 0.7)
    num_val_images = len(raw_image_paths) - num_train_images

    # Transformation to apply to the image before passing it to the Faster R-CNN model
    transform = T.Compose([T.ToTensor()])
    
    ### Labeling_Started          #datapipeline
    data=json_function.read_json()    
    data['Labelling_started'] = "True"
    data["cloud_status"] = "Labeling Started"
    json_function.write_json(data)
    
    for i, image_path in enumerate(raw_image_paths):
        # Detect objects and labels using YOLOv8
        yolo_results = model(image_path)  # Updated to use local image path
        yolo_labels = [model.names[cls] for cls in yolo_results[0].boxes.cls.cpu().tolist()]
     
        print("Yolo_outputs:", yolo_results)
        print("Yolo_labels:", yolo_labels)
     
        # Detect objects and labels using Faster R-CNN
        image = Image.open(image_path).convert("RGB")
        image_tensor = transform(image).unsqueeze(0)
        outputs = faster_rcnn_model(image_tensor)

        print("Faster_rcnn_outputs:", outputs)
    
        faster_rcnn_labels= []
        for box in outputs[0]['labels']:
             num=box.item()
             faster_rcnn_labels.append(coco_names[num-1])
        print("fasterrcnnlabels_num", num)
        print("fasterrcnnlabels: ",faster_rcnn_labels)

        #Combine YOLOv8 labels and Faster R-CNN labels
        combined_labels = list(set(yolo_labels) | set(faster_rcnn_labels))      
    
        # Add unique labels to data dictionary
        for label in combined_labels:
            if label not in data_dict['names'].values():
                 data_dict['names'][label_count] = label
                 label_count += 1

        # Draw bounding boxes and labels on image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Load a font
        font = ImageFont.truetype('arial.ttf', size=20)  # Change the size here

        for box in yolo_results[0].boxes:
            xy = box.xyxy.cpu().tolist()  # Convert tensor to list
            xy = [item for sublist in xy for item in sublist]  # Flatten the list
            x1, y1, x2, y2 = xy
            x1 = max(0, x1-10)
            x2 = min(image.width, x2+10)
            y1 = max(0, y1-10)
            y2 = min(image.height, y2+10)
            draw.rectangle([x1, y1, x2, y2], outline='orange', width=3)
            draw.text((x1, y1-20), text=model.names[box.cls.item()], fill='green', font=font)

            # Normalize coordinates
            image_width, image_height = image.size
            x_center = (x1 + x2) / (2 * image_width)
            y_center = (y1 + y2) / (2 * image_height)
            width = (x2 - x1) / image_width
            height = (y2 - y1) / image_height

            # Append annotation in YOLO format to data list
            class_index = list(data_dict['names'].keys())[list(data_dict['names'].values()).index(model.names[box.cls.item()])]
            annotation_data = f"{class_index} {x_center} {y_center} {width} {height}"

            # Determine whether to save the image in train or val folder
            if i < num_train_images:
                folder_path = train_folder
            else:
                folder_path = val_folder

            # Save annotation file (.txt) to train or val folder
            annotation_file_name = os.path.splitext(os.path.basename(image_path))[0] + '.txt'
            annotation_file_path = os.path.join(folder_path, annotation_file_name)
            with open(annotation_file_path, 'w') as annotation_file:
                annotation_file.write(annotation_data)

            # Save image with bounding boxes and labels to train or val folder
            new_image_path = os.path.join(folder_path, os.path.basename(image_path))
            image.save(new_image_path)
            print(f"Annotated image saved: {new_image_path}")
    
    ###  labeling completd          #datapipeline
    data=json_function.read_json()  
    data['Labelling_completed'] = "True"  
    data['cloud_status'] = "Labeling Completed"
    json_function.write_json(data)
    
    # Update the nc field in data_dict
    data_dict['nc'] = len(data_dict['names'])

    #Save data.yaml file locally      #datapipeline
    data_yaml_path = './data.yaml'
    with open(data_yaml_path, 'w') as yaml_file:
        yaml.dump(data_dict, yaml_file)

     ###  saving model          #datapipeline
    data=json_function.read_json()  
    data['saving_model'] = "True"  
    json_function.write_json(data)

    print("Annotations (.txt) and data.yaml files saved locally with YOLO format annotations and class names.")
