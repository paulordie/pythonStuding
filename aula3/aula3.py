'''
string e aspas simples e duplas
'''
print('test')
print('alguma coisa')
print("essa é uma string (str)")
print("aspas duplas")
print('1234')
print(1234)
print('essa strint "test" testou')
print("essa strint 'test' testou")
print("essa strint \"test\" testou")
print('essa strint \'test\' testou')
print('essa strint \'test\' \ntestou')
print(r'essa strint \'test\' \ntestou')
print(r'essa strint \'test\'testou')

your_variable_pattern_str = 'test'
print(r'%s' % your_variable_pattern_str)

otherVariable = "second String"
otherVariable2 = "third String"
print(r'%s' % otherVariable,otherVariable2)

numVar1 = 123
numVar2 = 1000
print(r'%d' % numVar1, numVar2)

print(r'%s' % numVar1)