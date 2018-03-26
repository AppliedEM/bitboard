from tkinter import *
import btccore

#to compile: pyinstaller bitboard.py

sats = 100000000

class Application(Frame):

    def send(self):
        print("sending")
        ad = self.addr.get()
        am = self.amt.get()
        am = int(float(am)*sats)
        f = self.fe.get()
        f = int(f)
        outp = btccore.perform_transaction(ad, am, f)
        if outp != -1:
            if outp['success'] != False:
                self.balance.set(str(float(self.balance.get()) - (float(am)/sats) - (f*sats)))
        #print(outp)
        self.outputdisplay.set(outp)

    def receive(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(btccore.getaddress2(self.tnet.get()))
        r.update()
        r.destroy()
        self.outputdisplay.set('copied address to clipboard')

    def initvals(self):
        self.balance.set(float(btccore.getbalance(self.tnet.get()))/sats)
        self.outputdisplay.set('output will appear here')

    def importwif(self):
        key = self.imp.get()
        btccore.changewallet(key)
        self.initvals()

    def createWidgets(self):
        #self.QUIT = Button(self, text = "QUIT", command = self.quit).grid(row = 0, column = 0)
        self.outputdisplay = StringVar()
        self.tnet = IntVar()
        self.balance = StringVar()


        #zeroth row
        self.lab5 = Label(self, text="balance:").grid(row = 0, column = 0)
        self.lab6 = Label(self, textvariable = self.balance).grid(row=0, column = 1)
        self.tnetbutt = Checkbutton(self, text='testnet?', variable = self.tnet, command=self.initvals).grid(row=0, column = 2)

        #first row
        self.lab1 = Label(self, text="address:").grid(row = 1, column = 0)
        self.addr = StringVar()
        self.address = Entry(self, textvariable = self.addr).grid(row = 1, column = 1)

        #second row
        self.lab2 = Label(self, text="amount:").grid(row = 2, column = 0)
        self.amt = StringVar()
        self.amount = Entry(self, textvariable = self.amt).grid(row = 2, column = 1)



        #third row
        self.lab3 = Label(self, text="fee (satoshi):").grid(row = 3, column = 0)
        self.fe = StringVar()
        self.fee = Entry(self, textvariable = self.fe).grid(row = 3, column = 1)

        #fourth row
        self.send = Button(self, text = "SEND", command = self.send).grid(row = 4, column = 0)
        self.importbut = Button(self, text = "IMPORT", command = self.importwif).grid(row = 4, column = 1)
        self.receivebut = Button(self, text="RECEIVE", command = self.receive).grid(row=4,column=2)

        #fifth row
        self.lab4 = Label(self, text="Import:").grid(row = 5, column = 0)
        self.imp = StringVar()
        self.importfield = Entry(self, textvariable = self.imp).grid(row = 5, column = 1)

        #sixth row
        self.lab7 = Label(self, textvariable = self.outputdisplay).grid(row = 6, column = 1)
        self.initvals()




    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
