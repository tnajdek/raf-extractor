import os, errno

def mkdir_p(path):
	try:
		os.makedirs(path)
	except OSError as exc: # Python >2.5
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else: raise


def convert_lol_path(path):
	if(os.pathsep != '/'):
		raise Exception("Not implementedy yet :(")
	return path