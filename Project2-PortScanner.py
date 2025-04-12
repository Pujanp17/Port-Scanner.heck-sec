import socket
from datetime import datetime

# Function to scan ports on a given IP address and port range
def scan_ports(ip, start_port, end_port):
    open_ports = []
    print(f"\nStarting scan on {ip} from port {start_port} to {end_port}...\n")
    start_time = datetime.now()

# Loop through the specified port range
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object using IPv4 and TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5) # Set timeout for each connection attempt

            # Attempt to connect to the target IP and port
            result = sock.connect_ex((ip, port))

            # If result is 0, the port is open
            if result == 0:
                open_ports.append(port)
                print(f"[+] Port {port} is open")

            # Close the socket after each attempt    
            sock.close()

        except socket.error as err:
            # Handle socket errors such as connection issues
            print(f"Socket error: {err}")
            break

    end_time = datetime.now()
    print(f"\nScan completed in: {end_time - start_time}")
    # Print message if no open ports are found
    if not open_ports:
        print("No open ports found.")
    return open_ports

# Function to get and validate user input
def get_user_input():
    ip = input("Enter IP address to scan: ").strip()
    # Validate the IP address format
    try:
        socket.inet_aton(ip)# Raises error if IP is invalid
    except socket.error:
        print("Invalid IP address.")
        return

    try:
        # Get and validate port range from user
        start_port = int(input("Enter start port (0-65535): "))
        end_port = int(input("Enter end port (0-65535): "))
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port):
            print("Invalid port range.")
            return
    except ValueError:
        # Handle non-integer port values
        print("Port numbers must be integers.")
        return

    # Call the scanning function with user input
    scan_ports(ip, start_port, end_port)

# Entry point of the script
if __name__ == "__main__":
    get_user_input()
