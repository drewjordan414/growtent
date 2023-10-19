# housekeeping, import 
from flask import Flask, Response, jsonify
# video streaming
import cv2
# sensors
import board
import busio 
import adafruit_seesaw
import adafruit_sht4x
import adafruit_tsl2591
# proxy 
from flask_cors import CORS
import time 
# database
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import datetime
import os
import dotenv

# Initialize I2C sensors 
i2c = busio.I2C(board.SCL, board.SDA)
ss = adafruit_seesaw.Seesaw(i2c)
sht = adafruit_sht4x.SHT4x(i2c)
tsl = adafruit_tsl2591.TSL2591(i2c)

# initialize db settings
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")

app = Flask(__name__)
# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_password}@{db_host}/{db_name}'
db = SQLAlchemy(app)
# CORS handling
CORS(app)  

# snesor ids
SENSOR_IDS = {
    "temperature": 1,
    "humidity": 2,
    "soil": 3,
    "light": 4
}


def read_temp():
    """Read the temperature in Fahrenheit from the SHT40."""
    temp = sht.temperature * 1.8 + 32
    return round(temp, 2)


def read_humidity():
    """Read the humidity from the SHT40."""
    humidity =  sht.relative_humidity
    return round(humidity, 2)


def read_soil():
    """Read the soil moisture from the soil sensor."""
    return ss.moisture_read()

def read_light():
    """Read the light sensor value."""
    light = tsl.lux
    return round(light, 2)

# Define the SQLAlchemy model for the sensors table
class SensorReading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)  # Storing the actual sensor value
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# @app.route('/api/sensor_data')
# def sensor_data():
#     """Provide sensor data as a JSON response."""
#     data = {
#         "temperature": read_temp(),
#         "humidity": read_humidity(),
#         "soil": read_soil(),
#         "light": read_light()
#     }
#     #send the data to graphs 
#     return jsonify(data)
                        # this is old code that was used to send data wihout database


@app.route('/api/sensor_data')
def sensor_data():
    """Provide sensor data as a JSON response."""
    data = {
        "temperature": read_temp(),
        "humidity": read_humidity(),
        "soil": read_soil(),
        "light": read_light()
    }
    
    # Store the data in the database
    for sensor_type, value in data.items():
        reading = SensorReading(
            sensor_id=SENSOR_IDS[sensor_type],
            value=value
        )
        db.session.add(reading)
    
    db.session.commit()

    return jsonify(data)



def gen():
    """Generate the video stream."""
    cap = cv2.VideoCapture(0)
    
    # Reduce resolution for faster processing (e.g., set to 640x480)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Increase JPEG compression for smaller frame size, but be aware this might reduce quality
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]  
        ret, jpeg = cv2.imencode('.jpg', frame, encode_param)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

        # Use a fixed time delay to attempt a more consistent frame rate
        time.sleep(0.0333)

@app.route('/api/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
