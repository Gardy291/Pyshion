# Pyshion

Pyshion is a Python server-client .exe that makes finding color combination easy. 

## Installation

First, make sure you have [python](https://www.python.org/downloads/) installed to be able to run Pyshion. Verify if it was installed correctly by using the following commands in the cmd. 

```bash
pip -V
```
After downloading and successfully installing [python](https://www.python.org/downloads/), download Pyshion from the [github repository](https://github.com/Gardy291/Pyshion.git). Once you have Pashion downloaded, you can put it to us by entering Python Shell, or any other python interpreter, and typing 

```bash
C:\Users\name\Pyshion> python server.py
```
That line will established the conection between server and client. After establishing the connection you are ready to go and use our application by typing
```bash
C:\Users\name\Pyshion> python Client.py
```
## Usage
```bash
¡Welcome to Pyshion! 

In this application you can find the complementary, splitcomplementary and triad colors 
By using the following syntax: 
	color
	complementary color
	splitcomplementary color
	triad color
These commands will return the possible combinations. For more information type help.

>>>complementary red
   the complementary is green

>>>triad green
   the triads are violet and orange

>>>splitcomplements blue
   the splitcomplements are red-orange and yellow-orange

>>>yellow
 the complementary is violet
 the splitcomplements are blue-violet and red-violet
 the triads are blue and red
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/Lbfe3-v7yE0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
