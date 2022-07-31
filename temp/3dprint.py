import serial
import time
from datetime import datetime

def command(ser, command):
  start_time = datetime.now()
  ser.write(str.encode(command)) 
  time.sleep(1)

  while True:
    line = ser.readline()
    print(line)

    if line == b'ok\n':
      break

# Connecting to serial port
# TODO: Verify serial port and baud rate
ser = serial.Serial('/dev/tty.usbserial-AG0KEQWV', 115200)
time.sleep(2)

# Heat bed to 45 degrees celsius but do not wait
command(ser, "M140 S45\r\n")

# Report temperature
command(ser, "M105\r\n")

# Wait for bed to heat to 45 degrees celsius and wait
command(ser, "M190 S45\r\n")

# Extruder Temp to 215 degree celsius
command(ser, "M104 S215\r\n")
# command(ser, "M104 S190 T0\r\n") #  start heating T0 to 190 degrees Celsius

# Report temperature
command(ser, "M105\r\n")

# Wait for extruder to reach 215 degrees before continuing with any other commands
command(ser, "M109 S215\r\n")
# command(ser, "M109 S190 T0\r\n") # wait for T0 to reach 190 degrees before continuing with any other commands

# absolute extrusion mode
command(ser, "M82\r\n")

# Reset Extruder
command(ser, "G92 E0\r\n")

# Return all axis to home position
command(ser, "G28\r\n")

# Move Z Axis up little to prevent scratching of Heat Bed
command(ser, "G1 Z2.0 F3000\r\n")

# Move to start position
command(ser, "G1 X0.1 Y20 Z0.3 F5000.0\r\n")

# Draw the first line
command(ser, "G1 X0.1 Y200.0 Z0.3 F1500.0 E15\r\n")

# Move to side a little
command(ser, "G1 X0.4 Y200.0 Z0.3 F5000.0\r\n")

# Draw the second line
command(ser, "G1 X0.4 Y20 Z0.3 F1500.0 E30\r\n")

# Reset Extruder
command(ser, "G92 E0\r\n")

# Move Z Axis up little to prevent scratching of Heat Bed
command(ser, "G1 Z2.0 F3000\r\n")

# Move over to prevent blob squish
command(ser, "G1 X5 Y20 Z0.3 F5000.0\r\n")


command(ser, "G92 E0\r\n")
command(ser, "G92 E0\r\n")

command(ser, "G1 F2700 E-5\r\n")
command(ser, "M107\r\n")
command(ser, "G1 F300 Z0.4\r\n")
command(ser, "G0 F6000 X105.566 Y95.458 Z0.4\r\n")
command(ser, "G1 F300 Z0.2\r\n")
command(ser, "G1 F2700 E0\r\n")
command(ser, "G1 F1200 X106.198 Y94.764 E0.03122\r\n")
command(ser, "G1 X106.886 Y94.127 E0.0624\r\n")
command(ser, "G1 X107.626 Y93.551 E0.09359\r\n")
command(ser, "G1 X108.412 Y93.039 E0.12479\r\n")
command(ser, "G1 X109.239 Y92.597 E0.15598\r\n")

# Return all axis to home position
# command(ser, "G28\r\n")
# command(ser, "G28 X0 Y0 Z0\r\n")
# command(ser, "G28 X0 Y0\r\n")
# command(ser, "G28 X0\r\n")
# command(ser, "G28 Y0\r\n")
# command(ser, "G28 Z0\r\n")

# Fan
# command(ser, "M106 S255\r\n") # fan speed full
# command(ser, "M106 S127\r\n") # fan speed about half
# command(ser, "M106 S0\r\n") # turn off fan

time.sleep(2)
ser.close()
