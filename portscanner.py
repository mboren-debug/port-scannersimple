import socket

#TCP port scanner for a network that allows user to identify if a port on localhost is open or not.





def pscan(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Initiates connection to port and defines connection. AF_INET indicated connection to IPv4, and SOCK_STREAM indicates continuous connection between client and server with TCP. The with commands closes the connection no matter the result.
            s.settimeout(1) #Arrives at conclusion about connection within 1 second.
            s.connect((target, port)) #Connects to the IP address, and its port.
            return True


    except:
        print(f"Port {port} is not open.")

def main():
    target = input('Enter a target IP: ').strip()  # Target of port scanning.
    port_str = input('Enter a target port: ').strip() #Allows user to decide port and regulates string formatting.
    try:
        port = int(port_str)#Converts port decision into integer.
    except:
        print(f"Port {port_str} is not valid.")
        return False
    if not (1 <= port <= 65535):
        print(f"Port {port} is out of range!")
        return False

    if pscan(target, port):
        print(f"Port {port} is open")
        return
    else:
        print(f"Port {port} is closed")



if __name__ == "__main__":
    main()
