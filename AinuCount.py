import math

counters=["","sine","tu","re","ine","asikne","iwan","arwan","tupesan","sinepesan","wan"]
numbers=["","sinep","tup","rep","inep","asik","iwan","arwan","tupes","sinepes","wanpe"]

def countType():
    while True:
        x = input("(n)umber or (c)ounter? :")
        if x=="n":
            return "number"
        if x=="c":
            return "counter"
        print("Please type n or c.")

def counterThing():
    while True:
        x = input("(t)hings in general, (p)ersons, or (o)thers? :")
        if x=="t":
            return "things"
        if x=="p":
            return "persons"
        if x=="o":
            return "others"
        print("Please type t, p, or o.")

def thingName():
    x = input("Input your words :")
    return x

def countNumber():
    while True:
        x = input("Input your count number (1-200) :")
        try:
            val = int(x)
            if val > 0 and val <= 200:
                return val
            else:
                print("Please input an integers between 1 and 200.")
        except ValueError:
            print("Please input an integers between 1 and 200.")

def numberWords(num,kind,word):
    if kind=="number":
        if num>0 and num<=10:
            return numbers[num]
        if num==20:
            return "hot"
    if kind=="others":
        if num>0 and num<=10:
            return counters[num]+" "+word
        if num==20:
            return "hotne"+" "+word
    if kind=="things":
        if num>0 and num<=5:
            return counters[num]+"-p"
        if num>5 and num<=10:
            return counters[num]+"-pe"
        if num==20:
            return "hotne"+"-p"
    if kind=="persons":
        if num>0 and num<=5:
            return counters[num]+"-n"
        if num>5 and num<=10:
            return counters[num]+"-iw"
        if num==20:
            return "hotne"+"-n"

    return counters[num]

def numberStrings(num,kind,word):
    if kind=="number" and num==10:
        return "to"
    z=""
    if num%10!=0:
        z+=numberWords(num%10,kind,word)
        if num>10:
            z+=" ikasma "
        else:
            return z
    tmp=int(num/10)
    if tmp==2:
        z+=numberWords(20,kind,word)
    elif tmp%2==0:
        z+=numberWords(int(tmp/2),"","")+"-"+numberWords(20,kind,word)
    elif tmp==1:
        z+=numberWords(10,kind,word)
    elif (tmp+1)%2==0:
        z+=numberWords(10,kind,word)+" e-"+numberWords(int(tmp/2)+1,"","")+"-"+numberWords(20,kind,word)
    return z

def cli_main():
    kind="number"
    word=""
    num=1
    kind = countType()
    if kind=="counter":
        kind = counterThing()
        if kind=="others":
            word = thingName()
    num = countNumber()
    print(numberStrings(num,kind,word))

if __name__ == "__main__":
    cli_main()
