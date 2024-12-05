from picamera import PiCamera 
from time import sleep
from datetime import datetime


camera = PiCamera()
camera.resolution = (1296, 972)

# Fumction to get the date and time as a string
def get_datetime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

dateandtime = get_datetime()

# camera.start_preview()

file_path = f'/home/deepcanyonnrs/MicrowaveSensor/videos/{dateandtime}.h264'

camera.start_recording(file_path)
sleep(5)

camera.stop_recording()

camera.close()


# camera.stop_preview()