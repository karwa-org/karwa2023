"""
Première idée: travailler avec des tableaux de ce type :

+--+--+--+--+-------+--+--+--+--+--+--+
|  |  |  |  | test  |  |  |  |  |  |  |
|  |  |  |  | test2 |  |  |  |  |  |  |
+--+--+--+--+-------+--+--+--+--+--+--+
|  |  |  |  | test1 |  |  |  |  |  |  |
|  |  |  |  | test2 |  |  |  |  |  |  |
+--+--+--+--+-------+--+--+--+--+--+--+

+--+--+--+--+------------+--+--+--+--+--+--+
|  |  |  |  | test test2 |  |  |  |  |  |  |
+--+--+--+--+------------+--+--+--+--+--+--+
|  |  |  |  | test1      |  |  |  |  |  |  |
|  |  |  |  | test2      |  |  |  |  |  |  |
+--+--+--+--+------------+--+--+--+--+--+--+

Et regarder un problème d'optimisation pour minimiser la taille totale.
Le problème est peut-être un peu trop dur, donc idée abandonnée.

À la place : récupérer la plus grande sous-matrice d'une matrice binaire.
Dynamic Programming : considérer les sous-matrices. Pour un point (i,j), on
garde en mémoire :
- le nombre de 1 au-dessus du point, noté height[j]
- l'indice le plus à gauche sur la ligne i, noté left[j], tel que de
  left[i] à j, on a un rectangle de 1 d'une hauteur height[j]
- l'indice le plus à droite sur la ligne i, noté right[j], tel que de
  j à right[i], on a un rectangle de 1 d'une hauteur height[j]

=> la hauteur du sous-rectangle est height[j] * (right[j]-left[j])

Si on voit un 1, on réinitialise left[j] à 0, right[j] à cols (nbrs de colonnes)
et ça n'impacte pas les calculs car height[j] vaudra de toute façon 0.

"""


def maximal_rectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])
    height = [0] * cols
    left, right = [0] * cols, [cols] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            height[j] = height[j]+1 if matrix[i][j] == 1 else 0

        cur_left = 0
        for j in range(cols):
            left[j], cur_left = (max(left[j], cur_left), cur_left) if matrix[i][j] == 1 else (0, j+1)

        cur_right = cols
        for j in range(cols-1, -1, -1):
            right[j], cur_right = (min(right[j], cur_right), cur_right) if matrix[i][j] == 1 else (cols, j)

        for j in range(cols):
            max_area = max(max_area, height[j] * (right[j]-left[j]))

    return max_area


def maximal_rectangle_naive(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_area = 0

    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if all(matrix[row][col] for row in range(top, bottom+1) for col in range(left, right+1)):
                        area = (bottom-top+1)*(right-left+1)
                        max_area = max(max_area, area)

    return max_area


tests = []
m = [[1,0,1,0,1],
     [0,1,0,1,0],
     [1,0,1,1,1],
     [0,0,1,1,1]]
tests.append(m)
m = [[1]*1000]*10000
m[20][21]=0
tests.append(m)
m = [[1,0,1,0,1],
     [0,1,0,1,0],
     [1,0,1,1,1]]
tests.append(m)
tests.append([[1,1]])
tests.append([[1],[0],[1],[1],[1]])

# 1000x1000 avec ligne de 1 sur la colonne 21 (22ème) : 978000.
# 1000x1000 avec 1 sur [20][21]


for m in tests:
    #print(f"Matrix size {len(m)}x{len(m[0])} : optimal algorithm {maximal_rectangle(m)}, naive algorithm : {maximal_rectangle_naive(m)}.")
    print(f"Matrix size {len(m)}x{len(m[0])} : optimal algorithm {maximal_rectangle(m)}.")
    print('-'*10)