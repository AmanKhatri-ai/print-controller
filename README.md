# 3D Printer Controller

This document contains the setup instruction to run this contoller in Raspberry Pi.



**MODULES**

- File Processor



## Setup

### Virtual Environment Setup

```bash
# Create a new virtual environment named env
virtualenv env

# Windows
env\Scipts\activate

# In Linux
source env/bin/activate
```



### Installing Required Libraries

- Install `pyserial` library to interact with serial port.

  ```bash
  pip install pyserial
  ```

- Install `paho-mqtt` for handling MQTT communication.

  ```bash
  pip install paho-mqtt
  ```

- Install `python-dotenv` for dealing with environment variables.

  ```bash
  pip install python-dotenv
  ```

- Install `wget` for downloading files from Internet

  ```bash
  pip install wget
  ```

  



### List Available Serial Ports

To use this command `pyserial` must be installed.

```bash
python -m serial.tools.list_ports -v
```

