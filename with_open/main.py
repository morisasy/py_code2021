import os.path

filename = "./data.csv"


if os.path.isfile(filename):
	with open(filename, 'rw') as f:
		fn = f.read()
		print(fn)
else:
	print(f'file {filename} does not exist')
