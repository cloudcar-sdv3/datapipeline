
from flask import Flask, request, send_file, render_template, jsonify, send_from_directory
from io import BytesIO
import numpy as np
import cv2
import base64
import json
import time
import os
import subprocess
# from validation import pop_up
# from ui import ui
import shutil
import config.config as config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  

last_update_client_time = None
dataReceived_status = 'N/A'                              # Default status message
TrainedModel_status = 'N/A'           
TrainingModel_status = 'N/A'             
EvaluatingModel_status = 'N/A'            
SavingModel_status = 'N/A'     

DATA_FILE = '../ui_with_react/public/update.json'               # Global variable to hold the last update_client time

def write_json(update_values):                                 # Function to update the update.json file
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    for key, value in update_values.items():
        data[key] = value
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


def update_database_file():
    with open(DATA_FILE, 'r') as file:                           # Load the content of update.json
        data = json.load(file)

    data["Image_imported"] = "False"                         # Modify the values as needed
    data["Labelling_started"] = "False"
    data["Labelling_completed"] = "False"  
    data["Training_started"] = "False"                         # Modify the values as needed
    data["Training_completed"] = "False"
    data["saving_model"] = "False"
    data["cloud_status"] = ""
    with open(DATA_FILE, 'w') as file:                           # Write the updated content back to update.json
        json.dump(data, file, indent=2)

#-------------------------------------------------------------------------------------
# Route to receive the Harvester Server response     # 
@app.route('/DataReceived', methods=['POST'])
def request_to_dataReceived_endpoint():
    global dataReceived_status
    data = request.get_json()
    status = data.get('status', 'FAILED')
    if status.lower() == 'success':
        dataReceived_status = 'SUCCESS'
        # Update the update.json file
        write_json({'cloud_data': "True"})                           # Assuming 'cloud_data' is a boolean field
        write_json({'cloud_status':"Data Imported"})
    else:
        dataReceived_status = 'FAILED'
        write_json({'cloud_data': "False"})
    return jsonify({'status': dataReceived_status})

#-------------------------------------------------------------------------------------
# @app.route('/dataReceived_status', methods=['GET'])          # Route the status of the Harvester Server data received status to Frontend                          
# def get_dataReceived_status():
#     return jsonify({'status': dataReceived_status})

#-------------------------------------------------------------------------------------
@app.route('/TrainedModel', methods=['POST'])                         # Route to receive the TrainedModel response
def request_to_TrainedModel_endpoint():
    global TrainedModel_status
    data = request.get_json()
    status = data.get('status', 'FAILED')
    if status.lower() == 'success':
        TrainedModel_status = 'SUCCESS'
        # Update the update.json file
        write_json({'mlops_start': "True"})                           # Assuming 'mlops_start' is a boolean field
        write_json({'cloud_status':"Training Started"})
    else:
        TrainedModel_status = 'FAILED'
        write_json({'mlops_start': "False"})
    return jsonify({'status': TrainedModel_status})

#-------------------------------------------------------------------------------------
# @app.route('/TrainedModel_status', methods=['GET'])                   # Route the status of the TrainedModel status to Frontend
# def get_TrainedModel_status():
#     return jsonify({'status': TrainedModel_status})

#-------------------------------------------------------------------------------------
@app.route('/TrainingModel', methods=['POST'])                           # Route to receive the TrainingModel response
def request_to_TrainingModel_endpoint():
    global TrainingModel_status
    data = request.get_json()
    status = data.get('status', 'FAILED')
    if status.lower() == 'success':
        TrainingModel_status = 'SUCCESS'
        # Update the update.json file
        write_json({'mlops_end': "True"})                            # Assuming 'mlops_end' is a boolean field
        write_json({'cloud_status':"Training Ended"})
    else:
        TrainingModel_status = 'FAILED'
        write_json({'mlops_end': "False"})
    return jsonify({'status': TrainingModel_status})

#-------------------------------------------------------------------------------------
# @app.route('/TrainingModel_status', methods=['GET'])                     # Route the status of the TrainingModel status to Frontend
# def get_TrainingModel_status():
#     return jsonify({'status': TrainingModel_status})

#-------------------------------------------------------------------------------------
@app.route('/EvaluatingModel', methods=['POST'])                          # Route to receive the EvaluatingModel response 
def request_to_EvaluatingModel_endpoint():
    global EvaluatingModel_status
    data = request.get_json()
    status = data.get('status', 'FAILED')
    if status.lower() == 'success':
        EvaluatingModel_status = 'SUCCESS'
        # Update the update.json file
        write_json({'code_build': "True"})                           # Assuming 'code_build' is a boolean field
        write_json({'cloud_status':"Evaluating Model"})
    else:
        EvaluatingModel_status = 'FAILED'
        write_json({'code_build': "False"})
    return jsonify({'status': EvaluatingModel_status})

#-------------------------------------------------------------------------------------
# @app.route('/EvaluatingModel_status', methods=['GET'])                    # Route the status of the EvaluatingModel status to Frontend
# def get_EvaluatingModel_status():
#     return jsonify({'status': EvaluatingModel_status})

#-------------------------------------------------------------------------------------
@app.route('/SavingModel', methods=['POST'])                       # Route to receive the OTA Triggered response
def request_to_SavingModel_endpoint():
    global SavingModel_status
    data = request.get_json()
    status = data.get('status', 'FAILED')
    if status.lower() == 'success':
        SavingModel_status = 'SUCCESS'
        # Update the update.json file
        write_json({'ota_trigger': "True"})                          # Assuming 'ota_trigger' is a boolean field
        write_json({'cloud_status':"Saving Model"})
    else:
        SavingModel_status = 'FAILED'
        write_json({'ota_trigger': "False"})
    return jsonify({'status': SavingModel_status})

#-------------------------------------------------------------------------------------
# @app.route('/SavingModel_status', methods=['GET'])                 # Route the status of the OTA Triggered status to Frontend
# def get_SavingModel_status():
#     return jsonify({'status': SavingModel_status})
#-------------------------------------------------------------------------------------

if __name__ == '__main__':
    update_database_file()    
    app.run(debug=True,host='0.0.0.0',port=5555)
