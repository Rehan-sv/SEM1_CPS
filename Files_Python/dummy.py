data = {
    'name': ['John', 'Mary', 'Mike', 'Maggie', 'Chris', 'Laura'],
    'age': [23, 21, 25, 22, 24, 19],
}
import pickle
# f1 = open('dummy.pkl', 'wb')
# pickle.dump(data, f1)
# f1.close()

f2 = open('dummy.pkl', 'rb')
dict_input = pickle.load(f2)
print(type(dict_input['name'][0]))
print(dict_input['name'][0])
f2.close()












# f1 = open('dummy', 'w')
# f1.write(str(data))
# f1.close()
# f2 = open('dummy', 'r')
# print(f2.read())
# f2.close()
