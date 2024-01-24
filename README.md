# Serial Logger

logs serial ports to files with timestamp

## build image

from this folder

```bash
docker build -t serial-logger .
```

## example use

add devices with `/dev/serial/by-id/` file path, execute from this folder

```bash
docker run -t -i -v .:/app --device=/dev/serial/by-id/usb-FTDI_TTL232R-3V3_FTBB668Z-if00-port0 --device=/dev/serial/by-id/usb-FTDI_TTL232R-3V3_FTBXAN11-if00-port0 --device=/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AL3M2611-if00-port0 serial-logger
```
