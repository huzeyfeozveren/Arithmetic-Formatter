def solution(x,y,operation):
  if operation == "+":
    return x + y
  elif operation == "-":
    return x - y

def arithmetic_arranger(problems,answer = False):
  first=[]
  second=[]
  dash=[]
  fourth=[]
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    elements = problem.split(" ")
    if not (elements[0]+elements[2]).isdigit():
      return "Error: Numbers must only contain digits."
    elif len(elements[0]) > 4 or len(elements[2]) > 4:
      return "Error: Numbers cannot be more than four digits." 
    elif True:
      if elements[1] == "-":
        pass
      elif elements[1] == "+":
        pass
      else:
        return "Error: Operator must be '+' or '-'."
    
  
  for problem in problems:
    elements = problem.split(" ")
    final = solution(int(elements[0]),int(elements[2]),elements[1])
    width = max([len(i) for i in elements]) + 2
    first   += ["{:>{}}".format(elements[0],width)]
    second  += ["{}{:>{}}".format(elements[1],elements[2],width-1)]
    dash    += ["{:>{}}".format(width*"-",width)]
    fourth  += ["{:>{}}".format(final,width)]
  arranged_problems = "    ".join(first) + "\n" + "    ".join(second) + "\n" + "    ".join(dash)
  if answer == True:
    return arranged_problems + "\n" + "    ".join(fourth)
  else:
    return arranged_problems
