from pydoc import cli
from statistics import mode
from dotenv import load_dotenv
import os
import json
import argparse

# MQTT imports
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# Utils
from utils.print_controller import start_3d_print

# take environment variables from .env
load_dotenv()


# The callback for when the client receives a CONNACK response from the server
def mqtt_on_connect(client, userdata, flags, rc):
    print("[MAIN] MQTT connection success")

    # Subscribing to topics
    client.subscribe("wutbruh/pi/print")


# The callback for when a PUBLISH message is received from the server
def mqtt_on_message(client, userdata, msg):
    payloadJson = str(msg.payload.decode("utf-8"))
    data = json.loads(payloadJson)

    # Starting the 3D print
    start_3d_print(userdata["serial_config"], url=data["path"], filepath=data["filename"])


def main(args):
    # Serial connection details
    userdata = {
        "serial_config": {
            "serial_port": args.serial,
            "baudrate": args.baudrate
        }
    }

    # Creating MQTT client and assigning callbacks
    client = mqtt.Client(userdata=userdata)
    client.on_connect = mqtt_on_connect
    client.on_message = mqtt_on_message

    # Connecting to MQTT broker
    client.username_pw_set(
        username=os.environ.get("MQTT_USERNAME"),
        password=os.environ.get("MQTT_PASSWORD")
    )

    client.connect(
        os.environ.get("MQTT_URL"),
        int(os.environ.get("MQTT_PORT")),
        60
    )

    # Starting a background thread to handle network loop
    # To stop this background thread call- client.loop_stop()
    client.loop_start()

    while True:
        pass


if __name__ == "__main__":
    # Command line arguments parser
    parser = argparse.ArgumentParser()

    # Adding arguments to parser
    serial_port_description = '''Name of the serial port to which 3D printer is connected.
        To check available serial ports use:
        python -m serial.tools.list_ports -v
        '''
    baudrate_description = "Baud rate to communicate with serial device"
    parser.add_argument("-s", "--serial", type=str, required=True, help=serial_port_description)
    parser.add_argument("-b", "--baudrate", type=int, required=False, default=115200, help=baudrate_description)

    # Parsing command line args
    args = parser.parse_args()
    
    main(args)
