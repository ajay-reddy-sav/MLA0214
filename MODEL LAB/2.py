import numpy as np

data = np.array([
    ['Old','High','Severe','Yes'],
    ['Middle','Low','Moderate','Yes'],
    ['Young','Mild','No','No'],
    ['Middle','Low','Mild','No']
])

X = data[:, :-1]
y = data[:, -1]

S = ['0'] * len(X[0])
G = [['?'] * len(X[0])]

for i in range(len(X)):
    if y[i] == 'Yes':
        for j in range(len(S)):
            if S[j] == '0':
                S[j] = X[i][j]
            elif S[j] != X[i][j]:
                S[j] = '?'
        G = [g for g in G if all(g[j] == '?' or g[j] == S[j] for j in range(len(S)))]
    else:
        new_G = []
        for g in G:
            for j in range(len(S)):
                if g[j] == '?':
                    if S[j] != X[i][j]:
                        new_h = g.copy()
                        new_h[j] = S[j]
                        new_G.append(new_h)
        G = new_G

print("S:", S)
print("G:", G)