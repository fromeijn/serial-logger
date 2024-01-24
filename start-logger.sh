#!/bin/bash

cd /dev/serial/by-id

mkdir -p /app/logs

date_str=$(date +%y%m%d-%H%M%S)

for serial_port in ./*; do
    echo "Starting logger on $serial_port"
	python3 /app/logger.py $serial_port /app/logs/$date_str-$(basename $serial_port).log &
done


echo "Waiting for logger to finish... (Ctrl+C to exit)"
while true; do
	sleep 1
done
