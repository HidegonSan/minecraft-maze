from mcpi import minecraft, block
import time
import random
import sys

M = 20
N = 20
H = 5
setPos = False
finish = False
posX = [1]
posZ = [1]
changeCount = 100
waitTime = 1
index2 = 0

file = sys.argv[0].replace('.exe', '').split(',')
if len(file) == 7:
	M = int(file[1])
	N = int(file[2])
	H = int(file[3])
	if int(file[4]):
		setPos = True
	changeCount = int(file[5])
	waitTime = float(file[6])


def put_maze_block(mc):
	global posX
	global posZ
	count = 0
	for num in range(len(posX)):
		num3 = random.sample(range(0, len(posX)), len(posX))
		index = random.sample(range(1, 5), 4)
		time.sleep(0.001)
		for num2 in range(4):
			if index[num2] == 1:
				blockstateN = mc.getBlock(posX[num3[num]], 0, posZ[num3[num]] - 2)
				if blockstateN == 35:
					mc.setBlocks(
						posX[num3[num]], 0, posZ[num3[num]],
						posX[num3[num]], H - 1, posZ[num3[num]] - 2,
						block.AIR
					)
					posX.append(posX[num3[num]])
					posZ.append(posZ[num3[num]] - 2)
					break
				else:
					count += 1
			elif index[num2] == 2:
				blockstateS = mc.getBlock(posX[num3[num]], 0, posZ[num3[num]] + 2)
				if blockstateS == 35:
					mc.setBlocks(
						posX[num3[num]], 0, posZ[num3[num]],
						posX[num3[num]], H - 1, posZ[num3[num]] + 2,
						block.AIR
					)
					posX.append(posX[num3[num]])
					posZ.append(posZ[num3[num]] + 2)
					break
				else:
					count += 1
			elif index[num2] == 3:
				blockstateW = mc.getBlock(posX[num3[num]] - 2, 0, posZ[num3[num]])
				if blockstateW == 35:
					mc.setBlocks(
						posX[num3[num]], 0, posZ[num3[num]],
						posX[num3[num]] - 2, H - 1, posZ[num3[num]],
						block.AIR
					)
					posX.append(posX[num3[num]] - 2)
					posZ.append(posZ[num3[num]])
					break
				else:
					count += 1
			elif index[num2] == 4:
				blockstateE = mc.getBlock(posX[num3[num]] + 2, 0, posZ[num3[num]])
				if blockstateE == 35:
					mc.setBlocks(
						posX[num3[num]], 0, posZ[num3[num]],
						posX[num3[num]] + 2, H - 1, posZ[num3[num]],
						block.AIR
					)
					posX.append(posX[num3[num]] + 2)
					posZ.append(posZ[num3[num]])
					break
				else:
					count += 1
		if count == M * N:
			global finish
			finish = True


def change_maze(mc):
	global index2
	if index2 == 0:
		index2 = 1
	else:
		index2 = 0
	while True:
		while True:
			if index2 == 0:
				place_x = random.randint(1, M - 2)
				place_z = random.randint(1, N - 1)
				if place_x % 2 == 1:
					place_x += 1
				if place_z % 2 == 0:
					place_x += 1
			else:
				place_x = random.randint(1, M - 4)
				place_z = random.randint(1, N - 3)
				if place_x % 2 == 0:
					place_x += 1
				if place_z % 2 == 1:
					place_x += 1

			playerPos = int(mc.player.getPos().x) + int(mc.player.getPos().z)
			difference = playerPos - place_z - place_x
			if difference > 4 or difference < -4:
				break
		facing = 0
		blockstateN = mc.getBlock(place_x, 0, place_z - 1)
		if blockstateN == 0:
			facing += 1
		blockstateS = mc.getBlock(place_x, 0, place_z + 1)
		if blockstateS == 0:
			facing += 1
		blockstateW = mc.getBlock(place_x - 1, 0, place_z)
		if blockstateW == 0:
			facing += 1
		blockstateE = mc.getBlock(place_x + 1, 0, place_z)
		if blockstateE == 0:
			facing += 1
		if facing >= 2:
			blockState = mc.getBlock(place_x, 0, place_z)
			if blockState == 0:
				if index2 == 1:
					break
			if blockState == 35:
				if index2 == 0:
					break

	blockState = mc.getBlock(place_x, 0, place_z)
	if blockState == 35:
		mc.setBlocks(
			place_x, 0, place_z,
			place_x, H - 1, place_z,
			block.AIR
		)
	else:
		mc.setBlocks(
			place_x, 0, place_z,
			place_x, H - 1, place_z,
			block.WOOL
		)


def main():
	mc = minecraft.Minecraft.create()
	mc.setBlocks(
		0, 0, 0,
		M, H - 1, N,
		block.WOOL
	)
	mc.setBlocks(
		1, 0, 0,
		1, H - 1, 0,
		block.AIR
	)
	mc.setBlocks(
		M - 1, 0, N,
		M - 1, H - 1, N,
		block.AIR
	)
	mc.setBlock(1, -1, 0, block.GOLD_BLOCK)
	mc.setBlock(M - 1, -1, N, block.DIAMOND_BLOCK)
	while not finish:
		time.sleep(0.01)
		put_maze_block(mc)

	if setPos:
		mc.player.setPos(1.5, 0, 0.5)
	mc.postToChat('start!!')
	for num in range(changeCount):
		time.sleep(waitTime)
		change_maze(mc)


if __name__ == '__main__':
	main()
