name = 'Julia'
my_list = ['Julia', 2, 2.3]
print(id(name))
print(id(my_list))

def test_func(par_name, par_list):
   par_name = 'Jom'
   par_list[0] = 'Jon'
   print(id(par_name))
   print(id(par_list))
test_func(name, my_list)
print(name)
print(my_list)