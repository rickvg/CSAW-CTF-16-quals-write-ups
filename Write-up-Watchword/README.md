# Write-up Watchword CSAW CTF 2016
In this section you will find the write-up of the Watchword Forensics challenge of CSAW CTF 2016 - 250 points.
The challenge provides the file "powpow.mp4" and several hints:
* Hint: http://domnit.org/stepic/doc/
* Hint: It's not base64, but it uses the Python 3 base64 module
* password = password

Video powpow.mp4 shows a man firing a gun, where the sound of gunshots are replaced by barking. After that it shows a dog barking, where the sound of barking is replaced by gunshots.

First, it would be useful to check whether there are any files hidden within the MP4-file. I checked this using Foremost by using the following command:
> foremost -t all -i powpow.mp4 -o test

Checking the folder, we find two separate folders: mov & png. Each folder contains a file, respectively: 00000000.mov and 00001069.png.
I decided to analyze the MOV-file first using strings:

> strings 00000000.mov

The results contained the following string:
>Stefan Hetzl
><data
>aHR0cDovL3N0ZWdoaWRlLnNvdXJjZWZvcmdlLm5ldC8=

The end of the string appears to be a base64 string within the data tags of the MOV-file. Decoding the base64 string results in:
>http://steghide.sourceforge.net/

Would this be a hint? After looking up Stefan Hetzl, I found he is the creator of Steghide, which is software used to hide data in JPG-files, WAV-files, BMP-files or AU-files.
The files extracted with foremost however, are not in this format. As I was unable to find more information in the MOV-file, I moved on to the PNG-file. The PNG-file was an image of a package oreos.

# Steganography
After finding nothing strange about this file, I decided to check out the hints. The first URL led to Stepic, a Python library used for image steganography.
I decided to use this Python Library to extract data from the PNG-file:

> stepic -d -i 00001069.png

The output showed a header that looked like a JFIF file header, which is used in JPEG/JPG files. So I decided to output the content directly to a JPG-file:

> stepic -d -i 00001069.png > newimage.jpg

The JPG-image showed a dialogue between a mother and a child:
* Mum, why is my cousin Diamond named like that?
* Because your aunty loves diamonds.
* What about me?
* Enough questions Harambe

Right, very nice. No flag at all here. However, we now have a JPG-file which is supported by Steghide. The given hint also mentioned the password is "password", so this is used to extract the data from the JPG-file.

> steghide extract -sf newimage.jpg

Here I enter the passphrase: password. This resulted in the output of Base64.txt

# Base64.txt
The base64 string given in the file: 
>W^7?+dsk&3VRB_4W^-?2X=QYIEFgDfAYpQ4AZBT9VQg%9AZBu9Wh@|fWgua4Wgup0ZeeU}c_3kTVQXa}eE

The hint in the challenge mentioned this is not Base64, but uses the Python3 base64 module. After trying out almost every method of the Python3 base64 module, the following module appeared to be successful and resulted in the flag:
> base64.b85decode("W^7?+dsk&3VRB_4W^-?2X=QYIEFgDfAYpQ4AZBT9VQg%9AZBu9Wh@|fWgua4Wgup0ZeeU}c_3kTVQXa}eE"))

Flag:
> flag{We are fsociety, we are finally free, we are finally awake!}
