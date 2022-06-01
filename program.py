from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import socket
import threading

HOST = 'localhost'  
PORT = 3000

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.connect((HOST,PORT))
root = Tk()
root.title("currency exchange")
root.geometry("500x650")

############## FUNCTION  ######################
def Cal1():
    # เช็คว่ากรอกข้อมูลครบยัง
    if not first_currency.get() or not second_currency.get() or not amount.get():
        messagebox.showwarning("WARNING","คุณยังเติมข้อมูลยังไม่ครบ")
    else:
        # ถ้ากรอกครบจะทำการส่งข้อมูลที่กรอก
        sum_value = first_currency.get()+"."+second_currency.get()+"."+amount.get() #ทำการรวมข้อมูลเป็นตัวเดียวกันโดยแบ่งแยกด้วย .
        server.send(sum_value.encode('utf-8')) #ส่งข้อมูลไปยัง server
        data_server = server.recv(1024).decode('utf-8') #รับข้อมูลกลับจาก server
        value2_entry.delete(0, END) # ทำการลบข้อมูลช่องนี้ถ้ามีการกรอกเกิดขึ้น
        value2_entry.insert(0,data_server) #นำข้อมูลมาแสดง
        server.close

def Clear():
    first_currency.delete(0,END)
    second_currency.delete(0,END)
    amount.delete(0,END)
    value2_entry.delete(0,END)

#################################################

####################  GUI  ######################
#Currency frame
currency = LabelFrame(text="currency")
currency.pack(pady=20)
#
currency1_Label = Label(currency, text="สกุลเงินที่จะเปลี่ยน",font=13) 
currency1_Label.pack(pady=10)

first_currency = Entry(currency, font=("Helvetica", 24))
first_currency.pack(pady=10,padx=10)

currency2_Label = Label(currency, text="สกุลเงินเปลี่ยน",font=13) 
currency2_Label.pack(pady=10)

second_currency = Entry(currency, font=("Helvetica", 24))
second_currency.pack(pady=10,padx=10)

#Valus frame

value = LabelFrame(text="value")
value.pack(pady=20)

value1_Label = Label(value, text="มูลค่าที่ต้องการจะเปลี่ยน",font=13) 
value1_Label.pack(pady=10)

amount = Entry(value, font=("Helvetica", 24))
amount.pack(pady=10,padx=10)

value2_Label = Label(value, text="ผลลัพธ์",font=13) 
value2_Label.pack(pady=10)

value2_entry = Entry(value, font=("Helvetica", 24) ,bd=0,bg="systembuttonface")
value2_entry.pack(pady=10,padx=10)

#Button
Button_Cal = Button(text="Calculate",font=("Helvetica",10),width=10,command=Cal1).pack(pady=10,padx=10)
Button_Clear = Button(text="Clear",font=("Helvetica",10),width=10,command=Clear).pack(pady=0,padx=10)

if __name__ == "__main__":
    root.mainloop()
