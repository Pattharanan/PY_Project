# main_Modules
import Modules
import Modules as m
from Modules import draw_triangle

menu = 'Main Menu\n' + ('=' * 10) + '\n1. Sum Number\n'
menu += '2. Factorial\n3. Draw Triangle\n4. Exit\nEnter Choice: '

while True:
  choice = input(menu)

  match choice:
    case '1':
      sum = Modules.sum_number(10, 40)
      print('\nSum 10 - 40 = ', sum, '\n')
    case '2':
      fac = m.factorial(7)
      print('\nFactorial (7) = ', fac, '\n')
    case '3':
      print()
      draw_triangle('#', 6)
      print()
    case '4':
      print('Exit Program...')
      break
    case _:
      print('No choice.')