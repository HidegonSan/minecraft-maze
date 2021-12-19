from mcpi import minecraft, block
import sys

count = 100
file = sys.argv[0].replace('.exe', '').split(',')
if len(file) == 2:
	count = int(file[1])


def main():
	mc = minecraft.Minecraft.create()
	mc.setBlocks(
		-count, 0, -count,
		count, 200, count,
		block.AIR
	)
	mc.setBlocks(
		-count, -1, -count,
		count, -1, count,
		block.STONE
	)
	mc.player.setPos(0, 0, 0)


if __name__ == '__main__':
	main()
