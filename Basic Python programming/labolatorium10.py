#Mateusz Blazejczyk

#zad 2
lista = []
def linia_po_lini(nazwa_pliku):
 txt = open(nazwa_pliku).readlines()
 for i in range(len(txt)):
  print(txt[i])


linia_po_lini('text1.txt')





#zad 3
def plik_do_plik(nazwa_pliku):
 txt = open(nazwa_pliku).read()
 with open('text2.txt', 'x') as f:
  f.write(txt)


plik_do_plik('text1.txt')




#zad 4
def plik_do_listy(nazwa_pliku):
 txt = open(nazwa_pliku).read()
 txt2 = txt.split(' ')

 txt3 = []
 for i in range(len(txt2)):
  temp = txt2[i].split('\n')
  for j in range(len(temp)):
   txt3.append(temp[j])

 longestId = 0
 longest = 0
 for i in range(len(txt3)):
  if len(txt3[i]) > longest:
   longest = len(txt3[i])
   longestId = i

 print(txt3[longestId])


plik_do_listy('text1.txt')




#zad 5
def liczbaslow(nazwa_pliku):
 txt = open(nazwa_pliku).read()
 txt2 = txt.split(' ')
 otp = []
 amm = []
 for i in range(len(txt2)):
  id = -1
  for j in range(len(otp)):
   if txt2[i] == otp[j]:
    id = j
    break
  if id == -1:
   otp.append(txt2[i])
   amm.append(1)
  else:
   amm[id] += 1

 for i in range(len(otp)):
  print('slowo: ' + otp[i].__str__() + " w ilosci " + amm[i].__str__())


liczbaslow('text3.txt')





#zad 6
import random


def losowe_slowa(nazwa_pliku):
 txt = open(nazwa_pliku).read()
 txt2 = txt.split(' ')

 txt3 = []
 for i in range(len(txt2)):
  temp = txt2[i].split('\n')
  for j in range(len(temp)):
   txt3.append(temp[j])

 for i in range(10):
  print(txt3[random.randint(0, len(txt3))])


losowe_slowa('text1.txt')





#zad 7
def ostatnie_wiersze(nazwa_pliku, ile):
 txt = open(nazwa_pliku).readlines()

 for i in reversed(range(ile)):
  print(txt[len(txt) - i - 1])


ostatnie_wiersze('text1.txt', 5)





#zad 8
def nazmiane(nazwa_pliku1, nazwa_pliku2):
 txt1 = open(nazwa_pliku1).readlines()
 txt2 = open(nazwa_pliku2).readlines()
 txt3 = []
 krotszy = 0
 ktory = 0
 if len(txt1) > len(txt2):
  krotszy = len(txt2)
  ktory = 2
 else:
  krotszy = len(txt1)
  ktory = 1

 for i in range(krotszy):
  txt3.append(txt1[i])
  txt3.append(txt2[i])


 if ktory == 2:
  while krotszy < len(txt1):
   txt3.append(txt1[krotszy])
   krotszy += 1
 else:
  while krotszy < len(txt2):
   txt3.append(txt2[krotszy])
   krotszy += 1

 output = ""
 for i in range(len(txt3)):
  output += txt3[i]
 with open('zad8.txt', 'x') as f:
  f.write(output)


nazmiane('text1.txt', 'text3.txt')





#zad 9
def bezspacji(nazwa_pliku):
 txt = open(nazwa_pliku).read()
 txt2 = txt.split(' ')

 txt3 = ""
 for i in range(len(txt2)):
  txt3 += txt2[i]

 with open('bez_spacji.txt', 'x') as f:
  f.write(txt3)




bezspacji('text1.txt')
