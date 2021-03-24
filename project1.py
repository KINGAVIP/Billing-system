import random
import string
if __name__ == '__main__':
    raa = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=10))

    # print result
    print("The generated random string : " + str(raa))
    #raa = random.randrange(10000)
    #print(raa)
#    print(''.join(random.choice(raa) for i in range(10)))
    sum=0
    count=0
    C=True
    k=[]
    while C:
        a=float(input("ENTER THE AMOUNT:"))
        sum+=a

        with open(f'{raa}.txt','a') as f:
            k.append(a)
            r=f.write(str(a))

        if a==0:
           print("Checkout")
           C=False

           print("Okay sir thanks for the shopping ,Your amount is :",sum)
           with open(f'{raa}.txt','r') as f:
               for i in range(count):
                print(f"item{i}:",k[i])

        else:
            C=True
            count+=1
            print("order so far",sum)

