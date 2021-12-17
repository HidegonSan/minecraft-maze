from mcpi import minecraft, block
from mazelib import Maze
from mazelib.generate.Prims import Prims
import time
import random

M = 10
N = 10
H = 5
count = 1000
waitTime = 0.1
index = 0
setPos = False


def put_maze_block(mc, mark, x_pos, z_pos):
	if mark == '#':
		mc.setBlocks(
			x_pos, 0, z_pos,
			x_pos, H - 1, z_pos,
			block.WOOL
		)


def change_maze(mc):
	global index
	if index == 0:
		index = 1
	else:
		index = 0
	while True:
		while True:
			place_x = random.randint(1, M * 2 - 1)
			place_z = random.randint(1, N * 2 - 1)
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
				if index == 0:
					break
			if blockState == 35:
				if index == 1:
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
	if setPos:
		mc.player.setPos(1.5, 0, 0.5)
	mc.setBlocks(
		-5, 0, -5,
		M * 2 + 10, 200, N * 2 + 10,
		block.AIR
	)
	mc.setBlocks(
		-5, -1, -5,
		M * 2 + 10, -1, N * 2 + 10,
		block.STONE
	)
	mc.setBlock(1, -1, 0, block.GOLD_BLOCK)
	mc.setBlock(M * 2 - 1, -1, N * 2, block.DIAMOND_BLOCK)

	mz = Maze()
	mz.generator = Prims(N, M)
	mz.generate()

	mz.start = (0, 1)
	mz.end = (N * 2, M * 2 - 1)

	maze_str = str(mz)
	maze_list = maze_str.split('\n')

	for z, maze_list in enumerate(maze_list):
		for x, mark in enumerate(maze_list):
			put_maze_block(mc, mark, x, z)

	mc.postToChat('start!!')
	for num in range(count):
		time.sleep(waitTime)
		change_maze(mc)


if __name__ == '__main__':
	main()
