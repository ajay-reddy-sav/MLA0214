data = [
    ['Old','High','Severe','Yes'],
    ['Middle','Low','Moderate','Yes'],
    ['Young','Mild','No','No'],
    ['Middle','Low','Mild','No']
]

hypothesis = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Yes':
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = row[i]
            elif hypothesis[i] != row[i]:
                hypothesis[i] = '?'

print(hypothesis)