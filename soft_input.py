from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import WindowBase

WindowBase.softinput_mode = 'below_target'

from kivy.lang import Builder

Builder.load_string('''
<InputWidget>:
	orientation: 'vertical'
	TextInput:
		text_hint: "key in some words"

	Label:
		id: lbl_show_words
		text: ""
	BoxLayout:
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"
	BoxLayout:
		Label:
			text: "Label#N"
		TextInput:
			text_hint: "key in some words"
		Button:
			text: "submit"

''')


class InputWidget(BoxLayout):
	pass

class TestApp(App):
	def build(self):
		return InputWidget()

if __name__ == '__main__':
	from kivy.core.window import Window
	Window.clearcolor = [.8, .8, .8, 1]
	TestApp().run()
