# Stand-Alone-Keyboard-Solenoid
#Summary:
	This is a device to emulate solenoid action that is unattached to your keyboard as a fun gag. The goal follows old solenoid enabled keyboards except is standalone and can attach to any keyboard enabling even laptop enjoyers to use it without too much tampering of their beloved device. Some may find the solenoid sound to be remedial and some may find it to be obnoxious.
#Hardware:
	To build the device this is what is required:
		1x – solenoid 9V
		2x – 9V batteries
		1x – TIP120 transistor
		1x – diode
		1x – 2.2k olm resistor
		1x – pro micro (most Arduino can be substituted for this with 1 output pin and 1 ground pin)
		1x – housing
		2x – alligator clips
		1x – micro usb
		Soldering skills
#Wiring Diagram:
	The wiring diagram will look something like this, instead of the 12V it is the daisy chained 9V:
 

#Dependencies:
	The software requires you to install a few dependencies including python and pip, this is how you install the rest:
pip install keyboard

python -m pip install pyserial

#Firmware:
	The code should look like this and is called inputarduino.ino
 
Open this in Arduino IDE and hit the -> button in the top left while the Arduino is connected via USB to flash the board. You may need to specify which controller you are flashing and which COM port

#Software:
	The software is relatively straightforward. There may be alittle bit of setting up so while the Arduino is plugged in via USB go to windows key->device manager and drop down the ports section:
 
Note the Arduino micro being on COM7,
Second open the python code lastattempt.py in your favorite IDE and change line 5 to match the port the Arduino micro is on (ie. COM7 in this case):
 

Now everything is ready, open terminal and go to the directory of where lastattempt.py is and run python lastattempt.py.

Any typing registered now should activate the solenoid if everything is setup properly.


*Notes: do not control + C out of terminal use = to exit the program or your solenoid will be stuck in the on position and start heating up until the battery is no longer in use. 
