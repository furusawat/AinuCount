dic=[["a","ア","а"],
        ["i","イ","и"],
        ["u","ウ","у"],
        ["e","エ","э"],
        ["o","オ","о"],
        ["k ","ㇰ","к "],
        ["ka","カ","ка"],
        ["ki","キ","ки"],
        ["ku","ク","ку"],
        ["ke","ケ","кэ"],
        ["ko","コ","ко"],
        ["s ","ㇱ","с "],
        ["sa","サ","са"],
        ["si","シ","си"],
        ["su","ス","су"],
        ["se","セ","сэ"],
        ["so","ソ","со"],
        ["t ","ッ","т "],
        ["ta","タ","та"],
        ["tu","トゥ","ту"],
        ["te","テ","тэ"],
        ["to","ト","то"],
        ["ca","チャ","ча"],
        ["ci","チ","чи"],
        ["cu","チュ","чу"],
        ["ce","チェ","че"],
        ["co","チョ","чо"],
        ["n ","ン","н "],
        ["na","ナ","на"],
        ["ni","ニ","ни"],
        ["nu","ヌ","ну"],
        ["ne","ネ","нэ"],
        ["no","ノ","но"],
        ["ha","ハ","ха"],
        ["hi","ヒ","хи"],
        ["hu","フ","ху"],
        ["he","ヘ","хэ"],
        ["ho","ホ","хо"],
        ["p ","ㇷ゚","п "],
        ["pa","パ","па"],
        ["pi","ピ","пи"],
        ["pu","プ","пу"],
        ["pe","ペ","пэ"],
        ["po","ポ","по"],
        ["m ","ㇺ","м "],
        ["ma","マ","ма"],
        ["mi","ミ","ми"],
        ["mu","ム","му"],
        ["me","メ","мэ"],
        ["mo","モ","мо"],
        ["y ","イ","й "],
        ["ya","ヤ","я"],
        ["yu","ユ","ю"],
        ["ye","イェ","е"],
        ["yo","ヨ","ё"],
        ["r ","ㇽ","р "],
        ["ra","ラ","ра"],
        ["ri","リ","ри"],
        ["ru","ル","ру"],
        ["re","レ","рэ"],
        ["ro","ロ","ро"],
        ["w ","ウ","в "],
        ["wa","ワ","ва"],
        ["we","ウェ","вэ"],
        ["wo","ウォ","во"]]

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
    len_tmp = len(dic)
    for i in range(len_tmp):
        if len(dic[i][src]) == 1:
            return_dic[dic[i][src]] = dic[i][tgt].strip()
        if len(dic[i][src]) == 2:
            if dic[i][src][0] not in return_dic:
                return_dic[dic[i][src][0]] = {}
            return_dic[dic[i][src][0]][dic[i][src][1]] = dic[i][tgt].strip()

    return return_dic

def letterChange(words,src,tgt):
    if src==tgt:
        return words
    result=[]
    if src=="latin":
        if tgt=="kana" or tgt=="cyrillic":
            if tgt=="kana":
                tmp_dic=dicMaker(0,1)
            elif tgt=="cyrillic":
                tmp_dic=dicMaker(0,2)
            i=0
            for k,v in soundchange.items():
                words = words.replace(k,v)
            len_tmp = len(words)
            while i < len_tmp:
                if words[i] in vowels:
                    result.append(tmp_dic[words[i]])
                elif words[i] in cons:
                    if i+1 == len_tmp or words[i+1] not in vowels:
                        if tgt=="cyrillic":
                            result.append(tmp_dic[words[i]][" "])
                        elif words[i]=="r":
                            if i<=0 or words[i-1] not in vowels:
                                result.append(r_vowels[2])
                            else:
                                result.append(r_vowels[vowels.index(words[i-1])])
                        elif i+1 < len_tmp and words[i:i+2] in ["pp","kk","ss"]:
                                result.append(tmp_dic["t"][" "])
                        elif i+1 < len_tmp and words[i:i+2] in ["mm","mp"]:
                                result.append(tmp_dic["n"][" "])
                        else:
                            result.append(tmp_dic[words[i]][" "])
                    else:
                        result.append(tmp_dic[words[i]][words[i+1]])
                        i+=1
                else:
                    result.append(words[i])
                i+=1

    return "".join(result)
