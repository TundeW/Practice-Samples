#Ths uses recursion to solve the Hanoi tower problem

def tower(n, source, target, spare):
    if n == 1:
        print ("move disk", n,"from", source,"to",target)
    else:
        tower(n-1, source, spare, target)
        print ("move disk", n,"from", source,"to",target)
        tower(n-1, spare, target, source)
n= input("Enter the number of disks in the Hanoi tower: ")
a= tower(int(n),"P1","P2","P3")
