dic=[["a","ア",""],
        ["i","イ",""],
        ["u","ウ",""],
        ["e","エ",""],
        ["o","オ",""],
        ["k ","ㇰ",""],
        ["ka","カ",""],
        ["ki","キ",""],
        ["ku","ク",""],
        ["ke","ケ",""],
        ["ko","コ",""],
        ["s ","ㇱ",""],
        ["sa","サ",""],
        ["si","シ",""],
        ["su","ス",""],
        ["se","セ",""],
        ["so","ソ",""],
        ["t ","ッ",""],
        ["ta","タ",""],
        ["tu","トゥ",""],
        ["te","テ",""],
        ["to","ト",""],
        ["ca","チャ",""],
        ["ci","チ",""],
        ["cu","チュ",""],
        ["ce","チェ",""],
        ["co","チョ",""],
        ["n ","ン",""],
        ["na","ナ",""],
        ["ni","ニ",""],
        ["nu","ヌ",""],
        ["ne","ネ",""],
        ["no","ノ",""],
        ["ha","ハ",""],
        ["hi","ヒ",""],
        ["hu","フ",""],
        ["he","ヘ",""],
        ["ho","ホ",""],
        ["p ","ㇷ゚",""],
        ["pa","パ",""],
        ["pi","ピ",""],
        ["pu","プ",""],
        ["pe","ペ",""],
        ["po","ポ",""],
        ["m ","ㇺ",""],
        ["ma","マ",""],
        ["mi","ミ",""],
        ["mu","ム",""],
        ["me","メ",""],
        ["mo","モ",""],
        ["y ","イ",""],
        ["ya","ヤ",""],
        ["yu","ユ",""],
        ["ye","イェ",""],
        ["yo","ヨ",""],
        ["ra","ラ",""],
        ["ri","リ",""],
        ["ru","ル",""],
        ["re","レ",""],
        ["ro","ロ",""],
        ["w ","ウ",""],
        ["wa","ワ",""],
        ["we","ウェ",""],
        ["wo","ウォ",""]]

soundchange={"n s":"y s",
        "n y":"y y",
        "n w":"n m",
        "r t":"t t",
        "r c":"t c",
        "r n":"n n",
        "r r":"n r"}

r_vowels=["ㇻ","ㇼ","ㇽ","ㇾ","ㇿ"]

vowels=["a","i","u","e","o"]
cons=["k","s","t","c","n","h","p","m","y","r","w"]

def dicMaker(src,tgt):
    return_dic = {}
    for i in range(len(dic)):
        if len(dic[i][src]) == 1:
            return_dic[dic[i][src]] = dic[i][tgt]
        if len(dic[i][src]) == 2:
            if dic[i][src][0] not in return_dic:
                return_dic[dic[i][src][0]] = {}
            return_dic[dic[i][src][0]][dic[i][src][1]] = dic[i][tgt]

    return return_dic

def letterChange(words,src,tgt):
    if src==tgt:
        return words
    result=""
    if src=="latin":
        if tgt=="kana":
            tmp_dic=dicMaker(0,1)
            i=0
            for k,v in soundchange.items():
                words = words.replace(k,v)
            while i in range(len(words)):
                if words[i] in vowels:
                    result+=tmp_dic[words[i]]
                elif words[i] in cons:
                    if i+1 == len(words) or words[i+1] not in vowels:
                        if words[i]=="r":
                            if i<=0 or words[i-1] not in vowels:
                                result+=r_vowels[2]
                            else:
                                result+=r_vowels[vowels.index(words[i-1])]
                        elif i+1 < len(words) and words[i:i+2] in ["pp","kk"]:
                                result+=tmp_dic["t"][" "]
                        elif i+1 < len(words) and words[i:i+2] in ["mm"]:
                                result+=tmp_dic["n"][" "]
                        else:
                            result+=tmp_dic[words[i]][" "]
                    else:
                        result+=tmp_dic[words[i]][words[i+1]]
                        i+=1
                else:
                    result+=words[i]
                i+=1

    return result
