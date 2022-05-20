
# coding: utf8

from time import sleep
from kivy.utils import platform

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient


CLIENT = OSCClient('localhost', 3002)

class GameService(OSCThreadServer):

	count = 0
	def __init__(self, **kwargs):
		super(GameService, self).__init__(**kwargs)

	def send_data(self):

		self.count += 1

		msg = str(self.count).encode('utf8')
		CLIENT.send_message(
			b'/msg_received',\
			[msg,],\
		)



if __name__ == '__main__':
	if platform == 'android':
		from jnius import autoclass
		PythonService = autoclass('org.kivy.android.PythonService')

		#from android.broadcast import BroadcastReceiver
		#broadcast_receiver = BroadcastReceiver(

		#)
		#broadcast_receiver.start()

	server = GameService()

	num = 0
	while True:
		print("[%d]service running..." % num)
		server.send_data()
		sleep(5)
		num += 1
