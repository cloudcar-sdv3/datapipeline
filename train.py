from ultralytics import YOLO
import json_function
import time

def train_model():
    # data.yaml file path
    local_data_yaml_path = "./data.yaml"

    # Load the YOLOv8n model
    model = YOLO('yolov8n.pt')  # Load the pretrained model
    
    # Set training parameters
    epochs = 1
    imgsz = 640
    device = 'cpu'  # Use CPU for training
    
    # Train the model
    data=json_function.read_json()    
    data['Training_started'] = "True"
    data['cloud_status'] = "Training Started"
    json_function.write_json(data)
    
    print("Training started")
    results = model.train(data=local_data_yaml_path, epochs=epochs, imgsz=imgsz, device=device)
        
    data=json_function.read_json() 
    data['Training_completed'] = "True"
    data['cloud_status'] = "Training Completed"
    json_function.write_json(data)

    print("Training completed.")

    time.sleep(10)

    data=json_function.read_json() 
    data['Saving_Model'] = "True"
    data['cloud_status'] = "Model Saved"
    json_function.write_json(data)
    print("Model saved")

    time.sleep(10)

    data=json_function.read_json() 
    data['Ota_Trigger'] = "True"
    data['cloud_status'] = "Ota Triggered"
    json_function.write_json(data)
    print("OTA Triggered")



    


   

