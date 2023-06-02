
import math
import sympy
from math import asin
from math import acos
from math import sqrt
import re


def solve_trig_equation(equation, variable):
    expr = sympy.sympify(equation)
    if "sqrt" in str(expr):
        expr = sympy.nsimplify(expr)
    solutions = sympy.solve(expr, variable)
    return solutions

equation = input("Entrez l'équation à resoudre: ")
variable = sympy.Symbol('x')
solutions = solve_trig_equation(equation, variable)

S = []
Solu = []

Solutions_possibles =[]

parts = equation.split("*x")
if len(parts) == 2:
  coefficient = parts[0].strip() 
  num_x = int(coefficient)
else:
  num_x = 1
for i in range(len(solutions)):
    solutions[i] = str(solutions[i]).replace("pi", "math.pi")
#print(solutions)

for i in solutions:  
  expression = i # test avec sin(3*x+pi/4)-1/2
  
  # evaluation//pour sympy
  valeur = eval(expression)
  
  # denominateur pour graphique
  denominateur = None
  if '/' in expression:
      denominateur = int(re.findall('\d+', expression.split('/')[1])[0])
  print(denominateur)
  for k in range(100):
      x = valeur + ((2 * k * math.pi) / num_x)
      if -math.pi <= x <= math.pi:
          S.append(x)
  
  for k in range(-1, -110, -1):
      x = valeur + ((2 * k * math.pi) /num_x)
      if -math.pi <= x <= math.pi:
          S.append(x)
  #print(S)
  S.sort()
  #print(S)

if denominateur is not None:
      for i in S:
          i = i * denominateur / math.pi
          Solu.append(f"{round(i)}𝝅/{denominateur}")
else:
      for i in S:
          Solu.append(str(i))

for i in range(len(solutions)):
  solutions[i] = str(solutions[i]).replace("math.pi", "𝝅")


#print(f"\nVos deux resultat d'équation à varier sont : {solutions[0]} et {solutions[1]}")

"""
if denominateur == None:
  print(f"\nVos deux resultat d'équation à varier sont : {solutions[0]} + 2k𝝅 et {solutions[1]}+ 2k𝝅 ")
else:
    for i in range(len(equation)):
      if equation[i] =="x":
        deno = equation[i-2:i-1]
    print(f"\nVos deux resultat d'équation à varier sont : {solutions[0]} + 2k𝝅/{deno} et {solutions[1]}+ 2k𝝅/{deno} ")
"""

resulist =[]
for element in Solu:
    if element not in resulist:
        resulist.append(element)
print(f"\nVous avez {len(resulist)} solutions pour l'équation {equation}, les voici (dans l'ordre croissant): \n")
n = 1
for i in resulist:
  print(f"Solution n°{n}: {i}")
  n += 1


# TODO 1h03 : prendre en charge les sqrt --> Resultat 2h30 > test avec cos(x)-sqrt(3)/2
# > cos(4*x-(pi/2)) - sqrt(3)/2

# Suite → application apk

def test():
  equation = "2*x+5= 10"
  
  # Séparer l'expression en utilisant "*x" comme délimiteur
  parts = equation.split("*x")
  coefficient = parts[0].strip() 
  num_x = int(coefficient)
  print(num_x)
     

test()