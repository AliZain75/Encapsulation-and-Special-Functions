class myClass:
 __privateVar = 27; 
 def __privMeth(self):
  print("I am inside my class myClass")
 def hellow(self):
  print("Pravit Varible value: ", myClass.__privateVar)
foo = myClass()
foo.hellow()
foo.__privMeth
