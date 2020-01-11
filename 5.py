import random
"""a=input("randomize= ")
b=int(a)
for x in range(b):
    print(random.randint(1,10))"""


'''d=str(c)
    e=d.split()
    for i in range(len(e)):
       e[i]=e[i].split(',')
       print'''

  
def main():
    a=input("randomize= ")
    b=int(a)
    x = 0
    for sum in range(b):
        randnums = random.randint(1,10)
        x = x + randnums 
        print(randnums, end=',')
    print("sum= ",x)

main()
