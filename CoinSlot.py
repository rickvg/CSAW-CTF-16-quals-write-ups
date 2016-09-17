import socket
import re

# Send specified payload to server and return received response
def sendpayload(strpayload):
    s.send(str(strpayload) + "\n")
    rcvdata = s.recv(4096)
    print(rcvdata)
    return rcvdata

# Set up socket & connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 8000))

# All possible values in online application, where syntax: [integer/float] * 100
possibilities = [1000000, 500000, 100000, 50000, 10000, 5000, 2000, 1000, 500, 100, 50, 25, 10, 5, 1]

arrValues = []

# Receive initial data from server
data = s.recv(4096)
print(data)

# Loop through all possibilities of the server software
while "flag" not in data:
    arrValues = []

    # Filter server received data to format, possible to convert to an integer
    reqmoney = int(re.sub('\$|\.|correct!|\n|10,000 bills:', '', data))
    print("Requested money * 100: $" + str(reqmoney))

    # Loop through all possibilities from possibilities array
    for i in range(0, len(possibilities)):
        possibility = True
        posscount = 0

        # Loop through a specific possibility to check whether it still fits in the remaining money value
        while possibility == True:
            if reqmoney - possibilities[i] >= 0:
                reqmoney = reqmoney - possibilities[i]
                posscount += 1
            else:
                possibility = False

        # Save count of a specific money value
        arrValues.append(posscount)

    # Send count of money values to server
    for i in range(0, len(arrValues)):
        data = sendpayload(arrValues[i])

s.close()
