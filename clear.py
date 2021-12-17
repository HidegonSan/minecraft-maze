from mcpi import minecraft, block

count = 100


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
	mc.player.setPos(1,1,1)


if __name__ == '__main__':
	main()
