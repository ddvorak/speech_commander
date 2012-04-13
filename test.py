import sys
import getopt
import alsaaudio
import datetime
import os



#Set a mixer object to mixer, grab just the Master channel
mixer = alsaaudio.Mixer('Master', 0)

#Grab the volume of the channel
volumes = mixer.getvolume()

#did it grab stuff?
print mixer.mixer()
print volumes


#change the volumes to a string so we can read it with the text to speech tool
volumes = ''.join(map(str,volumes))



def tts(text):
	'''built in text to speech for linux'''
	return os.system("espeak  -s 155 -a 200 "+text+" " )




m = datetime.datetime.now().strftime("%I %M %S")

if volumes == '100': 
	tts("'Bro your volume is maxed out'")

if volumes != '100':
	volumes = volumes + '%'
	tts("'Bro your volume is set to'" + volumes)
