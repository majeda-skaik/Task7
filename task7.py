#Q1
my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict[f"{'name'}"])
my_dict["age"]=32
my_dict.update({"workplace":"GSG"})
print(my_dict)

#Q2
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
new_dict=dict(my_tuple)
dict = {}
for k, v in new_dict.items():
    dict[v] = k
print(dict)

#Q3
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
my_dic={**dic1,**dic2, **dic3}
print(my_dic)
#ِAnother answer
new_dict={}
for d in [dic1,dic2,dic3]:
    new_dict.update(d)
print(new_dict)
#Q4
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
val=my_dict.values()
print("Maximum Value:",max(val))
print("Maximum Value:",min(val))
#Q5
my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
print("ID"in my_dict.keys())
#Q6
Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'], 'Market Share %': [27.99, 15.9, 9.36, 6.67]}
output = []
for i in range(len(Languages2023['Programming Language'])):
    language = Languages2023['Programming Language'][i]
    market_share = Languages2023['Market Share %'][i]
    language_dict = {'Programming Language': language, 'Market Share %': market_share}
    output.append(language_dict)
print(output)
