#CPSC 471 Programming Assignment 
Darren Vu
Samantha Ibasitas

Make sure all files and all terminals are within the same directory.
In one terminal first enter: "sudo python3 server.py"
In another terminal enter: "sudo python3 client.py <server host> <port number> <file name"
  
For example, two commands used for testing were:
sudo python3 client.py 127.0.0.1 80 webpage2.html
sudo python3 client.py 127.0.0.1 80 simple_webpage2.html
These commands work perfectly on an Ubuntu machine.
  
 127.0.0.1.80 was chosen as it is localhost.
 
 Make note: If you exit the server with a keyboard interrupt the Port seems to have a timeout for about 60 or so seconds. There will be a small delay before you can run the server.py program again. You can either wait out the time or change both the server and client's port to another value.
