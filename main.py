import time
import random
import os, sys

try:
	size = int(sys.argv[1])
	chance = int(sys.argv[2])
except IndexError:
	size = 50
	chance = 10

x, y = size, size

mtrxin = [[' ' for i in range(x)] for j in range(y)]
mtrxout = [[' ' for i in range(x)] for j in range(y)]

for rx in range(x):
	for ry in range(y):
		odds = random.randint(0, 100)
		if odds <= chance: mtrxin[rx][ry]='#'

def neighbors(cx, cy):
	neighbors = 0
	xmod, ymod = 0, 0
	if cx+1>=x: xmod=x
	if cy+1>=y: ymod=y
	check = [mtrxin[cx-1][cy-1], mtrxin[cx][cy-1], mtrxin[cx+1-xmod][cy-1],
			mtrxin[cx-1][cy], mtrxin[cx+1-xmod][cy],
			mtrxin[cx-1][cy+1-ymod], mtrxin[cx][cy+1-ymod], mtrxin[cx+1-xmod][cy+1-ymod]]

	for cell in check:
		if cell=='#': neighbors+=1

	return neighbors


def toBeOrNotToBe(x, y):
	near = neighbors(x, y)
	if near == 3: return '#'
	if near == 2 and mtrxin[x][y]=='#': return '#'
	return ' ' 

while True:
	time.sleep(0.3)
	os.system('cls' if os.name == 'nt' else 'clear')
	for rx in mtrxin:
		print(' '.join(rx))


	for rx in range(x):
		for ry in range(y):
			mtrxout[rx][ry] = toBeOrNotToBe(rx, ry)

	mtrxin = mtrxout
	mtrxout = [[' ' for i in range(x)] for j in range(y)]
