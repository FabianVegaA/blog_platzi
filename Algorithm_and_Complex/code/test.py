def function1(): 
  result = -3 
  assert result > 0, "Error with {0}".format (result) 
 
def function2(): 
  result = -3 
  if result > 0 : 
    raise ValueError ("Error with {0}".format (result))