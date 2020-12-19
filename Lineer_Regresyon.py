import tkinter
import pandas as pd
from matplotlib import pyplot as plt
import os
import sys
def h(i):
    return t[0] + t[1] * a["x"][i]

def J():
    s=0
    for i in range(len(a["y"])):
        s=s+ (h(i) - a["y"][i])**2
    return s/(2*len(a["y"]))
def gd():
    s = [0,0]
    for i in range(len(a["y"])):
        s[0]+= (h(i) - a["y"][i])
        s[1]+= (h(i) - a["y"][i])*a["x"][i]
    t[0] = t[0] - (alpha/len(a["y"]) * s[0])
    t[1] = t[1] - (alpha/len(a["y"]) * s[1])
def grafikciz():
    global xlabel 
    global ylabel 
    xlabel = i1.get()
    ylabel = i2.get()
    a = pd.read_csv(i5.get())
    plt.scatter(a["x"],a["y"])
    plt.plot(a["x"],t[0] + t[1] * a["x"])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def gradyaninis():
    global t
    t = [0,0]
    global alpha
    global iterasyon
    global loc 
    loc = i5.get()
    global a 
    a = pd.read_csv(loc)
    alpha  = float(i3.get())
    iterasyon = int(i4.get()) 
    global cost
    cost = []
    for i in range(iterasyon):
        gd()
        cost.append(J())
        print("Iterasyon " + str(i+1) + "/"+str(iterasyon))
    Tlabel["text"] = "θ0=" + str(t[0])+", " + "θ1=" + str(t[1]) + "\nHata Miktarı= " + str(cost[iterasyon-1])
    plt.plot(range(len(cost)),cost)
    plt.xlabel("İterasyon")
    plt.ylabel("Hata Miktarı")
    plt.show()
def hesap():
    y = i7.get()
    x = i6.get()
    if x == "?":
        i6.delete(0,"end")
        i6.insert(0,str(float(y)/t[1] - t[0]/t[1]))
    elif y == "?":
        i7.delete(0,"end")
        i7.insert(0,str(t[0] + t[1] * float(x)))
root = tkinter.Tk()
root.title("Gradyan İniş İle Lineer Regresyon")
root.resizable(False,False)
tkinter.Button(text = "Grafik Çiz",command = grafikciz).place(x = 0,y =170)
tkinter.Label(text = "X ekseninin ismi:").place(x=0,y=20)
i1 = tkinter.Entry()
i1.place(x= 100,y=20)
tkinter.Label(text = "Y ekseninin ismi:").place(x=0,y=50)
i2 = tkinter.Entry()
i2.place(x = 100,y=50)
tkinter.Label(text = "Alfa Değeri:").place(x = 0,y = 80)
i3 = tkinter.Entry()
i3.place(x = 100,y=80)
tkinter.Label(text = "İterasyon Sayısı:").place(x = 0,y= 110)
i4 = tkinter.Entry()
i4.place(x = 100,y=110)
i5 = tkinter.Entry(width = 49)
i5.place(x = 100, y= 140)
tkinter.Label(text = "Veri konumu:").place(x = 0,y = 140)
tkinter.Button(text = "Gradyan İniş",command = gradyaninis).place(x = 70,y= 170)
Tlabel = tkinter.Label(text = "θ0=0 θ1=0")
Tlabel.place(x = 150,y= 170)
i6 = tkinter.Entry(width = 10)
i6.place(x = 0,y = 250)
tkinter.Label(text = "Y değeri:").place(x = 100, y = 220)
tkinter.Label(text = "X değeri:").place(x = 0,y = 220)
i7 = tkinter.Entry(width = 10)
i7.place(x = 100,y = 250)
tkinter.Button(text = "Hesapla",command = hesap).place(x = 180,y = 250)
root.geometry("400x400")
root.mainloop()
