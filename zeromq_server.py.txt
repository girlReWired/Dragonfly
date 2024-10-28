import zmq
import time
from multiprocessing import Process

def start_publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5555")  # ZeroMQ server on port 5555

    print("ZeroMQ Publisher started at tcp://127.0.0.1:5555")

    # Loop to keep publisher active
    while True:
        time.sleep(1)  # Keep running to listen for messages

def publish_vote_update(vote_data):
    context = zmq.Context.instance()
    socket = context.socket(zmq.PUB)
    socket.connect("tcp://127.0.0.1:5555")  # Connect to publisher
    socket.send_json(vote_data)  # Send vote update data as JSON

if __name__ == "__main__":
    # Run the ZeroMQ server as a separate process
    Process(target=start_publisher).start()
