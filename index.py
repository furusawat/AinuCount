from AinuCount import numberStrings
from AinuLetter import letterChange

def click1():
    tmp = numberStrings(int(document.getElementById("num").value),document.getElementById("kind").value,document.getElementById("input").value,document.getElementById("dialect").value)+"\n"
    document.getElementById("words").textContent = letterChange(tmp,"latin",document.getElementById("letter").value)

def click2():
    tmp = ""
    for i in range(1,201):
        tmp += "{:3d} : ".format(i)+numberStrings(i,document.getElementById("kind").value,document.getElementById("input").value,document.getElementById("dialect").value)+"\n"
    document.getElementById("words").textContent = letterChange(tmp,"latin",document.getElementById("letter").value)
