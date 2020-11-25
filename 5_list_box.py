from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()d
def btncmd():
    listbox.delete(1) # 맨 앞의 항목을 삭제
    listbox.delete(END) # 맨 뒤의 항목을 삭제

    #갯수 확인
    print("리스트에는", listbox.size(),)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()