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

def gen_puzzle(puzzle_rep):
	# creates the hints needed from a puzzles representation
	rows = puzzle_rep.split('\n')
	# row hints
	row_hints = []
	for row in rows:
		row_hints += [[len(block) for block in row.split(" ") if len(block) > 0 ]]
	# col hints
	col_hints = []
	for i in range(len(rows[0])):
		col = "".join([row[i] for row in rows])
		col_hints += [[len(block) for block in col.split(" ") if len(block) > 0 ]]

	puz_tor = Puzzle(row_hints,col_hints,rows)
	return puz_tor

if __name__ == '__main__':
	with open('./puzzles/L','r') as f:
		L_puzzle = f.read()
	L_parsed = parse_mario_puzzle(L_puzzle)
	print(gen_puzzle(L_parsed))
	# print(L_parsed)