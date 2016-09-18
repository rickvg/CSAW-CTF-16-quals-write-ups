# Python 2.7
# By rickvg - https://github.com/rickvg

# Imports
import socket
import re
import rstr

# Send specified payload to server and return received response
def sendpayload(strpayload):
    s.send(str(strpayload) + "\n")
    rcvdata = s.recv(16000)
    rcvdata = rcvdata.strip("\n")
    print(rcvdata)
    return rcvdata


# Set up socket & connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 8001))

# Receive initial data from server (2 transfers). Second transfer = Issued Regex
data = s.recv(16000)
data = s.recv(16000)

# Print regex issued by server
print("Issued regex: " + data)

# Loop through all possibilities of the server software
while "flag" not in data:
    # Use rstr library with xeger method to generate string based on regex - https://bitbucket.org/leapfrogdevelopment/rstr/
    response = rstr.xeger(re.compile(data))

    # Replace all unsupported characters. Initially this would only be \n, but rest is removed to be sure.
    response = response.replace('\n', '!').replace('\r', '!').replace('\t', '!').replace(' ', '!')
    print("Data to send back: " + response)
    data = sendpayload(response)

s.close()
