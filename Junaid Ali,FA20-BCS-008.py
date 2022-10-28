#!/usr/bin/env python
# coding: utf-8

# In[1]:



row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]



def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))            and not processed[x][y]



def searchBoggle(board, words, result, processed, i, j, path=''):

    processed[i][j] = True


    path += board[i][j]


    if path in words:
        result.add(path)


    for k in range(len(row)):

        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)

    processed[i][j] = False


def searchInBoggle(board, words):

    result = set()


    if not board or not len(board):
        return


    (M, N) = (len(board), len(board[0]))


    processed = [[False for x in range(N)] for y in range(M)]


    for i in range(M):
        for j in range(N):

            searchBoggle(board, words, result, processed, i, j)

    return result


if __name__ == '__main__':
    board = [
        ['M', 'S', 'E', 'F'],
        ['R', 'A', 'T', 'D'],
        ['L', 'O', 'N', 'E'],
        ['k', 'A', 'F', 'B']
    ]

    words = ['NOTE', 'SAND', 'STONE']

    validWords = searchInBoggle(board, words)
    print(validWords)


# In[2]:


d = {
         'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
         'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
         'Timisoara': [('Arad', 118), ('Lugoj', 111)],
         'Zerind': [('Arad', 75), ('Oradea', 71)],
         'Oradea': [('Zerind', 71), ('Sibiu', 151)],
         'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
         'Rimnicu': [('Sibiu', 80), ('Craivo', 146), ('Pitesti', 97)],
         'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
         'Bucharest': [('Giurgiu', 90), ('Urziceni', 85), ('Pitesti', 101), ('Fagaras', 211)],
         'Craivo': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu', 146)],
         'Pitesti': [('Rimnicu', 97), ('Craivo', 138), ('Bucharest', 101)],
         'Mehadia': [('Dobreta', 75), ('Lugoj', 70)],
         'Giurgiu': [('Bucharest', 90)],
         'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
         'Dobreta': [('Mehadia', 75), ('Craivo', 120)],
         'Hirsova' : [('Eforie', 86), ('Urziceni', 98)],
         'Vaslui' : [('Urziceni', 142), ('Lasi', 92)],
         'Eforie' : [('Hirsova', 86)],
         'Lasi': [('Neamt', 87), ('Vaslui', 92)],
         'Neamt': [('Lasi', 87)],
}

total_nodes = list(d.keys())

total_nodes

h_n_ = {
         'Arad': 366,
         'Sibiu':  253,
         'Timisoara': 329,
         'Zerind': 374,
         'Oradea': 380,
         'Fagaras': 178,
         'Rimnicu': 193,
         'Lugoj': 244,
         'Bucharest': 0,
         'Craivo': 160,
         'Pitesti': 98,
         'Mehadia': 241,
         'Giurgiu': 77,
         'Urziceni': 80,
         'Dobreta': 242,
         'Hirsova' : 151,
         'Vaslui' : 199,
         'Eforie' : 161,
         'Lasi': 226,
         'Neamt': 234
}



def my(x):
    return x[1]

def build_dcit(lis):
    di  = {}

    for i in lis:
        name = i[0]
        cost = i[1]
        di[name] = cost
    return di

def GBFS(start,goal):
    
    q = []
    start_val = h_n_.get(start)
    q.append((start,start_val))
    explored = []
    expanded = []
    
    while len(q)>0:


        node = q.pop(0)

        if node[0] not in explored:
            explored.append(node[0])
        
        if node[0] == goal:
            print('Result :',explored,expanded,len(expanded))
            return

        child = d.get(node[0])
 
        for i in child:
            n_key = i[0]
            n_val = (h_n_.get(n_key))+i[1]
            n_tuple = n_key,n_val

            if i[0] not in explored and i[0] not in build_dcit(q):
                q.append(n_tuple)
        expanded.append(node[0])
            
        q = sorted(q,key= my)
    return explored,expanded,len(expanded)
        
    
GBFS('Arad','Bucharest')


# In[ ]:




