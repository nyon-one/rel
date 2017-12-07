from . import Rel
from configparser import ConfigParser

class Config(ConfigParser):
	def __init__(self, relative_file, file_name='data.ini'):
		ConfigParser.__init__(self)
		self.doc = Rel(relative_file).doc(file_name)
		self.read(self.doc.dest_path)
		self.options = self.defaults()

	def save(self):
		with self.doc.open_func('w') as w:
			self.write(w)

	def ammend(self, obj):
		self.options.update(obj)
