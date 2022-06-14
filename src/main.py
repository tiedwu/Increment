import os

from kivy.logger import Logger
from kivy.app import App
from kivy.uix.label import Label

from android.permissions import Permission, request_permissions
from android.permissions import check_permission

from android.storage import app_storage_path, primary_external_storage_path
from android.storage import secondary_external_storage_path

def log(msg):
	Logger.info(msg)

def check_permissions(perms):
	for perm in perms:
		if check_permission(perm) != True:
			return False
	return True

def testwrite():
	testfile = bytes([1, 2, 3, 4])

	perms = [Permission.WRITE_EXTERNAL_STORAGE, \
		Permission.READ_EXTERNAL_STORAGE]

	if check_permissions(perms) != True:
		request_permissions(perms)
		exit()

	try:
		Logger.info('Got requested permissions')
		fname = os.path.join(primary_external_storage_path(), 'testfile')
		#fname = os.path.join(app_storage_path(), 'testfile')
		log('writing to : %s' % fname)

		with open(fname, 'wb') as f:
			f.write(testfile)

		return fname

	except:
		log('could not write to external storage ... missing permissions ?')

class MyApp(App):
	def build(self):
		return Label(text='wrote to %s' % testwrite())

MyApp().run()
