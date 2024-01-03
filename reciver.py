# receiver.py

import socket
def process_data(data):

    # ESP32 server address and port
    esp32_ip = "192.168.0.107"  # Replace with the ESP32's IP address
    esp32_port = 80  # Replace with the port number used by your ESP32 server

    print(f"Received data: {data}")
    try:

        data_to_send = data

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the ESP32 server
        client_socket.connect((esp32_ip, esp32_port))

        # Send data to the ESP32
        client_socket.sendall(data_to_send.encode())

        # Close the socket
        client_socket.close()

        print(f"Data sent to {esp32_ip}:{esp32_port}: {data_to_send}")

    except ConnectionRefusedError:
        print(
            "Connection to the ESP32 was refused. Make sure the ESP32 server is running and the IP and port are correct.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Receiver script is running.")
    process_data("0")
