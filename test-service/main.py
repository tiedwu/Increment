# coding: utf8

__version__ = '0.1'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.utils import platform

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient


Builder.load_string('''
<RootWidget>:
	orientation: 'vertical'
	Label:
		id: lbl_id
		text: "0"


''')


class RootWidget(BoxLayout):
	pass

class TestApp(App):
	count = 0
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		if platform == 'android':
			self.start_service()

	def build(self):

		self.server = server = OSCThreadServer()
		server.listen(
			address=b'localhost',
			port=3002,
			default=True,
		)

		server.bind(b'/msg_received', self.show_number)

		self.client = OSCClient(b'localhost', 3000)
		self.root = RootWidget()
		return self.root

	def show_number(self, message):
		if self.root:
			self.root.ids.lbl_id.text = message.decode('utf8')

	@staticmethod
	def start_service():
		from jnius import autoclass
		service = autoclass("org.kivy.oscservice.ServiceEmpire")
		mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
		service.start(mActivity, "")
		return service

if __name__ == '__main__':
	TestApp().run()
