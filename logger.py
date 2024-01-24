#!/usr/bin/python3

import serial
import datetime
import csv
import argparse

parser = argparse.ArgumentParser(description="Serial logger")
parser.add_argument("port", help="Serial port to log")
parser.add_argument("logfile", type=argparse.FileType("w", encoding="latin-1"), help="File to log to")
parser.add_argument("--baud", type=int, default=115200, help="Baud rate")
args = parser.parse_args()

ser = serial.Serial(args.port, baudrate=args.baud)
ser.flushInput()
port_name = args.port.split("/")[-1]

while True:
    try:
        ser_line = ser.readline()
        time_str = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"\033[93m {port_name}\033[00m \033[92m {time_str}\033[00m {ser_line}")
        writer = csv.writer(args.logfile, delimiter=",")
        writer.writerow([time_str, ser_line])
        args.logfile.flush()
    except:
        print("Exit")
        break
