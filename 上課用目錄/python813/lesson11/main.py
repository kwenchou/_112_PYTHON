import tkinter as tk
import tools

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我的第一個視窗")        
        btn1 = tk.Button(self,text="下載資料",padx=50,pady=25,font=('Arial',20,'bold'),command=self.btn1_click)
        btn1.pack(padx=100,pady=50)

    def btn1_click(self):
        print("PI的值是")
        print(type(tools.PI))
        print(type(tools.myfunction))
        print(type(tools.MyClass))
        

def main():
    #chinese和english區域變數
    window = Window()   
    window.mainloop()

if __name__ == "__main__":
    main()
    
