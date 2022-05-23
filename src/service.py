from kivy.utils import platform
from time import sleep

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

import json

#from os.path import abspath

CLIENT = OSCClient('localhost', 3002)

class GameService(OSCThreadServer):

	count = 0

	user_id = "999999"
	data_path = "data/user_data.json"
	data = {}

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.listen('localhost', port=3000, default=True)
		self.bind(b'/resources_increase', self.res_inc)
		self.bind(b'/resources_decrease', self.res_dec)

	def res_inc(self, arg):
		inc = int(arg.decode('utf8'))
		#print(ins)
		self.data["resources"] += inc

	def res_dec(self, arg):
		dec = int(arg.decode('utf8'))
		self.data["resources"] -= dec

	def init_data(self):
		#print(abspath(self.data_path))
		#from os.path import realpath
		#print(realpath(self.data_path))
		with open(self.data_path, "r") as f:
			all_data = json.load(f)
			self.data = all_data[self.user_id]

	def get_soldiers(self):
		amount = 0
		for k in self.data["soldiers"].keys():
			amount += self.data["soldiers"][k]
		return amount

	def check_data(self):
		soldiers = self.get_soldiers()

		# resident - soldiers = labors = increase for normal
		self.labors = increase = self.data["residents"] - soldiers
		#increase = self.data["resources_increase"]
		if self.data["double_gathering_time"] > 0:
			increase = increase * 2
			self.data["double_gathering_time"] -= 1
		self.data["resources"] += increase
		print("send resources %d" % self.data["resources"])
		#self.count += 1
		res = str(self.data["resources"]).encode('utf8')
		ins = str(increase).encode('utf8')
		remain = str(self.data["double_gathering_time"]).encode('utf8')
		CLIENT.send_message(b'/resources', [res, ins, remain])

if __name__ == '__main__':
	if platform == 'android':
		from jnius import autoclass
		PythonService = autoclass('org.kivy.android.PythonService')
	loop = 0
	server = GameService()
	server.init_data()
	while True:
		print("[%d]service running..." % loop)
		server.check_data()
		loop += 1
		sleep(1)


