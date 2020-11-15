counters=["","sine","tu","re","ine","asikne","iwan","arwan","tupesan","sinepesan","wan"]
numbers=["","sinep","tup","rep","inep","asik","iwan","arwan","tupes","sinepes","wanpe"]

def counterThing():
    while True:
        x = input("Choose one: (n)umber, (t)hings in general, (p)ersons, (d)ays, t(i)mes, or (o)thers? :")
        if x=="n":
            return "number"
        if x=="t":
            return "things"
        if x=="p":
            return "persons"
        if x=="d":
            return "days"
        if x=="i":
            return "times"
        if x=="o":
            return "others"
        print("Please type n, t, p, d, i, or o.")

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

def dialect():
    while True:
        x = input("(s)aru, or (i)shikari? :")
        if x=="s":
            return "saru"
        if x=="i":
            return "ishikari"
        print("Please type s, or i.")

def numberWords(num,kind,word,dlct):
    if kind=="number":
        if num>0 and num<=10:
            return numbers[num]
        if num==20:
            return "hot"
    if kind=="things":
        if num>0 and num<=5:
            return counters[num]+"p"
        if num>5 and num<=10:
            return counters[num]+"pe"
        if num==20:
            if dlct=="ishikari":
                return "hot"
            return "hotnep"
    if kind=="persons":
        if num>0 and num<=5:
            return counters[num]+"n"
        if num>5 and num<=10:
            return counters[num]+"iw"
        if num==20:
            if dlct=="ishikari":
                return "hot"
            return "hotnen"

    if kind=="days":
        word="to"
        if num==2:
            return "tutko"
        if num==3:
            return "rerko"
        if num>3 and dlct=="saru":
            word="rerko"
    if kind=="times":
        word="suy"
        if num==1:
            return "arsuy"
    if num>0 and num<=10:
        return counters[num]+" "+word
    if num==20:
        if dlct=="ishikari":
            return "hot "+word
        return "hotne "+word

def numberStrings(num,kind,word,dlct):
    if kind=="number" and num==10:
        return "to"
    z=""
    if num%10!=0:
        z+=numberWords(num%10,kind,word,dlct)
        if num>10:
            z+=" ikasma "
        else:
            return z
    tmp=int(num/10)
    ten=numberWords(10,kind,word,dlct)
    twenty=numberWords(20,kind,word,dlct)

    if dlct=="ishikari":
        if tmp>9:
            if int(tmp/10)>1:
                z+=counters[int(tmp/10)]
            z+="atuyta "
        tmp=tmp%10
        if tmp==1:
            z+=ten
        elif tmp==2:
            z+=twenty
        elif tmp==0:
            if kind=="days":
                z+="to"
            elif kind=="times":
                z+="suy"
            elif kind=="others":
                z+=word
            else:
                z=z[:-1]
        else:
            z+=counters[int(tmp)]+twenty
        return z

    if tmp==2:
        z+=twenty
    elif tmp%2==0:
        z+=counters[int(tmp/2)]+twenty
    elif tmp==1:
        z+=ten
    elif (tmp+1)%2==0:
        z+=ten+" e"+counters[int(tmp/2)+1]+twenty
    return z

def cli_main():
    word=""
    kind = counterThing()
    if kind=="others":
        word = thingName()
    num = countNumber()
    dlct = dialect()
    print(numberStrings(num,kind,word,dlct))

if __name__ == "__main__":
    cli_main()
