from communitysdk import list_connected_devices
from communitysdk import RetailPixelKitSerial as PixelKit
from time import sleep

from KanoVertical import KanoVertical
import RandomHex

devices = list_connected_devices()
pk_filter = filter(lambda device: isinstance(device, PixelKit), devices)
pk = next(pk_filter, None) # Get first Pixel Kit

if pk != None:
	kano = KanoVertical()
	
	'''
	Seems like 10 frames per a second is the minimum speed else Pixel Kit
	will thin we have finished.
	'''
	while True:
		for y in range(kano.height):
			for x in range(kano.width):
				kano.set(x, y, RandomHex.generate())

		pk.stream_frame(kano.frame)
		sleep(0.1)
else:
	print('No Pixel Kit was found :(')
