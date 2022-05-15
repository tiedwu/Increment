from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.vkeyboard import VKeyboard


class VKeyboardTest(BoxLayout):
	def __init__(self, **kwargs):
		super(VKeyboardTest, self).__init__(**kwargs)

		vk = VKeyboard()
		vk.bind(on_key_up=self.key_up)
		self.add_widget(vk)

	def key_up(self, *args):
		print("keydown: ", args[-1], args[1], args[2])

class VKeyboardApp(App):
	def build(self):
		return VKeyboardTest()

if __name__ == '__main__':
	from kivy.core.window import Window
	Window.clearcolor = [.8, .8, .8, 1]
	VKeyboardApp().run()
