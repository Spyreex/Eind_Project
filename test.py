from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import time
import random
import qrcode
from time import *


class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def exit(self):
        self.top.withdraw()
        if __name__ == "__main__":
            window = Window(None)
            window.geometry('1920x1080')
            window.title('Home')
            window.mainloop()

    def initialize(self):
        self.regibutton = Button(master=self, text='Registreren', command=self.Regi,
                                 bg='lightgreen', relief=SOLID, font='Calibri',
                                 width=40)
        self.regibutton.pack(pady=10)

        self.logingobutton = Button(master=self, text='Inloggen', command=self.inloggen,
                               bg='lightgreen', relief=SOLID, font='Calibri',
                               width=40)
        self.logingobutton.pack(pady=10)

        self.infobutton = Button(master=self, text='Informatie', command=self.infoalgemeen,
                            bg='lightgreen', relief=SOLID, font='Calibri',
                            width=40)
        self.infobutton.pack(pady=10)

        self.quitbutton = Button(master=self, text='Afsluiten', command=quit,
                            bg='red', relief=SOLID, font='Calibri',
                            width=40)
        self.quitbutton.pack(pady=10)

    def regi(self):
        if self.telfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.ovrfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.vnaamfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.anaamfield.get()  == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.wwrfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')

        telefoon =self.telfield.get()
        if telefoon.isdigit():  # TELEFOON
            digit = telefoon
        else:
            digit = ' '
        if telefoon is not digit:
            return showwarning(title='Telefoon', message='Telefoonnummer mag alleen nummers bevatten')

        if len(telefoon) is not 8:
            return showwarning(title='Telefoon', message='Telefoonnummer moet 8 nummers bevatten')

        ov = self.ovrfield.get()
        if ov.isdigit():  # OV
            nummer = ov
        else:
            nummer = ' '
        if ov is not nummer:
            return showwarning(title='OV', message='OV mag alleen nummers bevatten')

        if len(ov) is not 4:
            return showwarning(title='OV', message='Telefoonnummer moet 4 nummers bevatten')

        ww = self.wwrfield.get()
        if len(ww) < 6:
            return showwarning(title='Wachtwoord', message='Het wachtwoord moet minstens 6 karakters bevatten')

        if self.wwrfield.get() != self.wwr2field.get():
            return showwarning(title='Wachtwoord', message='De wachtwoorden zijn niet gelijk ')

        with open('Gegevens', 'a') as f:

            f.write(self.vnaamfield.get())
            f.write(';')
            f.write(self.anaamfield.get())
            f.write(';')
            f.write(self.wwrfield.get())
            f.write(';')
            f.write(self.telfield.get())
            f.write(';')
            f.write(self.ovrfield.get())
            f.write('\n')
            f.close()
        return self.exit()

    def Regi(self):
        self.withdraw()
        self.top = Toplevel()
        self.top.title("Registreren")
        self.top.geometry("1920x1080")

        self.label = Label(self.top, text='Voornaam')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Achternaam')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Telefoonnummer(06-)')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Laatste 4 cijfers van uw OV')
        self.label.grid(row=3, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Wachtwoord (minimaal 6 karakters)')
        self.label.grid(row=4, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))
        self.label = Label(self.top, text='Wachtwoord opnieuw')
        self.label.grid(row=5, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.vnaamfield = Entry(master=self.top)
        self.vnaamfield.grid(row=0, column=21, pady=20)

        self.anaamfield = Entry(master=self.top)
        self.anaamfield.grid(row=1, column=21, pady=20)

        self.telfield = Entry(master=self.top)
        self.telfield.grid(row=2, column=21, pady=20)

        self.ovrfield = Entry(master=self.top)
        self.ovrfield.grid(row=3, column=21, pady=20)

        self.wwrfield = Entry(master=self.top, show='*')
        self.wwrfield.grid(row=4, column=21, pady=20)

        self.wwr2field = Entry(master=self.top, show='*')
        self.wwr2field.grid(row=5, column=21, pady=20)

        self.registrerenbutton = Button(self.top, text='Registreren', command=self.regi,
                                   bg='lightgreen', relief=SOLID, font='Calibri',
                                   width=40)
        self.registrerenbutton.grid(row=6, column=20, sticky=E)

        self.terugbutton = Button(self.top, text='Terug', command=self.exit,
                                   bg='lightgreen', relief=SOLID, font='Calibri',
                                   width=40)
        self.terugbutton.grid(row=6, column=21, sticky=E)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='red', relief=SOLID, font='Calibri',
                                 width=40)
        self.quitbutton.grid(row=6, column=22)


    def informatieIedereen(self):
        bezet = 0
        regel = open('Stallen.txt', 'r')
        for line in regel.readlines():
            bezet += 1
        regel.close()
        if bezet < 701:
            vrij = 701 - bezet

        else:
            vrij = 0
        return vrij

    def infoalgemeen(self):
        vrij = 'Om OV-fietsenstalling te gebruiken heeft u een geldige OV-chipkaart en telefoonnummer nodig. Er zijn geen stallingskosten, een fiets huren kost €0.80 per uur. Plaatsen vrij: '
        vrij2 = self.informatieIedereen()
        vrij3 = str(vrij)+ str(vrij2)
        showinfo(title='Informatie Algemeen', message=vrij3)

    def clicked(self):
        bericht = 'De ingevulde gegevens kloppen niet'
        showwarning(title='popup', message=bericht)

    def login(self):
        if self.naamfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.ovfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.wwfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        file = open('Gegevens', 'r')
        lines = file.readlines()
        for line in lines:
            y = line.strip('\n')
            z = y.split(';')
            if self.naamfield.get() == z[0]:
                if self.ovfield.get() == z[4]:
                    if self.wwfield.get() == z[2]:
                        file.close()
                        f1 = open('Ingelogd', 'w')
                        f1.write(line)
                        f1.close()
                        return self.menu2()
        self.clicked()

    def inloggen(self):
        self.withdraw()
        self.top = Toplevel()
        self.top.title("Inloggen")
        self.top.geometry("1920x1080")

        self.label = Label(self.top, text='Voornaam')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Wachtwoord')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.label = Label(self.top, text='Laatste 4 nummers van uw OV')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Calibri", 16))

        self.naamfield = Entry(master=self.top)
        self.naamfield.grid(row=0, column=21, pady=20)

        self.wwfield = Entry(master=self.top, show='*')
        self.wwfield.grid(row=1, column=21, pady=20)

        self.ovfield = Entry(master=self.top)
        self.ovfield.grid(row=2, column=21, pady=20)

        self.loginbutton = Button(master=self.top, text='Inloggen', command=self.login,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
        self.loginbutton.grid(row=6, column=20, sticky=E)

        self.terugbutton = Button(self.top, text='Terug', command=self.exit,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
        self.terugbutton.grid(row=6, column=21, sticky=E)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='red', relief=SOLID, font='Calibri',
                                 width=30)
        self.quitbutton.grid(row=6, column=22, sticky=E)

    def menu2(self):
        self.top.withdraw()
        self.top = Toplevel()
        self.top.title("Inloggen")
        self.top.geometry("1920x1080")

        self.stallenbutton = Button(master=self.top, text='Fiets Stallen', command=self.fiets_stallen,
                                    bg='lightgreen', relief=SOLID, font='Calibri',
                                    width=40)
        self.stallenbutton.pack(pady=10)

        self.ophalenbutton = Button(master=self.top, text='Fiets Ophalen', command=self.Fietsophalen,
                                    bg='lightgreen', relief=SOLID, font='Calibri',
                                    width=40)
        self.ophalenbutton.pack(pady=10)

        self.hurenbutton = Button(master=self.top, text='Fiets Huren', command=self.fiets_huren,
                                  bg='lightgreen', relief=SOLID, font='Calibri',
                                  width=40)
        self.hurenbutton.pack(pady=10)

        self.terugbrengenbutton = Button(master=self.top, text='Huurfiets Terugbrengen', command=self.fiets_terugbrengen,
                                         bg='lightgreen', relief=SOLID, font='Calibri',
                                         width=40)
        self.terugbrengenbutton.pack(pady=10)

        self.informatiebutton = Button(master=self.top, text='Informatie', command=self.InfoEigenaar,
                                       bg='lightgreen', relief=SOLID, font='Calibri',
                                       width=40)
        self.informatiebutton.pack(pady=10)

        self.hulpqrbutton = Button(master=self.top, text='Hulp QR', command=self.QRHulpPopup,
                                       bg='lightgreen', relief=SOLID, font='Calibri',
                                       width=40)
        self.hulpqrbutton.pack(pady=10)

        self.uitloggenbutton = Button(self.top, text='Uitloggen', command=self.exit,
                                      bg='red', relief=SOLID, font='Calibri',
                                      width=40)
        self.uitloggenbutton.pack(pady=10)

    def fiets_stallen(self):

        import time

        read = open('Ingelogd', 'r')
        infile = read.readlines()
        for lines in infile:
            gegevens = lines.split(';')
            voornaam = gegevens[0]
            achternaam = gegevens[1]
            ov = gegevens[4].strip('\n')
        read.close()

        read1 = open('Stallen.txt','r')
        infile1 = read1.readlines()
        for lines1 in infile1:
            stalgegevens = lines1.split(';')
            voornaamstal = stalgegevens[0]
            achternaamstal = stalgegevens[1]
            ovstal = stalgegevens[9]
            stalnummer = stalgegevens[10].strip('\n')
            if voornaam == voornaamstal and achternaam == achternaamstal and ov == ovstal:
                self.stalErrorText = ('U heeft al een fiets gestald op plek: ' + str(stalnummer))
                showinfo(title='Error', message=self.stalErrorText)
                return self.login()
        read1.close()

        self.cijfer = random.randint(1001, 999999)
        rnummer = random.randint(1, 701)
        datum = time.strftime('%H;%M;%S;%d;%m;%Y')

        writeStal = open('Stallen.txt','a')
        writeStal.write(voornaam + ';' + achternaam + ';' + str(self.cijfer) + ';' + datum + ';' + str(ov) + ';' + str(rnummer) + '\n')
        writeStal.close()

        stallenbericht = 'U kunt u fiets veilig stallen op plek: ' + str(rnummer)
        showinfo(title='Stallen', message=stallenbericht)
        return self.qrCodePopup()

    def qrCodePopup(self):    # cijfer nog global maken ofzo en qr code toevoegen ofzo
        self.bewaartext = (
            'Bewaar de volgende QR Code om je fiets weer op te halen.')
        showinfo(title='Hulp QR', message=self.bewaartext)

        return qrcode.run_example(self.cijfer)

    def fiets_huren(self):

        self.top.withdraw()
        self.top = Toplevel()
        self.top.title("Fiets Huren")
        self.top.geometry("1920x1080")

        self.huurtext = Label(master=self.top, text='Weet u zeker dat u een fiets wilt huren?\n'
                                                    'Het tarief is: €1 euro + 20 cent per 15 minuten',
                                                    relief=SOLID, font='Calibri')
        self.huurtext.place(relx=0.5, rely=0.4, anchor=S)

        self.accepteerbutton = Button(master=self.top, text='Ja', command=self.Fiets_huren,
                                    bg='lightgreen', relief=SOLID, font='Calibri',
                                    width=40)
        self.accepteerbutton.place(relx=0.26 ,rely=0.422, anchor=W)

        self.accepteernietbutton = Button(master=self.top, text='Nee', command=self.login,
                                    bg='red', relief=SOLID, font='Calibri   ',
                                    width=40)
        self.accepteernietbutton.place(relx=0.5, rely=0.4)

    def Fiets_huren(self):

        import time

        huurnummer = random.randint(1,50)

        infile = open('Ingelogd', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')

        file = open('Huurgegevens', 'r')
        lines = file.readlines()
        file.close()

        for line in lines:  # checked of dezelfde gegevens in 'Ingelogd' ook staan in 'Huurgegevens', zoja, dan betekend het dat er al een fiets is gehuurd
            x = line.split(';')
            if inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[2]:
                huurtext = ('U heeft al een fiets gehuurd')
                showinfo(title='Error', message=huurtext)
                return self.login()

            if huurnummer == x[3]:
                self.Fiets_huren()

        datum = time.strftime('%H;%M;%S;%d;%m;%Y')
        datum1 = time.strftime('%H:%M:%S %d/%m/%Y')

        huurfile = open('Huurgegevens', 'a')
        huurfile.write(inlog[0] + ';' + inlog[1] + ';' + inlog[4].strip('\n') + ';' + str(huurnummer) + ';' + datum + '\n')
        huurfile.close()

        huurtext = ('Fietsnummer {} is gehuurd vanaf {}.'.format(huurnummer, datum1))
        showinfo(title='Fiets Gehuurd', message=huurtext)
        return self.login()

    def regel_verwijderen(self):
        lijst = []
        file = open('Huurgegevens', 'r')
        regels = file.readlines()
        file.close()

        infile = open('Ingelogd', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')
        infile.close()

        for regel in regels:  # voegt elke regel toe die niet gelijk is aan de teruggebrachde fiets aan een lijst, die hij later terug het bestand in zet
            x = regel.split(';')
            counter = 0
            if inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[2]:
                counter += 1
            if counter == 0:
                lijst.append(regel)
        file.close()
        wfile = open('Huurgegevens', 'w')
        for gegevens in range(len(lijst)):
            wfile.write(lijst[gegevens])

    def fiets_terugbrengen(self):

        import time

        gelukt = 0
        dag = 86400  # in seconden
        jaar = 31536000

        terugfile = open('Huurgegevens', 'r')
        linest = terugfile.readlines()
        terugfile.close()

        infile = open('Ingelogd', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')
        infile.close()

        for linet in linest:
            y = linet.split(';')

            if inlog[0] == y[0] and inlog[1] == y[1] and inlog[4].strip('\n') == y[2]:
                datumstartH = y[4]
                datumstartM = y[5]
                datumstartS = y[6]
                datumstartd = y[7]
                datumstartm = y[8]
                datumstartY = y[9].strip('\n')

                tijdHt = time.strftime('%H')  # uren;tijdsbepaling van nu
                tijdMt = time.strftime('%M')  # minuten
                tijdSt = time.strftime('%S')  # seconden
                datumdt = time.strftime('%d')  # dag
                datummt = time.strftime('%m')  # maand
                datumYt = time.strftime('%Y')  # jaar

                tijddatum = tijdHt + ':' + tijdMt + ':' + tijdSt + ' ' + datumdt + '/' + datummt + '/' + datumYt

                print('U heeft de fiets gehuurd sinds',
                      '{}:{}:{} {}/{}/{}'.format(datumstartH, datumstartM, datumstartS, datumstartd, datumstartm,
                                                 datumstartY), 'en de fiets terug gebracht op', tijddatum)
                total = int(datumstartH) * 3600 + int(datumstartM) * 60 + int(datumstartS) + int(
                    datumstartd) * dag + int(datumstartm) / 12 * jaar + int(datumstartY) * jaar
                totalt = int(tijdHt) * 3600 + int(tijdMt) * 60 + int(tijdSt) + int(datumdt) * dag + int(
                    datummt) / 12 * jaar + int(datumYt) * jaar

                gehuurdtijdtotal = totalt - total
                gehuurdtijd = gehuurdtijdtotal
                totalY = gehuurdtijd // (jaar)  # hier en onder berekent hij per tijd hoelang de fiets gehuurd is
                if totalY == 1:
                    jaren = 'jaar'
                else:
                    jaren = 'jaren'
                gehuurdtijd = gehuurdtijd - totalY * jaar
                totalm = gehuurdtijd // (jaar / 12)
                if totalm == 1:
                    maanden = 'maand'
                else:
                    maanden = 'maanden'
                gehuurdtijd = gehuurdtijd - totalm * jaar / 12
                totald = gehuurdtijd // (dag)
                if totald == 1:
                    dagen = 'dag'
                else:
                    dagen = 'dagen'
                gehuurdtijd = gehuurdtijd - totald * dag
                totalH = gehuurdtijd // (3600)
                if totalH == 1:
                    uren = 'uur'
                else:
                    uren = 'uren'
                gehuurdtijd = gehuurdtijd - totalH * 3600
                totalM = gehuurdtijd // (60)
                if totalM == 1:
                    minuten = 'minuut'
                else:
                    minuten = 'minuten'
                gehuurdtijd = gehuurdtijd - totalM * 60
                totalS = gehuurdtijd
                if totalS == 1:
                    seconden = 'seconde'
                else:
                    seconden = 'seconden'

                prijs = gehuurdtijdtotal // (60 * 15) * 0.2 + 1  # elke 15 minuten + 20 cent en standaard 1 euro
                prijsafg = round(prijs,2)
                self.regel_verwijderen()

                terugbrengentext = ('U heeft de fiets voor {} {}, {} {}, {} {}, {} {}, {} {} en {} {} gehuurd, dat kost u {} euro'.format(
                    int(totalY), jaren, int(totalm), maanden, int(totald), dagen, int(totalH), uren, int(totalM),
                    minuten, int(totalS), seconden, str(prijsafg)))
                showinfo(title='Fiets Teruggebracht', message=terugbrengentext)
                return self.login()

        if gelukt != 1:
            terugniettext = ('U kan niet de fiets terugbrengen, omdat u geen fiets heeft gehuurd')
            showinfo(title='Error', message=terugniettext)
            return self.login()
    def infopopup(self):
        self.infotext = (
                    'Geregistreerde naam: ' + self.naam + ' ' + self.achternaam + '\n' + 'Geregisteerd wachtwoord: ' + self.ww + '\n' + 'Geregisteerd telefoon nummer: ' + self.tel + '\n' + 'Geregisteerde OV: ' + self.ov)
        showinfo(title='Stallen', message=self.infotext)

    def InfoEigenaar(self):
            gegevens = open('Ingelogd', 'r')
            gegeven = gegevens.readlines()
            for item in gegeven:
                regel = item.split(';')
                self.naam = regel[0]
                self.achternaam = regel[1]
                self.ww = regel[2]
                self.tel = regel[3]
                self.ov = regel[4]
                self.infopopup()

    def QRHulpPopup(self):
        self.infotext = (
                    'Om een QR te scannen moet u een QR of Barcode scanner downloaden op uw smartphone. Na het scannen krijgt u de code te zien, bewaar deze om later je fiets weer op te kunnen halen.')
        showinfo(title='Hulp QR', message=self.infotext)

    def OphalenPopup(self):

        readfile = open('Stallen.txt', 'r')
        infile2 = readfile.readlines()
        for lines2 in infile2:
            stalgegevens = lines2.split(';')
            voornaam = stalgegevens[0]
            stalnummer = stalgegevens[10].strip('\n')
            codegegeven = stalgegevens[2].strip('')
        if self.code.get() != codegegeven:
            return showwarning(title='Fout', message='De ingevulde code is onjuist')
        else:
            self.infotext = (
                    voornaam + ' uw fiets is ontgrendeld en staat vrij om opgehaald te worden op stal #' + stalnummer)
            showinfo(title='Ophaal', message=self.infotext)
            self.top.withdraw()




    def Fietsophalen(self):

        self.top = Toplevel()
        self.top.title('Ophalen')
        self.top.geometry("1920x1080")


        self.label = Label(self.top, text='Uw QR Code')
        self.label.config(font=("Calibri", 16))
        self.label.pack(fill=X, padx=25, pady=100)




        self.code = Entry(master=self.top)
        self.code.pack(fill=X, padx=700)

        self.Enterbutton = Button(master=self.top, text='Enter', command=self.OphalenPopup,
                                          bg='lightgreen', relief=SOLID, font='Calibri',
                                          width=40)
        self.Enterbutton.pack(fill=X, padx=600, pady=25)

        self.Closebutton = Button(master=self.top, text='Afsluiten', command=self.exit,
                                  bg='red', relief=SOLID, font='Calibri',
                                  width=40)
        self.Closebutton.pack(fill=X, padx=600, pady=10)


if __name__ == "__main__":
    window = Window(None)
    window.geometry('1920x1080')
    window.title('Home')
    window.mainloop()

