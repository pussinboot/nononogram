from puzzle import Puzzle

def parse_mario_puzzle(puzzle_rep):
	# marios picross gamefaq convert
	# (http://www.gamefaqs.com/gameboy/563278-marios-picross/faqs/6189)
	puzzle_rep = puzzle_rep.split('\n')[2::2]
	# it's enough to look at every other row to know if the
	# cell is blank or filled in
	for i in range(len(puzzle_rep)):
		puzzle_rep[i] = puzzle_rep[i][2::4]
	return "\n".join(puzzle_rep)


if __name__ == '__main__':
	with open('./puzzles/L','r') as f:
		L_puzzle = f.read()
	L_parsed = parse_mario_puzzle(L_puzzle)
	print(L_parsed)