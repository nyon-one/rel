from os import path
import os

class Doc(object):
	def __init__(self, dest_path):
		self.dest_path = dest_path
		self.is_file = path.isfile(dest_path)

	def open_func(self, _type, encoding='utf-8'):
		return open(self.dest_path, _type, encoding=encoding)

class Document(Doc):		
	def write(self, text):
		with self.open_func('a') as w:
			w.write(text.strip())

	def read(self):
		with self.open_func('r') as r:
			read = r.read()
			read = read.strip()
			return read

class Rel(object):
	def __init__(self, file_path):
		self.file_path = path.abspath(file_path)
		self.rel_dir = path.dirname(self.file_path) if not path.isdir(file_path) else file_path

	def __str__(self):
		return 'dirname: %s file_path: %s'%(self.rel_dir, self.file_path)

	def join(self, *args):
		return path.join(self.rel_dir, *args)

	def folder(self, dirname):
		dir_path = self.join(dirname)
		if not path.isdir(dir_path):os.mkdir(dir_path)
		return Rel(dir_path)

	def data(self):
		folder = self.folder('data')
		return Document(path.join(folder, 'data'))

	def doc(self, file_name):
		return Doc(self.join(file_name))

	def document(self, file_name):
		return Document(self.join(file_name))

# r = Rel(__file__)
# d = r.folder('.data').document('data.json')

# d.write('''gogogo''')
# print(d)