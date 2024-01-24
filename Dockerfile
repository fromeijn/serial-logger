FROM ubuntu:20.04
WORKDIR /app
RUN apt update && apt install -y python3 python3-serial
CMD [ "./start-logger.sh" ]
