fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits[1] = 'blueberry'
fruits.remove('cherry')
print(fruits)

coordinates = (10, 20, 30)
print(coordinates[0])

fruits_set = {'apple', 'banana', 'cherry'}
fruits_set.add('orange')
fruits_set.add('apple')
print(fruits_set)

student = {'name': 'John Doe', 'age': 22, 'major': 'Computer Science'}
student['graduation_year'] = 2023
del student['age']
print(student)

X = [[1,2],[3,4],[5,6]]
y = [0,1,0]
print("Fitur:", X)
print("Label:", y)

model_params = {'weights':[0.5,-0.2],'bias':0.1}
print(model_params['weights'])
print(model_params['bias'])
model_params['bias']=0.2
print(model_params)
