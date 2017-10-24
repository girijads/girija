fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"

for letter in 'Python':     # First Example
   if letter == 'n':
      break
   print 'Current Letter :', letter
  
var = 10                           # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 0:
      break

print "Good bye!"

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      continue

print "Good bye!"
