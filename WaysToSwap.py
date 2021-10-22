a = 5
b = 10

print('Original values')
print('a = ', a, ' b = ', b)

#Method 1
#using temp variable

temp = a
a = b
b = temp

print('Using temp variable')
print('a = ', a, ' b = ', b)

#Method 2
#using addition & subtraction

a = a + b
b = a - b
a = a - b

print('Using Add & Sub')
print('a = ', a, ' b = ', b)


#Method 3
#using xor

a = a ^ b
b = a ^ b
a = a ^ b

print('Using xor')
print('a = ', a, ' b = ', b)

#Method 4
#simple construct
a, b = b, a

print('Using python construct')
print('a = ', a, ' b = ', b)

#Method 5
#using multiplication & division

a = a * b
b = a / b
a = a / b

print('Using mult & div')
print('a = ', a, ' b = ', b)
