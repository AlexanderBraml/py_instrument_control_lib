import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

c = 0

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(1)
    conn, addr = s.accept()

    output = ''

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                break

            data = data.decode('UTF-8')

            output += data
            if 'print' in data:
                conn.sendall(str(c).encode())
                output += f'Sent {c}\n'
                c += 1

        except socket.error as e:
            print("Error Occured.", e)
            break

    print(output)

    conn.close()
