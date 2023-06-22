import socket
import threading


questions ={
    'STP protocl mainmission is preventing later 3 loops .': 'f',
    'The device can send and receive at the same time when workin on Half-Duplex mode.': 'f',
    '6In STP, Blocking ports can still receive BBDUs.': 't',
    'VLANS help in reducing the size of broadcast domains.': 't',
    'Root switch has many Root ports .': 'f',
    'We can use only one router port to serve multiple VLANs .': 't',
    'ISL is a type of routing protocols.': 'f',
    'same switch may support multiple LAN technologies.': 't',
    'HTTP DNS FTP are Transport Layer protocols.': 'f',
    'SRES is an essential data of GSN SIM card.': 'f',
    'There is need to use any mobility managment between in progress calls inside the cell.': 'f',
    'Slow frequency hopper is a part of BSC block diagram.': 'f',
    'same switch may support multiple LAN technologies.': 't',
    'Any cellular operation starts using BCCH.': 'f',
    ' VLANS help in reducing the size of broadcast domains.': 't',
    ' Root switch has many Root ports .': 'f',
    ' We can use only one router port to serve multiple VLANs .': 't',
    ' UDP adds Sequence number to sending datagrams.': 'f',
    ' same switch may support multiple LAN technologies.': 't',
    'In GSM system, the access burst has the longest guard bits.': 't',
    'UDP adds Sequence number to sending datagrams.': 'f'
}


scores = {}

def new_client(client_socket, address):
    for question in questions.keys():
        client_socket.send(question.encode())
        answer = client_socket.recv(1024).decode()

        if answer == questions[question]:
            scores[address] = scores.get(address, 0) + 1

    if address in scores:
        score_message = '{}/{}'.format(scores[address], len(questions))
        client_socket.send(score_message.encode())

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 4432))
    server_socket.listen(5)
    print('server started .')
    while True:
        client_socket, address = server_socket.accept()
        print('New client  :', address)

        client_thread = threading.Thread(target=new_client, args=(client_socket, address))
        client_thread.start()
start_server()

