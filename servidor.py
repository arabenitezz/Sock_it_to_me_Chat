import socket # --> Libreria que gestiona la conexion de red
import threading # --> Libreria que permite ejecutar varias tareas al mismo tiempo

# Definir la conexion de datos e inicializar el socket

host = 'localhost' # --> Almacena y gestiona archivos compartidos en la red
port = 3000 # --> Lugar virtual en el sistema en donde empiezan y terminan las conexiones red

# Creamos un objeto de socket que toma de argumento lo necesario para indicar que usaremos el protocolo IPv4 y 
# lo que usamos para indicar que utilizaremos un socket de flujo y protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # --> asignamos al objeto socket a el puerto y host elegidos
server.listen() # --> ponemos al servidor en modo escucha

# Creamos listas para los usuarios 
clients = [] # --> sockets
usernames = [] # --> string

# Creamos una funcion para enviar mensajes generales

def broadcast(message): 
    for client in clients:
        client.send(message)

# Funcion para gestinar los mensajes de los clientes

def manage(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close() # --> cerramos el socket del cliente
            username = usernames[index]
            broadcast('{} salió del chat'.format(username).encode('utf-8')) # --> avisamos a todos que el usuario (client) se desconecto
            usernames.remove(username)
            break

# Funcion para aceptar y agregar a los usuarios en el servidor

def receive():
    while True:
        client, adress = server.accept() # --> aceptamos conexiones de los clientes asignándoles un socket
        print('Conectado desde {}'.format(str(adress)))

        client.send('NICK'.encode('utf-8')) # --> enviamos un codigo NICK para indicar que pedimos un nombre de usuario
        username = client.recv(1024).decode('utf-8')
        usernames.append(username) # --> metemos el nombre de usuario a la lista de nombres de usuario
        clients.append(client) # --> metemos el socket correspondiente al cliente en la lista de clientes

        print("Usuario: {}".format(username))
        broadcast("{} se ha unido al chat".format(username).encode('utf-8'))
        client.send('Te has conectado exitosamente'.encode('utf-8'))

        thread = threading.Thread(target=manage, args=(client,)) # --> creamos un nuevo hilo y definimos que funcion manejara
        thread.start() # --> inicializamos el hilo

print('Servidor activo :)')
receive() # --> llamamos a la funcion