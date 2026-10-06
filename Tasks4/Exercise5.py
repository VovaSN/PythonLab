def checkCharacter(c):
   assert len(c) == 1, "Only 1 character available"

   c = c.lower()
   vowels = "аеёиоуыэюяaeiou"
   
   if c in vowels:
      return "Vowels"
   elif c.isalpha():
      return "Consonant"
   else:
      return "Other character"

while True:
   ans = input("Enter one character:")
   print(f"{ans} is {checkCharacter(ans)}")    