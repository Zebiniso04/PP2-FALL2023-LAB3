import re
with open('row.txt','r', encoding='utf-8') as text:
    data = text.read()
# assignment 1
pattern = r'а*б*'
matches = re.findall(pattern, data)
matches = [match for match in matches if match.strip()]

for i in matches:
    print(i,end = ' ') 
# assignment 2
pattern = r'а*б{2,3}'
matches = re.findall(pattern, data)
matches = [match for match in matches if match.strip()]
for i in matches:
    print(i,end=' ') 
# assignment 3
pattern = r'[а-я]+_[а-я]+'
matches = re.findall(pattern, data)
matches = [match for match in matches if match.strip()]
for i in matches:
    print(i, end=' ') 
# assignment 4
pattern = r'[А-Я]{1}[а-я]+'
matches = re.findall(pattern, data, re.MULTILINE | re.DOTALL)
matches = [match for match in matches if match.strip()]
for i in matches:
    print(i,end=', ') 
# assignment 5
pattern = r'^а.*б$'
matches = re.findall(pattern, data, re.MULTILINE | re.DOTALL)
matches = [match for match in matches if match.strip()]
for i in matches:
    print(i, end=' ')   
# assignment 6 
datam = re.sub(r' ', ';', data)
print(datam)  
# assignment 7
pattern = r'_(\w)'
uppered = re.sub(pattern, lambda x: x.group(0).upper(), data)

res = re.sub(r'_','',uppered)
print(res)
# assignment 8
split_data = re.split(r'[А-Я]', data)
print(split_data) 
# assignment 9
result = re.sub(r'([а-я])([А-Я])',r'\1 \2', data)
print(result) 
# assignment 10
def camelToSnake(data):
    words = re.findall(r'[А-Я][а-я]*', data)
    return '_'.join(word.lower() for word in words)
res = camelToSnake(data)
print(res) 