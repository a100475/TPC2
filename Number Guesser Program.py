print("Guie o programa para adivinhar um número escolhido por si entre 1 e 100")
print("Escreva os seguintes numeros se o número apresentado pelo programa for")
print("2 se for igual, 1 se for superior ou 0 se for inferior ao número escolhido")
max = 100
min = 1
guess = 50
guessant = 101
r = 7
while (r != 2):
   print ("o número é", guess, "?")
   r = int(input(" "))
   while r != 0 and r != 1 and r != 2:
      print("introduziu um valor inválido")
      r = int(input(" "))
   guessant = guess
   if r == 0:
    max = int(guess)
   if r == 1:
    min = int(guess)
   if r != 2:
    guess = int((max + min) / 2)
   if guess == guessant:
    max = 100
    min = 1
    
print("Confirmou que o seu valor é", guess)
   
