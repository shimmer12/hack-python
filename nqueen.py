

global N
N = 4

def Soln(bread):
	for i in range(N):
		for j in range(N):
			print (bread[i][j],end=' ')
		print()



def safeis(bread, row, col):

	# Check this row on left side
	for i in range(col):
		if bread[row][i] == 1:
			return False

	
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if bread[i][j] == 1:
			return False

	
	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if bread[i][j] == 1:
			return False

	return True

def solveNQUtil(bread, col):
	
	if col >= N:
		return True

	
	for i in range(N):

		if safeis(bread, i, col):
			# Place this queen in bread[i][col]
			bread[i][col] = 1

			# recur to place rest of the queens
			if solveNQUtil(bread, col + 1) == True:
				return True

			# If placing queen in bread[i][col
			# doesn't lead to a solution, then
			# queen from bread[i][col]
			bread[i][col] = 0

	# if the queen can not be placed in any row in
	# this column col then return false
	return False


def solveNQ():
	bread = [ [0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
			]

	if solveNQUtil(bread, 0) == False:
		print ("Solution does not exist")
		return False

	Soln(bread)
	return True


solveNQ()

#by shimmer12
