from picamera import PiCamera 
from time import sleep
from datetime import datetime

#intialize the camera
camera = PiCamera()

# Fumction to get the date and time as a string
def get_datetime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

camera.start_preview()
sleep(2)
dateandtime = get_datetime()
file_path = f'/home/deepcanyonnrs/{dateandtime}.jpg'

camera.capture(file_path)
camera.stop_preview()

