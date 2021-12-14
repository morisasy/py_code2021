import socket
import platform

get_hostname = socket.gethostname()
get_platform_name = platform.node()

print(get_hostname)
print(platform_name)