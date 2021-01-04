![LUNA logo](/images/LUNA.jpg)

LUNA is a python project design to run on the Raspberry Pi Hardware (at best gen 2 or newer). LUNA acts as a voice asisstance such as Alexa or Siri. 
With LUNA you can check the weather, create a shopping list, control smart devices in your home or listen to some music. LUNA makes it possible - while also beeing free!

## Installation 
For the seperation, we differentiate between Client on Server. LUNA supports multiple clients located in different rooms. 
The server can be installed on the same Pi as a client or on a different one. 

### Client installation 
As a client you will need some sort of microphone and speaker. It is recommended however, that you dont use the onboard audio capabilities of the Raspberry Pi but rather
use an USB Speaker. 
For the Linux distribution running on your Pi we recommend simply using the Raspberry OS. 
For installation instructions use [this](https://www.raspberrypi.org/downloads/raspberry-pi-os/) site

Now let's get LUNA actually running for you!

### Server installation
The server handles all client requests and helps with the communication between clients. 
Firstly you will need to install some important packages:
`sudo apt-get install python3.5-dev python3.4-dev`

Needed audio brackets:
`sudo apt-get install portaudio19-dev sox flac`

Speech Recognition: 
`sudo pip3 install SpeechRecognition` 

Voice output: 
`sudo apt-get install libttspico0 libttspico-utils` 

Since there is a problem with the recent package manager of Rasperry OS you will need to install some packages manually.

`wget http://ftp.us.debian.org/debian/pool/non-free/s/svox/libttspico0_1.0+git20130326-9_armhf.deb` 

`wget http://ftp.us.debian.org/debian/pool/non-free/s/svox/libttspico-utils_1.0+git20130326-9_armhf.deb`

Now run:

`sudo apt-get install -f ./libttspico0_1.0+git20130326-9_armhf.deb ./libttspico-utils_1.0+git20130326-9_armhf.deb`


Now onto the real server installation. For that we will need some more Python libraries.

´sudo pip3 install telepot´

`sudo apt-get install portaudio19-dev sox flac ffmpeg`

`pip3 install pyaudio` 

Additionaly LUNA uses some more Python packages to access important data. Install them by running this: 

`sudo pip3 install wikipedia googlemaps spacex_py html5lib python_dateutil pytube3 phue`

and

`sudo apt-get install xdotool`

Now you are almost done with installing LUNA. You can download LUNA itself now by cloning this GitHub-Repo to your home folder.

`git clone https://github.com/JakobPrie/LUNA.git`

Now cd into the LUNA directory and execute the installation file by running:

`sudo python3 LUNA_setup_server.py`

The installation file will guide you through the rest of the installation process. Have fun with LUNA!
