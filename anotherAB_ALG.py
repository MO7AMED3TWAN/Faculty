MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
	if depth == 3:
		return values[nodeIndex]

	best = MIN if maximizingPlayer else MAX
	for i in range(2):
		val = minimax(depth + 1, nodeIndex * 2 + i, not maximizingPlayer, values, alpha, beta)
		best = max(best, val) if maximizingPlayer else min(best, val)
		alpha = max(alpha, best)
		if beta <= alpha:
			break
    
	return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))