Andre Le
CSE 283 - Section A
Date: October 15 - 2017
Assignment: Project 1 - Web Server

To run the program:
1. If you are using Mac, go to Terminal (if you are on Window then go to cmd).
2. Determine the IP address of the server you are in (you can do this by typing 'ifconfig' in your terminal and look for the IP of your Internet).
3. Once you have your IP address, go into the file program.py and change the value of variable 'ip' to your IP address, then save it.
4. Go back to Terminal, Type 'python program.py' to start the program
5. If it returns 'Ready to serve...', then you are ready to go.
6. From the browser, go to http://<your_id_address>:1234/index.html (For example: http://172.22.30.250:1234/index1.html)
7. You should see it works, the content of the index.html file appears. The terminal prints out ‘Send successfully’
8. Go to http://<your_id_address>:1234/index1.html, you should see it does not work (received 404 Not Found), the terminal should print out ‘error in sending’ denotes that the file is not presented in the server.
