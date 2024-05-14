"""
module containing global variables
"""

def initialize(): 
    global UPLOAD_PATH
    global JSON_FILE
    global IMAGE_FILE
    global IMAGE_PATH
    global CAMERA_IMAGE
    global CAMERA_NO
    global TIMESTAMP
    global ZIP_PATH
    global ZIP_FILE
    global HARVESTER_SERVER_URL
    global DETECTION_DIFF_FLAG
    global VIDEO_FILE_PATH
    global CONFIDENCE_THRESHOLD
    global OTA_UPDATE_FLAG
    global NODE_SWAP_FLAG
    global OTA_CONFORMATION_FLAG

    global MAX_ITERATIONS
    global ITERATION_COUNT 
    global MAX_ITERATIONS_COUNT

    global INPUT_IMAGE
    global FRCNN_OUTPUT
    global YOLO_V1_OUTPUT
    global YOLO_V2_OUTPUT
    global DIFFERENCE_OUTPUT
    global UI_SIZE

    global INPUT_IMAGE_PATH     
    global DIFF_IMAGE_PATH      
    global IMAGE_FRAMES_PATH    
    global YOLO_V1_IMAGE_PATH  
    global FRCNN_IMAGE_PATH   
    global YOLO_V2_IMAGE_PATH

    global FRCNN_SERVER
    global YOLO_V1_SERVER
    global YOLO_V2_SERVER 

    global JSON_UPDATE
    global DATA_UPDATE
    global PADDING_WIDTH

    global SOURCE
    global LLM
    global USER_NODE
    global SHADOW_NODE
    global DIFFERENCE
    global PAUSE_TEXT

    global WINDOW_WIDTH
    global WINDOW_HEIGHT

    global DETECTION
    global TOTAL_FRAMES
    global CURRENT_FRAME
    global TOTAL_FRAMES_COUNT

    global SCALE_PERCENT
    global POSITION_A
    global POSITION_B
    global POSITION_X
    global POSITION_Y
    global INPUT_SOURCE

    global FRCNN_RESULT
    global YOLO_V1_RESULT
    global DIFFERENCE_RESULT
    global YOLO_V2_RESULT

    global LOADING_SOURCE_PATH
    global LOADING_DESTINATION_PATH    

    global SIZE
    global OUTPUT
    
    SIZE = 40
    WINDOW_WIDTH = 375
    WINDOW_HEIGHT = 125
    CAMERA_NO = 0
    MAX_ITERATIONS_COUNT = 70
    TOTAL_FRAMES_COUNT = 110
    MAX_ITERATIONS = 8
    ITERATION_COUNT = 0

    SCALE_PERCENT = 100
    POSITION_A = 3 * SCALE_PERCENT
    POSITION_B = 0.3 * SCALE_PERCENT
    POSITION_X = 1.35 * SCALE_PERCENT
    POSITION_Y = 2.5 * SCALE_PERCENT

    DETECTION_DIFF_FLAG = True
    OTA_UPDATE_FLAG     = False
    OTA_CONFORMATION_FLAG = False
    NODE_SWAP_FLAG    = False

    PADDING_WIDTH   = "1"
    JSON_UPDATE     = "../ui_with_react/public/update.json"
    DATA_UPDATE     = "../database.json"

    UPLOAD_PATH     = "./data/upload/"
    ZIP_PATH        = "./data/"

    # FRCNN_SERVER    = "http://localhost:30183/predict"
    # YOLO_V1_SERVER  = "http://localhost:32359/predict"
    # YOLO_V2_SERVER  = "http://localhost:30813/predict"

    FRCNN_SERVER    = "http://localhost:7002/predict"
    YOLO_V1_SERVER  = "http://localhost:7001/predict"
    YOLO_V2_SERVER  = "http://localhost:7003/predict"
    
    JSON_FILE       = ".json"
    IMAGE_FILE      = ".jpg"
    ZIP_FILE        = ".zip"

    VIDEO_FILE_PATH = "./data/video/newyork_4_fps_360p_screen_1280x720.mp4"
    
    LOADING_SOURCE_PATH="./data/result/yolo-v2/loading.jpg"
    LOADING_DESTINATION_PATH="./data/result/yolo-v2/output.jpg"
    
    INPUT_IMAGE_PATH   = "./data/image/"
    DIFF_IMAGE_PATH    = "./data/result/diff/"
    IMAGE_FRAMES_PATH  = "./data/image_frames/"
    YOLO_V1_IMAGE_PATH = "./data/input/yolo-v1/"
    FRCNN_IMAGE_PATH   = "./data/input/faster-rcnn/"
    YOLO_V2_IMAGE_PATH = "./data/input/yolo-v2/"
    YOLO_V1_OUTPUT     = "./data/result/yolo-v1/"

    FRCNN_RESULT       ="./data/result/faster-rcnn/output.jpg"
    YOLO_V1_RESULT     ="./data/result/yolo-v1/output.jpg"
    DIFFERENCE_RESULT  ="./data/result/diff/output.jpg"
    YOLO_V2_RESULT     ="./data/result/yolo-v2/output.jpg"
    OUTPUT             ="./data/result/output/output.jpg"

    INPUT_SOURCE       = "input.jpg"
    
    IMAGE_PATH      = "./data/image/"
    CAMERA_IMAGE       = "_CamImg.jpg"
    TIMESTAMP          = ""

    CONFIDENCE_THRESHOLD = 70

    HARVESTER_SERVER_URL    = 'http://ec2-54-159-44-128.compute-1.amazonaws.com:3000/app/videoupload'

    DETECTION       = {}
    TOTAL_FRAMES    = 1
    CURRENT_FRAME   = 1

    SOURCE          = "Source"
    LLM             = "Advanced"
    USER_NODE       = "Base"
    SHADOW_NODE     = "Updated Base"
    DIFFERENCE      = "Difference"
    PAUSE_TEXT      = "Demo Paused"
