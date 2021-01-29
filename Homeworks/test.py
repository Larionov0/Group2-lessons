trees = [
    ["Дуб", 5 , "д", "Д", 1, 
     [],
     0
     ],
    ["Береза", 3, "б", "Б", 3,
     [],
     0
     ],
    ["Сосна", 1, "с", "С", 4, 
     [],
     0
     ]
    ]

width = 6
height = 6

# матриця
matrix = []
i = 0
while i < height:
    row = ['-'] * width
    matrix.append(row)
    i += 1
for row in matrix:
        row_text = '|'
        for element in row:
            row_text += str(element) + ' '
        row_text = row_text[:-1] + '|'
        print(row_text)

# геймплей
while True:
    # хід гравця
    skip = input('Skip? так/ні: ')
    
    if skip == 'ні':
        x = int(input('x: '))
        y = int(input('y: '))
        tree = input('tree: ')

        for el in trees:
            if el[0] == tree and el[4] != 0:
                treeInfo = []
                treeChar = el[2]
                treeMadeMoves = 0
                treeX = x
                treeY = y
                treeInfo.append(treeChar)
                treeInfo.append(treeMadeMoves)
                treeInfo.append(treeX)
                treeInfo.append(treeY)
                el[5].append(treeInfo)
                el[6] += 1
                el[4] -= 1

    # ріст дерев
    for el in trees:
        for tree in el[5]:
            if tree[1] == el[1]:
                tree[0] = el[3]
            tree[1] += 1

    print(trees)
    for el in trees:
        for tree in el[5]:
            matrix[tree[3]-1][tree[2]-1] = tree[0]
            
    # формування матриці
    for row in matrix:
        row_text = '|'
        for element in row:
            row_text += str(element) + ' '
        row_text = row_text[:-1] + '|'
        print(row_text)
