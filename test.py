import sys
import getopt
import alsaaudio
import datetime
import os




mixer = alsaaudio.Mixer('Master', 0)
volumes = mixer.getvolume()

print mixer.mixer()
print volumes

volumes = ''.join(map(str,volumes))



def tts(text):
      return os.system("espeak  -s 155 -a 200 "+text+" " )




m = datetime.datetime.now().strftime("%I %M %S")

if volumes == '100': 
	tts("'Bro your volume is maxed out'")

'''if volumes != '100':
	volumes = volumes + '%'
	tts("'Bro your volume is set to'" + volumes)
'''

def lsser():
	return os.system("ls")



lsser()