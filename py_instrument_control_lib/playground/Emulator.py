import socket
import sys
from random import randrange

response_mode = 0  # Reponse to print messages. 0: Static number, 1: Incrementing counter, 2: Random number in range
static_number = 1  # If static (0)
counter = 0  # If counter (1)
lower_bound, upper_bound = int(1e9), int(1e12)  # If random number (2)


def response_data() -> int:
    match response_mode:
        case 0:
            return static_number
        case 1:
            global counter
            counter += 1
            return counter
        case 2:
            return randrange(int(1e9), int(1e12))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid number of arguments. Expected IP and port of host.')
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode('UTF-8')
            print('Recv:', data)
            if 'print' in data or 'IDN?' in data:
                response = response_data()
                conn.sendall(str(response).encode())
                print('Sent:', response)

        except socket.error as e:
            print("Error Occured.", e)
            break

    conn.close()
