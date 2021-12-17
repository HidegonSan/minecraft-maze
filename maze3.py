from mcpi import minecraft, block
import time
import random

M = 20  # length(set even)
N = 20  # width(set even)
H = 5   # height
setPos = True
finish = False   # set False
posX = [1]   # set 1
posZ = [1]   # set 1


def put_maze_block(mc):
	global posX
	global posZ
	count = 0
	for num in range(len(posX)):
		num3 = random.sample(range(0, len(posX)), len(posX))
		index = random.sample(range(1, 5), 4)
		time.sleep(0.01)
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
	mc.setBlock(1, -1, 0,block.GOLD_BLOCK)
	mc.setBlock(M - 1, -1, N, block.DIAMOND_BLOCK)
	while not finish:
		time.sleep(0.01)
		put_maze_block(mc)

	if setPos:
		mc.player.setPos(1.5, 0, 0.5)
	mc.postToChat('start!!')


if __name__ == '__main__':
	main()
