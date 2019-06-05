import os

file = 'buff.txt'

def execute(str):
	if not '\n' in str:
		buff = os.popen(str + ' 2>&1').read()
		yield buff
	else:
		cmds = str.split('\n')
		for cmd in cmds:
			yield os.popen(cmd + ' 2>&1').read()
	