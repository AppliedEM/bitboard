from tkinter import *
import btccore

sats = 100000000

class Application(Frame):

    def send(self):
        print("sending")
        ad = self.addr.get()
        am = self.amt.get()
        am = int(float(am)*sats)
        f = self.fe.get()
        f = int(float(f)*sats)
        outp = btccore.perform_transaction(ad, am, f)
        print(outp)

    def createWidgets(self):
        #self.QUIT = Button(self, text = "QUIT", command = self.quit).grid(row = 0, column = 0)


        self.lab1 = Label(self, text="address:").grid(row = 1, column = 0)
        self.addr = StringVar()
        self.address = Entry(self, textvariable = self.addr).grid(row = 1, column = 1)

        self.lab2 = Label(self, text="amount:").grid(row = 2, column = 0)
        self.amt = StringVar()
        self.amount = Entry(self, textvariable = self.amt).grid(row = 2, column = 1)

        self.lab3 = Label(self, text="fee:").grid(row = 3, column = 0)
        self.fe = StringVar()
        self.fee = Entry(self, textvariable = self.fe).grid(row = 3, column = 1)

        self.send = Button(self, text = "SEND", command = self.send).grid(row = 4, column = 0)



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
