import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 8000))

possibilities = [1000000, 500000, 100000, 50000, 10000, 5000, 2000, 1000, 500, 100, 50, 25, 10, 5, 1]

count = 0
arrValues = []

data = s.recv(4048)
while 1:
	print(data)
	if count == 0: #Not useful at all.
		arrValues = []
		split_data = data.split("\n")
		if split_data[0] == "correct!":
			split_data[0] = split_data[1]
		split_data[0] = split_data[0].strip("$")
		split_data[0] = int(split_data[0].replace(".",""))
		print(split_data[0])
		newValue = split_data[0]
		for i in range(0,len(possibilities)):
			possibility = True
			posscount = 0
			while possibility == True:
				if newValue - possibilities[i] >= 0:
					newValue = newValue - possibilities[i]
					posscount += 1
				else:
					possibility = False
			arrValues.append(posscount)
		print(arrValues)
		for i in range(0,len(arrValues)):
			s.send(str(arrValues[i])+"\n")
			data = s.recv(4048)
			print(data)
s.close()
