from communitysdk import list_connected_devices
from communitysdk import RetailPixelKitSerial as PixelKit
from time import sleep

from KanoVertical import KanoVertical

devices = list_connected_devices()
pk_filter = filter(lambda device: isinstance(device, PixelKit), devices)
pk = next(pk_filter, None) # Get first Pixel Kit

if pk != None:
	# Sample lighting of the four corners with KanoVertical
	kano = KanoVertical()
	kano.set(0, 0, '#ff0000')
	kano.set(7,0, '#00ff00')
	kano.set(0, 15,'#0000ff')
	kano.set(7, 15, '#ffff00')

	'''
	We will send a frame every 0.1 seconds to Pixel Kit (10 frames
    per second). It's important to keep sending frames to the Pixel Kit,
    otherwise it will go back to the mode it was before.
	'''
	while True:
		pk.stream_frame(kano.frame)
		sleep(0.1)
else:
	print('No Pixel Kit was found :(')
