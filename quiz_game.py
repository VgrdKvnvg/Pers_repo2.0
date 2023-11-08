print("Velkommen til min data quiz!")

playing = input("Vil du spille? ")

if playing.lower() != "ja":
    quit()

print("Hefti! La oss spille:)")
Score = 0

Svar = input("Hva betyr CPU? ").lower()
if Svar == "central processing unit":
    print("Riktig! ")
    Score += 1
else:
    print("Feil!")

Svar = input("Hva betyr gpu? ")
if Svar.lower() == "graphics processing unit":
    print("Riktig! ")
    Score = Score + 1
else:
    print("Feil!")

Svar = input("Hva er hovedstaden i USA? ")
if Svar.lower() == "washington dc":
    print("Riktig! ")
    Score += 1
else:
    print("Feil!")

Svar = input("Hvem er konge i Norge? ")
if Svar.lower() == "kong harald":
    print("Riktig! ")
    Score += 1
else:
    print("Feil!")

print("Du fikk", Score,"poeng, av totalt 4 mulige poeng.")

print("Du svarte riktig på", (Score/4*100),"%" " av oppgavene!")
