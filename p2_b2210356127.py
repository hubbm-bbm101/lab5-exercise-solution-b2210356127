email = input("enter your email please: ")
def checker(email):
  at=None
  dot=None
  for word in email:
    if word == "@":
      at=True
  for word in email:
    if word==".":
      dot=True
  if at and dot == True:
      print("Congrats! Your email is valid.")
  else:
      print("Oops! Your email is not valid.")

checker(email)
