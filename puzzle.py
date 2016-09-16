class Puzzle():
	"""docstring for Puzzle"""
	def __init__(self, row_hints, col_hints,known_sol=None):
		self.row_hints, self.col_hints = row_hints, col_hints
		self.dims = (len(row_hints),len(col_hints))
		self.known_sol = known_sol

	def __str__(self):
		# bad ascii art of the puzzle
		# first figure out offsets..
		x_offset = max([len(rh) for rh in self.row_hints])
		y_offset = max([len(ch) for ch in self.col_hints])

		tor = ""

		# header (col hints)
		header = [[0 for w in range(self.dims[1])] for h in range(y_offset)] 
		for i, ch in enumerate(self.col_hints):
			ch.reverse()
			for j, hint in enumerate(ch):
				ind = y_offset - j - 1
				header[ind][i]=hint
			
		for line in header:
			tor += " " * (2 * x_offset) + "| "
			for hint in line:
				if hint > 0:
					tor += str(hint) + " "
				else:
					tor += "  "
			tor+="\n"

		tor += "-" * x_offset * 2 + "+" + "-" * self.dims[1]*2 + "\n"
		# row hints
		rhs = [[0 for w in range(x_offset)] for h in range(self.dims[0])] 
		for j, rh in enumerate(self.row_hints):
			rh.reverse()
			for i, hint in enumerate(rh):
				rhs[j][i]=hint

		for i, row in enumerate(rhs):
			row.reverse()
			for hint in row:
				if hint > 0:
					tor += str(hint) + " "
				else:
					tor += "  "
			tor += "| "
			if self.known_sol is not None:
				for c in self.known_sol[i]:
					if c != " ":
						tor += "# "
					else:
						tor += "  "

			tor+="\n"

		return tor
		# return "puzzle"
		