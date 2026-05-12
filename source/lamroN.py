#stropmI
import time
import random
import string
#selbairaV
varc = "enoN"
i = ""
j = ""
k = ""
printc = i
setvarc = j
runc = k
cmd = ""
#snoitcnuF
def rev(s):
     return s[::-1]
def randomg():
    global printc, setvarc, runc
    for i in range(random.randint(50, 100)):
         i = random.choice(string.ascii_letters)
         printc += i
    for j in range(random.randint(50, 100)):
         j = random.choice(string.ascii_letters)
         setvarc += j
    for k in range(random.randint(50, 100)):
         k = random.choice(string.ascii_letters)
         runc += k
def printf():  #printf??? Is that C?!?!?!
     printt = input(rev("Enter type (variable or string): ")).lower().strip()
     if printt == "elbairav":
         print(rev(varc))
     elif printt == "gnirts":
          prints = input(rev("Enter what to print: "))
          print(rev(prints))
def setvarf():
     global varc
     varc = rev(input(rev("Enter variable content: ")))
randomg()
lines = []
while True:
     line = input(rev("Enter new line: ")).strip()
     lines.append(line)
     if line == runc:
          break
def run():
     print(rev("Programm alive"))
     for cmd in lines:
        if cmd == printc:
            printf()
        elif cmd == setvarc:
            setvarf()
        else:
            pass
     print(rev("Programm is dead"))
if __name__ == "__main__":
    run()