try:
   print(5/0)
except ZeroDivisionError:
   print('wrong division')
except NameError:
   print('variable isnt defined')
except:
   print('wrong value')
else:
   print('No Error')

