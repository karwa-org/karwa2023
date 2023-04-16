import math
import sys
sys.setrecursionlimit(int(1e6))

def minimax (nodeIndex, k, turn):
    if nodeIndex == 0:
        return -int(turn)
    if (turn):
        return max(minimax(nodeIndex - i - 1, k, False) for i in range(k) if nodeIndex - i - 1 >= 0)
    else:
        return min(minimax(nodeIndex - i - 1, k, True) for i in range(k) if nodeIndex -i - 1 >= 0)

n,k = map(int, input().split())
print("Brieuc" if not minimax(n, k, True) else "Aymeric")