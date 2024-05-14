# main.py

import autolabel
import train
import json_function

data=json_function.read_json()    
data['Image_imported'] = "False"
data['Labelling_started']= "False"
data['Labelling_completed'] ="False"
data['Training_started']= "False"
data['Training_completed']= "False"
json_function.write_json(data)

def main():
    autolabel.label_images()
    train.train_model()

if __name__ == "__main__":
    main()

