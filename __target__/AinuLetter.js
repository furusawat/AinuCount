'use strict';import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,__ipow__,
__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__proxy__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,
format,getattr,hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";var __name__="AinuLetter";export var dic=[["a","\u30a2",""],["i","\u30a4",""],["u","\u30a6",""],["e","\u30a8",""],["o","\u30aa",""],["k ","\u31f0",""],["ka","\u30ab",""],["ki","\u30ad",""],["ku","\u30af",""],["ke","\u30b1",""],["ko","\u30b3",
""],["s ","\u31f1",""],["sa","\u30b5",""],["si","\u30b7",""],["su","\u30b9",""],["se","\u30bb",""],["so","\u30bd",""],["t ","\u30c3",""],["ta","\u30bf",""],["tu","\u30c8\u30a5",""],["te","\u30c6",""],["to","\u30c8",""],["ca","\u30c1\u30e3",""],["ci","\u30c1",""],["cu","\u30c1\u30e5",""],["ce","\u30c1\u30a7",""],["co","\u30c1\u30e7",""],["n ","\u30f3",""],["na","\u30ca",""],["ni","\u30cb",""],["nu","\u30cc",""],["ne","\u30cd",""],["no","\u30ce",""],["ha","\u30cf",""],["hi","\u30d2",""],["hu","\u30d5",
""],["he","\u30d8",""],["ho","\u30db",""],["p ","\u31f7\u309a",""],["pa","\u30d1",""],["pi","\u30d4",""],["pu","\u30d7",""],["pe","\u30da",""],["po","\u30dd",""],["m ","\u31fa",""],["ma","\u30de",""],["mi","\u30df",""],["mu","\u30e0",""],["me","\u30e1",""],["mo","\u30e2",""],["y ","\u30a4",""],["ya","\u30e4",""],["yu","\u30e6",""],["ye","\u30a4\u30a7",""],["yo","\u30e8",""],["ra","\u30e9",""],["ri","\u30ea",""],["ru","\u30eb",""],["re","\u30ec",""],["ro","\u30ed",""],["w ","\u30a6",""],["wa","\u30ef",
""],["we","\u30a6\u30a7",""],["wo","\u30a6\u30a9",""]];export var soundchange=dict({"n s":"y s","n y":"y y","n w":"n m","r t":"t t","r c":"t c","r n":"n n","r r":"n r"});export var r_vowels=["\u31fb","\u31fc","\u31fd","\u31fe","\u31ff"];export var vowels=["a","i","u","e","o"];export var cons=["k","s","t","c","n","h","p","m","y","r","w"];export var dicMaker=function(src,tgt){var return_dic=dict({});var len_tmp=len(dic);for(var i=0;i<len_tmp;i++){if(len(dic[i][src])==1)return_dic[dic[i][src]]=dic[i][tgt];
if(len(dic[i][src])==2){if(!__in__(dic[i][src][0],return_dic))return_dic[dic[i][src][0]]=dict({});return_dic[dic[i][src][0]][dic[i][src][1]]=dic[i][tgt]}}return return_dic};export var letterChange=function(words,src,tgt){if(src==tgt)return words;var result=[];if(src=="latin")if(tgt=="kana"){var tmp_dic=dicMaker(0,1);var i=0;for(var [k,v]of soundchange.py_items())var words=words.py_replace(k,v);var len_tmp=len(words);while(i<len_tmp){if(__in__(words[i],vowels))result.append(tmp_dic[words[i]]);else if(__in__(words[i],
cons))if(i+1==len_tmp||!__in__(words[i+1],vowels))if(words[i]=="r")if(i<=0||!__in__(words[i-1],vowels))result.append(r_vowels[2]);else result.append(r_vowels[vowels.index(words[i-1])]);else if(i+1<len_tmp&&__in__(words.__getslice__(i,i+2,1),["pp","kk","ss"]))result.append(tmp_dic["t"][" "]);else if(i+1<len_tmp&&__in__(words.__getslice__(i,i+2,1),["mm"]))result.append(tmp_dic["n"][" "]);else result.append(tmp_dic[words[i]][" "]);else{result.append(tmp_dic[words[i]][words[i+1]]);i++}else result.append(words[i]);
i++}}return"".join(result)};

//# sourceMappingURL=AinuLetter.map