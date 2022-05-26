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
		self.bind(b'/dismiss_military', self.dismiss)
		self.bind(b'/set_lancer', self.set_lancer)
		self.bind(b'/set_shieldman', self.set_shieldman)
		self.bind(b'/set_archer', self.set_archer)
		self.bind(b'/set_cavalryman', self.set_cavalryman)
		self.bind(b'/gain_double_gathering', self.gain_double_gathering)
		self.bind(b'/gain_double_payload', self.gain_double_payload)
		self.bind(b'/set_residents', self.set_residents)

	def set_residents(self, arg):
		residents = int(arg.decode('utf8'))
		self.data["residents"] = residents

	def gain_double_gathering(self, arg):
		gain = int(arg.decode('utf8'))
		self.data["double_gathering_time"] += gain

	def gain_double_payload(self, arg):
		gain = int(arg.decode('utf8'))
		self.data["double_payload_time"] += gain

	def set_lancer(self, arg):
		unit = int(arg.decode('utf8'))
		self.data["soldiers"]["lancer"] = unit

	def set_shieldman(self, arg):
		unit = int(arg.decode('utf8'))
		self.data["soldiers"]["shieldman"] = unit

	def set_archer(self, arg):
		unit = int(arg.decode('utf8'))
		self.data["soldiers"]["archer"] = unit

	def set_cavalryman(self, arg):
		unit = int(arg.decode('utf8'))
		self.data["soldiers"]["cavalryman"] = unit

	def dismiss(self):
		print("service(): dismiss_military")
		for k in self.data["soldiers"].keys():
			self.data["soldiers"][k] = 0

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
		#print("soldiers: %d" % soldiers)

		# resident - soldiers = labors = increase for normal
		self.labors = increase = self.data["residents"] - soldiers
		#increase = self.data["resources_increase"]
		if self.data["double_gathering_time"] > 0:
			increase = increase * 2
			self.data["double_gathering_time"] -= 1
		self.data["resources"] += increase
		#print("send resources %d" % self.data["resources"])

		# check double_payload_time
		if self.data["double_payload_time"] > 0:
			self.data["double_payload_time"] -= 1
		#self.count += 1
		res = str(self.data["resources"]).encode('utf8')
		inc = str(increase).encode('utf8')
		dg_remain = str(self.data["double_gathering_time"]).encode('utf8')
		dp_remain = str(self.data["double_payload_time"]).encode('utf8')
		CLIENT.send_message(b'/resources', [res, inc, dg_remain, dp_remain])

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


