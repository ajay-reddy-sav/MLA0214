from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

data = [
    ['Old','High','Severe','Yes'],
    ['Middle','Low','Moderate','Yes'],
    ['Young','Mild','No','No'],
    ['Middle','Low','Mild','No']
]

X = [row[:-1] for row in data]
y = [row[-1] for row in data]

encoders = []
for i in range(len(X[0])):
    le = LabelEncoder()
    col = [row[i] for row in X]
    le.fit(col)
    for j in range(len(X)):
        X[j][i] = le.transform([X[j][i]])[0]
    encoders.append(le)

le_y = LabelEncoder()
y = le_y.fit_transform(y)

model = GaussianNB()
model.fit(X, y)

test = ['Old','Low','Moderate']
for i in range(len(test)):
    test[i] = encoders[i].transform([test[i]])[0]

pred = model.predict([test])
prob = model.predict_proba([test])

print(pred)
print(prob)