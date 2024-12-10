# Chat Cliente-Servidor con Sockets en Python  

Este proyecto implementa un sistema de chat cliente-servidor utilizando sockets TCP/IP en Python. Permite la conexión de múltiples clientes a un servidor central para enviar y recibir mensajes en tiempo real.  

## Requisitos  

- Python 3.7 o superior  

## Archivos principales  

1. **`cliente.py`**: Script para los clientes que se conectan al servidor.  
2. **`servidor.py`**: Script que ejecuta el servidor para gestionar las conexiones y los mensajes.  

## Instalación  

1. Clona este repositorio en tu máquina local:  
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```  

2. Asegúrate de que ambos scripts estén en la misma carpeta para facilitar la ejecución.  

## Ejecución  

### Paso 1: Iniciar el servidor  
Ejecuta el archivo `servidor.py` en tu terminal para inicializar el servidor.  
```bash
python servidor.py
```  
El servidor estará escuchando conexiones en `localhost` y el puerto `3000`.  

### Paso 2: Conectar clientes  
Ejecuta el archivo `cliente.py` para conectar un cliente al servidor.  
```bash
python cliente.py
```  
El cliente deberá ingresar un nombre de usuario al iniciar.  

### Comunicación en el chat  
- Los mensajes enviados por un cliente serán transmitidos a todos los demás usuarios conectados.  
- Si un cliente se desconecta, el servidor notificará al resto del grupo.  

## Características  

- **Servidor multicliente**: Soporta múltiples conexiones simultáneas utilizando `threading`.  
- **Mensajes en tiempo real**: Cada mensaje enviado por un cliente es retransmitido a todos los demás.  
- **Desconexión automática**: Si un cliente se desconecta inesperadamente, el servidor lo maneja limpiamente.  

## Estructura del proyecto  

```
.
├── cliente.py      # Script del cliente
├── servidor.py     # Script del servidor
└── README.md       # Este archivo
```  

## Notas importantes  

- Asegúrate de que el puerto `3000` esté disponible en tu máquina antes de iniciar el servidor.  
- Este proyecto está configurado para funcionar en `localhost`. Si deseas usarlo en una red diferente, actualiza las variables `host` en ambos scripts.  

## Contribuciones  

Si tienes ideas para mejorar el proyecto, siéntete libre de abrir issues o enviar pull requests.  

---

Proyecto para Penguin Academy 🐧🚀
