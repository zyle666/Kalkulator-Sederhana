from functools import partial
import tkinter as tk


class applikasiKalkulator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MATH lite")
        self.membuatTombol()
        self.penentu = False

    def membuatTombol(self):
        self.layar = tk.Entry(self, width=39,bg="silver",relief="sunken",font=("arial",9,"bold"))
        self.layar.grid(row=0, column=0, columnspan=5)

        btn_list = [
            '1',  '2',  '3',
            '4',  '5',  '6',
            '7',  '8',  '9',
            '0',  '+',  '-',
            'C',  '/',  '*',
            '='
        ]
        baris = 1
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung, penampung)
            if penampung == '=':
                tk.Button(self, text='=',bg="violet",relief="sunken",font=("arial",10,"bold"), width=33, command=perintah).grid(row=baris, column=kolom, columnspan=8)
            else :
                tk.Button(self, text=penampung, width=10, command=perintah,bg="violet",relief="sunken",font=("arial",10,"bold")).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung(self, key):
        if key == '=':
            self.penentu = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.insert(tk.END, "-> Error!")
        elif key == 'C':
            self.layar.delete(0, tk.END)
        else:
            if self.penentu :
                self.layar.delete(0, tk.END)
                self.penentu = False
            self.layar.insert(tk.END, key)

panggil = applikasiKalkulator()
panggil.mainloop()
