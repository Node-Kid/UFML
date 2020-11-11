import UFML

while True:
  text = input("UFML> ")
  result, error = UFML.run(text)
  if error: print (error.as_string())
  else: print(result)
