#!/usr/bin/env python3

a={}
a['name'] = 'Brady'
b=[]

try:
	print('hello')
	print(a['name'])
	print(b[0])
	print('string3')
except KeyError as e:
	print('There was a key exception for reason  "%s"' % e)
except IndexError as e:
	print('There was an index exception for reason "%s"' % e)

print('The End')