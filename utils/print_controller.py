import serial
import time

# Utils
from utils.downloader import fileDownload

def connect_printer(port_name, baud_rate):
    '''
    Connect to the 3D printer serial port for serial communication

    Parameters:
        port_name: Name of serial port to which 3D printer is connected
        baud_rate: Specify the baud rate for serial communication

    Returns:
        serial_connection: Serial connection object which can be used to read and wrrite to serial port
    '''
    print(f"[PRINT CONTROLLER] Connecting to printer...")

    serial_connection = serial.Serial(port_name, baud_rate)
    time.sleep(2)

    print(f"[PRINT CONTROLLER] Connected to printer")
    return serial_connection


def send_command(serial_connection, command):
    '''
    Send a command to 3D printer and waits for response from printer

    Parameters:
        serial_connection: Serial connection object to send the command
        command: Payload to send via serial connection

    Returns:
        None
    '''
    serial_connection.write(str.encode(command))
    time.sleep(1)

    while True:
        line = serial_connection.readline()
        print(f"[PRINT CONTROLLER] Printer response: { line }")

        if b'ok' in line:
            break


def start_print(serial_connection, filepath):
    '''
    Processes the 3D file and starts printing

    Parameters:
        serial_connection: Serial connection object to communicate with device
        filepath: Path where the file is stored

    Returns:
        None
    '''
    print(f"[PRINT CONTROLLER] Processing model file...")

    # Opening the gcodes and saving into list
    gcodes = []
    with open(filepath) as file:
        gcodes = file.readlines()

    gcodes_len = len(gcodes)
    
    print(f"\n[PRINT CONTROLLER] Starting print...\n")

    current_line = 0
    for gcode in gcodes:
        gcode = gcode.rstrip("\n") + "\r\n"
        send_command(serial_connection, gcode)

        # Print progress
        print(f"[PRINT CONTROLLER] Print Progress: { round(((current_line * 100) / gcodes_len), 2) }%")
        current_line += 1

    print(f"[PRINT CONTROLLER] Printing complete")
    print(f"[PRINT CONTROLLER] Closing serial connection")
    time.sleep(2)
    serial_connection.close()


def start_3d_print(serial_config, url, filepath):
    '''
    Downloads the model file, initiate the 3D printer and start printing

    Parameters:
        url (String): 3D file download URL
        filepath (String): filepath to store the file, should include extension also

    Returns:
        None
    '''
    # Downloading the model file
    model_path = fileDownload(url, filepath)

    # Connecting to 3D printer
    serial_connection = connect_printer(serial_config["serial_port"], serial_config["baudrate"])

    # Start the printing
    start_print(serial_connection, model_path)
