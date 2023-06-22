import socket

def start_client():
    server_address = ('localhost', 4432)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    
    for i in range (20):
        question = client_socket.recv(1024).decode()
        print("Question:", question)
        answer = input("Your answer (t or f): ")
        client_socket.sendall(answer.encode())
    
    final_score = client_socket.recv(1024).decode()
    print( 'Score:' ,final_score)



start_client()
