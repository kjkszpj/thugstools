import os
import os.path

rootdir='/Users/you/Music/'
for parent, dirnames, filenames in os.walk(rootdir):
	for file in filenames:
		fullname = os.path.join(parent, file)
		if fullname.endswith('.cue'):
			os.system('cp "%s" "%s.temp"' %(fullname, fullname))
			if (os.system('iconv -f GBK -t UTF-8 "%s">"%s.temp"' %(fullname, fullname)) != 0):
				print(fullname)
				#u = input()
			else:
				os.system('mv "%s.temp" "%s"' %(fullname, fullname))