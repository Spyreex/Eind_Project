from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import random
import qrcode
import time

class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def exit(self):
        """
        Hier gaan de codes op het Hoofdmenu op terug als je op Terug drukt. Ook als je succesvol hebt geregistreerd.
        Het bouwed ook de GUI.
        """
        self.top.withdraw()
        if __name__ == "__main__":
            window = Window(None)
            window.geometry('1280x720')
            window.title('Home')
            window.wm_iconbitmap('ns.ico')
            window.configure(bg='gold')

            windowWidth = window.winfo_reqwidth()
            windowHeight = window.winfo_reqheight()
            positionRight = int(window.winfo_screenwidth() / 4 - windowWidth / 1.5)
            positionDown = int(window.winfo_screenheight() / 4 - windowHeight / 1.5)
            window.geometry("+{}+{}".format(positionRight, positionDown))

            window.mainloop()

    def initialize(self):
        """
        Het Hoofdmenu van de Fietsen stalling, hier registreer je of Log je in. Je kunt ook informatie opvragen
        van de fietsenstalling.
        """
        photo = PhotoImage(master=self, file="ns.png")
        w = Label(self, image=photo, bg='gold')
        w.photo = photo
        w.pack(pady=25)
        self.rnummer = -1
        self.welcometext = Label(master=self, text='Welkom bij deze NS fietsenstalling\n'
                                                    'Kies een van de volgende opties:',
                              bg = 'gold', relief=FLAT, font='Sans', fg= 'blue4')
        self.welcometext.pack(pady = 50)

        self.regibutton = Button(master=self, text='Registreren', command=self.Regi,
                                 bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                 width=40)
        self.regibutton.pack(pady=10)

        self.logingobutton = Button(master=self, text='Inloggen', command=self.inloggen,
                               bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                               width=40)
        self.logingobutton.pack(pady=10)

        self.infobutton = Button(master=self, text='Informatie', command=self.infoalgemeen,
                            bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                            width=40)
        self.infobutton.pack(pady=10)

        self.quitbutton = Button(master=self, text='Afsluiten', command=quit,
                            bg='goldenrod', relief=FLAT, font='Arial', fg='blue4',
                            width=40)
        self.quitbutton.pack(pady=10)

    def regi(self):
        """
        De code voor het registeren, testen of alle velden zijn ingevult, of het ingevulde telefoon en ovnummer uit
        cijfers bestaat, of er al iemand met de opgegeven voornaam, achternaam en ov bestaat, of het wachtwoord meer
        dan 6 karakters bevat en velvolgens write hij dit in Gegevens.txt.
        """
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

        telefoon = self.telfield.get()
        vnaam = self.vnaamfield.get()
        anaam = self.anaamfield.get()
        ov = self.ovrfield.get()
        ww = self.wwrfield.get()
        ww2 = self.wwr2field.get()

        if telefoon.isdigit():
            digit = telefoon
        else:
            digit = ' '
        if telefoon is not digit:
            return showwarning(title='Telefoon', message='Telefoonnummer mag alleen cijfers bevatten')

        if len(telefoon) is not 8:
            return showwarning(title='Telefoon', message='Telefoonnummer moet 8 cijfers bevatten')

        gegevens = open('Gegevens.txt','r')
        line = gegevens.readlines()
        for lines in line:
            x = lines.split(';')
            if vnaam == x[0] and anaam == x[1] and ov == x[4].strip('\n'):
                return showwarning(title='Error', message='Er is al geregistreerd met deze gegevens')
            if telefoon == x[3]:
                return showwarning(title='Error', message='Er is al iemand met dit telefoonnummer')
        if ov.isdigit():
            nummer = ov
        else:
            nummer = ' '
        if ov is not nummer:
            return showwarning(title='OV', message='OV mag alleen nummers bevatten')

        if len(ov) is not 4:
            return showwarning(title='OV', message='Het OV moet 4 nummers bevatten')

        if len(ww) < 6:
            return showwarning(title='Wachtwoord', message='Het wachtwoord moet minstens 6 karakters bevatten')

        if ww != ww2:
            return showwarning(title='Wachtwoord', message='De wachtwoorden zijn niet gelijk')

        result = ''

        for i in range(0, len(ww)):
            result = result + chr(ord(ww[i]) - 4)

        with open('Gegevens.txt', 'a') as f:

            f.write(self.vnaamfield.get())
            f.write(';')
            f.write(self.anaamfield.get())
            f.write(';')
            f.write(result)
            f.write(';')
            f.write(self.telfield.get())
            f.write(';')
            f.write(self.ovrfield.get())
            f.write('\n')
            f.close()
        showwarning(title='Geregistreerd', message='Succesvol geregistreerd')
        return self.exit()

    def Regi(self):
        """
        De GUI van het registreren scherm.
        """
        self.withdraw()
        self.top = Toplevel()
        self.top.title("Registreren")
        self.top.wm_iconbitmap('ns.ico')
        self.top.geometry("1280x720")
        self.top.configure(bg='gold')

        windowWidth = self.top.winfo_reqwidth()
        windowHeight = self.top.winfo_reqheight()
        positionRight = int(self.top.winfo_screenwidth() / 4 - windowWidth / 1.5)
        positionDown = int(self.top.winfo_screenheight() / 4 - windowHeight / 1.5)
        self.top.geometry("+{}+{}".format(positionRight, positionDown))

        self.label = Label(self.top, text='')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W, pady=50)
        self.label.config(bg='gold')

        self.label = Label(self.top, text='Voornaam')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Achternaam')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Telefoonnummer(06-)')
        self.label.grid(row=3, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Laatste 4 cijfers van uw OV')
        self.label.grid(row=4, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Wachtwoord (minimaal 6 karakters)')
        self.label.grid(row=5, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Wachtwoord opnieuw')
        self.label.grid(row=6, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.vnaamfield = Entry(master=self.top)
        self.vnaamfield.grid(row=1, column=21, pady=20)

        self.anaamfield = Entry(master=self.top)
        self.anaamfield.grid(row=2, column=21, pady=20)

        self.telfield = Entry(master=self.top)
        self.telfield.grid(row=3, column=21, pady=20)

        self.ovrfield = Entry(master=self.top)
        self.ovrfield.grid(row=4, column=21, pady=20)

        self.wwrfield = Entry(master=self.top, show='*')
        self.wwrfield.grid(row=5, column=21, pady=20)

        self.wwr2field = Entry(master=self.top, show='*')
        self.wwr2field.grid(row=6, column=21, pady=20)

        self.registrerenbutton = Button(self.top, text='Registreren', command=self.regi,
                                   bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                   width=40)
        self.registrerenbutton.grid(row=7, column=21, sticky=E, pady=10)

        self.terugbutton = Button(self.top, text='Terug', command=self.exit,
                                   bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                   width=40)
        self.terugbutton.grid(row=8, column=21, sticky=E, pady=10)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='goldenrod', relief=FLAT, font='Arial', fg='blue4',
                                 width=40)
        self.quitbutton.grid(row=9, column=21, pady=10)

    def informatieIedereen(self):
        """
        Om bij de popup van informatie het aantal vrije stallingen te laten zien.
        """
        regel = open('Stallen.txt', 'r')
        line = regel.readlines()
        regel.close()
        if len(line) < 701:
            vrij = 701 - len(line)
        else:
            vrij = 0
        return vrij

    def infoalgemeen(self):
        """
        De popup die komt als je op Informatie drukt.
        """
        vrij = 'Om OV-fietsenstalling te gebruiken heeft u een geldige OV-chipkaart en telefoonnummer nodig. Er zijn geen stallingskosten, een fiets huren kost €1 plus €0.20 per kwartier. Plaatsen vrij: '
        vrij2 = self.informatieIedereen()
        vrij3 = str(vrij)+ str(vrij2)
        showinfo(title='Informatie Algemeen', message=vrij3)

    def clicked(self):
        """
        Als bij het inlog scherm de gegevens niet kloppen.
        """
        bericht = 'De ingevulde gegevens kloppen niet'
        showwarning(title='popup', message=bericht)

    def login(self):
        """
        De code voor het inloggen. Hij checked of alle velden zijn ingevuld, vervolgens write hij alles in
        Ingelogd.txt.
        """
        if self.naamfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.ovfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.wwfield.get() == '':
           return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        ww = self.wwfield.get()

        result = ''

        for i in range(0, len(ww)):
            result = result + chr(ord(ww[i]) - 4)

        file = open('Gegevens.txt', 'r')
        lines = file.readlines()
        for line in lines:
            y = line.strip('\n')
            z = y.split(';')
            if self.naamfield.get() == z[0]:
                if self.ovfield.get() == z[4]:
                    if result == z[2]:
                        file.close()
                        f1 = open('Ingelogd.txt', 'w')
                        f1.write(line)
                        f1.close()
                        return self.menu2()
        self.clicked()

    def inloggen(self):
        """
        De GUI voor het inlog scherm.
        """
        self.withdraw()
        self.top = Toplevel()
        self.top.title("Inloggen")
        self.top.wm_iconbitmap('ns.ico')
        self.top.geometry("1280x720")
        self.top.configure(bg='gold')

        windowWidth = self.top.winfo_reqwidth()
        windowHeight = self.top.winfo_reqheight()
        positionRight = int(self.top.winfo_screenwidth() / 4 - windowWidth / 1.5)
        positionDown = int(self.top.winfo_screenheight() / 4 - windowHeight / 1.5)
        self.top.geometry("+{}+{}".format(positionRight, positionDown))

        self.label = Label(self.top, text='')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W, pady=50)
        self.label.config(bg='gold')

        self.label = Label(self.top, text='Voornaam')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W, pady=10)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Wachtwoord')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.label = Label(self.top, text='Laatste 4 nummers van uw OV')
        self.label.grid(row=3, column=20, ipadx=170, sticky=W)
        self.label.config(font=("Arial", 16),bg = 'gold',fg= 'blue4')

        self.naamfield = Entry(master=self.top)
        self.naamfield.grid(row=1, column=21, pady=20)

        self.wwfield = Entry(master=self.top, show='*')
        self.wwfield.grid(row=2, column=21, pady=20)

        self.ovfield = Entry(master=self.top)
        self.ovfield.grid(row=3, column=21, pady=20)

        self.loginbutton = Button(master=self.top, text='Inloggen', command=self.login,
                                  bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                  width=40)
        self.loginbutton.grid(row=7, column=21, sticky=E, pady=10)

        self.terugbutton = Button(self.top, text='Terug', command=self.exit,
                                  bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                  width=40)
        self.terugbutton.grid(row=8, column=21, sticky=E, pady=10)

        self.quitbutton = Button(master=self.top, text='Afsluiten', command=quit,
                                 bg='goldenrod', relief=FLAT, font='Arial', fg='blue4',
                                 width=40)
        self.quitbutton.grid(row=9, column=21, sticky=E, pady=10)

    def menu2(self):
        """
        De GUI van de fietsenstalling. Met knoppen voor alle opties binnen de fietsen stalling.
        """
        self.top.withdraw()
        self.top = Toplevel()
        self.top.title("Fietsen Stalling")
        self.top.wm_iconbitmap('ns.ico')
        self.top.geometry("1280x720")
        self.top.configure(bg='gold')

        windowWidth = self.top.winfo_reqwidth()
        windowHeight = self.top.winfo_reqheight()
        positionRight = int(self.top.winfo_screenwidth() / 4 - windowWidth / 1.5)
        positionDown = int(self.top.winfo_screenheight() / 4 - windowHeight / 1.5)
        self.top.geometry("+{}+{}".format(positionRight, positionDown))

        photo = PhotoImage(master=self.top, file="ns.png")
        w = Label(self.top, image=photo, bg='gold')
        w.photo = photo
        w.pack(pady=25)

        self.stallenbutton = Button(master=self.top, text='Fiets Stallen', command=self.fiets_stallen,
                                    bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                    width=40)
        self.stallenbutton.pack(pady=10)

        self.ophalenbutton = Button(master=self.top, text='Fiets Ophalen', command=self.Fietsophalen,
                                    bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                    width=40)
        self.ophalenbutton.pack(pady=10)

        self.hurenbutton = Button(master=self.top, text='Fiets Huren', command=self.fiets_huren,
                                  bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                  width=40)
        self.hurenbutton.pack(pady=10)

        self.terugbrengenbutton = Button(master=self.top, text='Huurfiets Terugbrengen', command=self.fiets_terugbrengen,
                                         bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                         width=40)
        self.terugbrengenbutton.pack(pady=10)

        self.informatiebutton = Button(master=self.top, text='Informatie', command=self.InfoEigenaar,
                                       bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                       width=40)
        self.informatiebutton.pack(pady=10)

        self.hulpqrbutton = Button(master=self.top, text='Hulp QR', command=self.QRHulpPopup,
                                       bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                       width=40)
        self.hulpqrbutton.pack(pady=10)

        self.wwveranderen = Button(master=self.top, text='Wachtwoord Veranderen', command=self.WachtwoordVeranderenWindow,
                                   bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                   width=40)
        self.wwveranderen.pack(pady=10)

        self.uitlogbutton = Button(master=self.top, text='Uitloggen', command=self.Uitloggen,
                                      bg='goldenrod', relief=FLAT, font='Arial', fg='blue4',
                                      width=40)
        self.uitlogbutton.pack(pady=10)

    def fiets_stallen(self):
        """
        De code voor het stallen van je fiets, hij neemt gegevens uit Ingelogd.txt en maakt een random nummer aan voor
        de fiets stal plek. Hij checked of je al een fiets hebt gestald en of de fietsen stalling vol zit. Vervolgens
        haalt hij de tijd en datum op en write hij alle gegevens in de file Stallen.txt.
        """
        read = open('Ingelogd.txt', 'r')
        infile = read.readlines()
        for lines in infile:
            gegevens = lines.split(';')
            voornaam = gegevens[0]
            achternaam = gegevens[1]
            ov = gegevens[4].strip('\n')
        read.close()

        self.rnummer = random.randint(1, 701)
        try:
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
                    return self.menu2

                if len(infile1) == 701:
                    self.stalVolText = ('De fietsenstalling zit vol')
                    showinfo(title='Error', message=self.stalVolText)
                    return self.login()

                while stalnummer == self.rnummer:
                    self.rnummer = random.randint(1, 701)

            read1.close()
            raise Exception

        except:
            self.cijfer = random.randint(1001, 999999)

            datum = time.strftime('%H;%M;%S;%d;%m;%Y')

            writeStal = open('Stallen.txt','a')
            writeStal.write(voornaam + ';' + achternaam + ';' + str(self.cijfer) + ';' + datum + ';' + str(ov) + ';' + str(self.rnummer) + '\n')
            writeStal.close()

            stallenbericht = 'U kunt u fiets veilig stallen op plek: ' + str(self.rnummer)
            showinfo(title='Stallen', message=stallenbericht)
            return self.qrCodePopup()

    def qrCodePopup(self):
        """
        Popup voor de QR hulp.
        """
        self.bewaartext = (
            'Bewaar de volgende QR Code om je fiets weer op te halen.')
        showinfo(title='Hulp QR', message=self.bewaartext)

        return qrcode.run_example(self.cijfer)

    def fiets_huren(self):
        """
        De GUI voor bij het huren van een ov fiets.
        """
        self.top.withdraw()
        self.top = Toplevel()
        self.top.title("Fiets Huren")
        self.top.wm_iconbitmap('ns.ico')
        self.top.geometry("1280x720")
        self.top.configure(bg='gold')

        windowWidth = self.top.winfo_reqwidth()
        windowHeight = self.top.winfo_reqheight()
        positionRight = int(self.top.winfo_screenwidth() / 4 - windowWidth / 1.5)
        positionDown = int(self.top.winfo_screenheight() / 4 - windowHeight / 1.5)
        self.top.geometry("+{}+{}".format(positionRight, positionDown))

        photo = PhotoImage(master=self.top, file="ns.png")
        w = Label(self.top, image=photo, bg='gold')
        w.photo = photo
        w.pack(pady=25)

        self.huurtext = Label(master=self.top, text='Weet u zeker dat u een fiets wilt huren?\n'
                                                    'Het tarief is: €1 euro + 20 cent per 15 minuten',
                                                    relief=FLAT, font='Arial',fg='blue4', bg='gold')
        self.huurtext.pack(pady=50)

        self.accepteerbutton = Button(master=self.top, text='Ja', command=self.Fiets_huren,
                                    bg='DodgerBlue2', relief=FLAT, font='Arial', fg= 'white',
                                    width=40)
        self.accepteerbutton.pack(pady=10)

        self.accepteernietbutton = Button(master=self.top, text='Nee', command=self.menu2,
                                    bg='goldenrod', relief=FLAT, font='Arial   ', fg='blue4',
                                    width=40)
        self.accepteernietbutton.pack(pady=10)

    def Fiets_huren(self):
        """
        De code voor het huren van een ov fiets, hij checked of je al een fiets hebt gehuurd en of er nog ov fietsen
        over zijn. Hij haalt de tijd op en write alle gegevens in de file Huurgegevens.txt.
        """
        huurnummer = random.randint(1,50)

        infile = open('Ingelogd.txt', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')

        file = open('Huurgegevens.txt', 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            x = line.split(';')
            if inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[2]:
                huurtext = ('U heeft al een fiets gehuurd')
                showinfo(title='Error', message=huurtext)
                return self.menu2()

            if len(lines) == 50:
                geenfietsentext = ('Er zijn helaas geen fietsen meer beschikbaar')
                showinfo(title='Error', message=geenfietsentext)
                return self.menu2()

            if huurnummer == x[3]:
                self.Fiets_huren()

        datum = time.strftime('%H;%M;%S;%d;%m;%Y')
        datum1 = time.strftime('%H:%M:%S %d/%m/%Y')

        huurfile = open('Huurgegevens.txt', 'a')
        huurfile.write(inlog[0] + ';' + inlog[1] + ';' + inlog[4].strip('\n') + ';' + str(huurnummer) + ';' + datum + '\n')
        huurfile.close()

        huurtext = ('Fietsnummer {} is gehuurd vanaf {}.'.format(huurnummer, datum1))
        showinfo(title='Fiets Gehuurd', message=huurtext)
        return self.menu2()

    def regel_verwijderen(self):
        """
        De code voor het verwijderen van de line uit Huurgegevens.txt.
        """
        lijst = []
        file = open('Huurgegevens.txt', 'r')
        regels = file.readlines()
        file.close()

        infile = open('Ingelogd.txt', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')
        infile.close()

        for regel in regels:
            x = regel.split(';')
            counter = 0
            if inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[2]:
                counter += 1
            if counter == 0:
                lijst.append(regel)
        file.close()
        wfile = open('Huurgegevens.txt', 'w')
        for gegevens in range(len(lijst)):
            wfile.write(lijst[gegevens])
        wfile.close()

    def fiets_terugbrengen(self):
        """
        De code voor als je je huur fiets terug brengt. Hij neemt de datum van nu als een lang cijfer en neemt de datum
        van huren en trekt deze van elkaar af. zo krijg je de tijd dat de fiets is gestald. We hebben gekozen voor de
        schaal van elke 15 is 'een dag'. om te voorkomen dat je letterlijk een dag moet wachten. Dan geeft hij een popup
        dat je fiets is teruggebracht.
        """
        gelukt = 0
        dag = 86400
        jaar = 31536000

        terugfile = open('Huurgegevens.txt', 'r')
        linest = terugfile.readlines()
        terugfile.close()

        infile = open('Ingelogd.txt', 'r')
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

                total = int(datumstartH) * 3600 + int(datumstartM) * 60 + int(datumstartS) + int(
                    datumstartd) * dag + int(datumstartm) / 12 * jaar + int(datumstartY) * jaar
                totalt = int(tijdHt) * 3600 + int(tijdMt) * 60 + int(tijdSt) + int(datumdt) * dag + int(
                    datummt) / 12 * jaar + int(datumYt) * jaar

                gehuurdtijdtotal = totalt - total
                gehuurdtijd = gehuurdtijdtotal
                totalY = gehuurdtijd // (jaar)
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

                prijs = gehuurdtijdtotal // (60 * 15) * 0.2 + 1
                prijsafg = round(prijs,2)
                self.regel_verwijderen()

                terugbrengentext = ('U heeft de fiets voor {} {}, {} {}, {} {}, {} {}, {} {} en {} {} gehuurd, dat kost u {} euro'.format(
                    int(totalY), jaren, int(totalm), maanden, int(totald), dagen, int(totalH), uren, int(totalM),
                    minuten, int(totalS), seconden, str(prijsafg)))
                showinfo(title='Fiets Teruggebracht', message=terugbrengentext)
                return self.menu2()

        if gelukt != 1:
            self.infotext = (
                'U kan niet de fiets terugbrengen, omdat u geen fiets heeft gehuurd')
            showinfo(title='Hulp QR', message=self.infotext)

    def infopopup(self):
        """
        De popup voor persoonlijke informatie. Hij print je naam, achternaam, ov en telefoornummer. Ook checkt hij of je
        een fiets hebt gehuurd en/of gestald. Dit zet hij er ook in.
        """
        ingelogd = open('Ingelogd.txt', 'r')
        line = ingelogd.readlines()
        for lines in line:
            x = lines.split(';')

        stalling = open('Stallen.txt', 'r')
        zin = stalling.readlines()

        for zinnen in zin:
            k = zinnen.split(';')
            if k[0] == x[0] and k[1] == x[1]:
                self.stal = k[10]
            else:
                self.stal = '\\'

        stalling = open('Huurgegevens.txt', 'r')
        regel = stalling.readlines()

        for regels in regel:
            r = regels.split(';')
            if r[0] == x[0] and r[1] == x[1]:
                self.huur = 'Ja'
            else:
                self.huur = 'Nee'

        try:
            if self.huur == 'Ja':
                pass
        except AttributeError:
            self.huur = 'Nee'

        try:
            if self.stal == '\\':
                pass
        except AttributeError:
            self.stal = '\\'

        self.infotext = (
                'Geregistreerde naam: ' + self.naam + ' ' + self.achternaam + '\n' + 'Geregisteerd telefoon nummer: ' + self.tel + '\n' + 'Geregisteerde OV: ' + self.ov + '\n' + 'Stallingsplek: ' + str(
            self.stal) + '\n' + 'Fiets Gehuurd: ' + self.huur + '\n' + 'Om wachtwoord te veranderen, druk in het menu op wachtwoord veranderen')
        showinfo(title='Stallen', message=self.infotext)

        self.stal = '\\'
        self.huur = 'Nee'

    def InfoEigenaar(self):
        """
        De informatie van de ingelogde persoon, wordt gebruikt in de informatie popup.
        """
        gegevens = open('Ingelogd.txt', 'r')
        gegeven = gegevens.readlines()
        for item in gegeven:
            regel = item.split(';')
            self.naam = regel[0]
            self.achternaam = regel[1]
            self.tel = regel[3]
            self.ov = regel[4]
            self.infopopup()

    def QRHulpPopup(self):
        """
        De popup met hulp voor gebruik van de QR.
        """
        self.infotext = (
                    'Om een QR te scannen moet u een QR of Barcode scanner downloaden op uw smartphone. '
                    'Na het scannen krijgt u de code te zien, bewaar deze om later je fiets weer op te kunnen halen.')
        showinfo(title='Hulp QR', message=self.infotext)

    def OphalenPopup(self):
        """
        Hier wordt gechecked of de ingevoerde QR-Code gelijkstaat aan de QR-Code die bij het stallen gegeven was.
        Daarna haalt hij de fiets uit Stallen.txt.
        """
        counter = 0
        infile = open('Ingelogd.txt', 'r')
        ilines = infile.readlines()
        for iline in ilines:
            inlog = iline.split(';')
        infile.close()

        readfile = open('Stallen.txt', 'r')
        infile2 = readfile.readlines()
        for lines2 in infile2:
            stalgegevens = lines2.split(';')
            if inlog[0] == stalgegevens[0] and inlog[1] == stalgegevens[1] and inlog[4].strip('\n') == stalgegevens[9]:
                counter = 1
                stalnummer = stalgegevens[10].strip('\n')
                codegegeven = stalgegevens[2]

        if counter == 1:
            if self.code.get() != codegegeven:
                return showwarning(title='Fout', message='De ingevulde code is onjuist')
            else:
                self.infotext = (
                        'Uw fiets staat op plek ' + stalnummer + '. U kunt uw fiets meenemen.')
                showinfo(title='Ophaal Plek', message=self.infotext)
                readfile.close()

            lijst = []

            for regel in infile2:
                x = regel.split(';')
                counter2 = 0
                if inlog[0] == x[0] and inlog[1] == x[1] and inlog[4].strip('\n') == x[9]:
                    counter2 += 1
                if counter2 == 0:
                    lijst.append(regel)

            wfile = open('Stallen.txt', 'w')
            for gegevens in range(len(lijst)):
                wfile.write(lijst[gegevens])
            return self.menu2()
        else:
            return showwarning(title='Fout', message='U heeft geen fiets gestald.')

    def Fietsophalen(self):
        """
        Creëert de GUI voor fietsophalen.
        """
        self.top.withdraw()
        self.top = Toplevel()
        self.top.title('Ophalen')
        self.top.wm_iconbitmap('ns.ico')
        self.top.geometry("1280x720")
        self.top.configure(bg='gold')

        windowWidth = self.top.winfo_reqwidth()
        windowHeight = self.top.winfo_reqheight()
        positionRight = int(self.top.winfo_screenwidth() / 4 - windowWidth / 1.5)
        positionDown = int(self.top.winfo_screenheight() / 4 - windowHeight / 1.5)
        self.top.geometry("+{}+{}".format(positionRight, positionDown))

        photo = PhotoImage(master=self.top, file="ns.png")
        w = Label(self.top, image=photo, bg='gold')
        w.photo = photo
        w.pack(pady=25)

        self.label = Label(self.top, text='Uw QR Code')
        self.label.config(font=("Arial", 16),bg='gold', fg='blue4' )
        self.label.pack(fill=X, padx=25, pady=50)

        self.code = Entry(master=self.top)
        self.code.pack(fill=X, padx=300)

        self.Enterbutton = Button(master=self.top, text='Enter', command=self.OphalenPopup,
                                      bg='DodgerBlue2', relief=FLAT, font='Arial', fg='white',
                                      width=40)
        self.Enterbutton.pack(fill=X, padx=600, pady=25)

        self.Closebutton = Button(master=self.top, text='Terug', command=self.menu2,
                                  bg='goldenrod', relief=FLAT, font='Arial', fg='blue4',
                                  width=40)
        self.Closebutton.pack(fill=X, padx=600)

    def Uitloggen(self):
        """
        Leegt Ingelogd.txt voor de volgende gebruiker.
        """
        readfile = open('Ingelogd.txt','w')
        readfile.close()
        self.exit()

    def WachtwoordVeranderen(self):
        """
        Checked of oude wachtwoord overeenkomt met wat is ingevoerd,
        of de ov overeenkomt met de gegevens,
        of het nieuwe wachtwoord 2 keer hetzelfde is ingevoerd en
        write het nieuwe wachtwoord in Gegevens.txt en Ingelogd.txt
        """
        if self.ovfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.oudwwfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')
        if self.nieuwwwfield.get() == '':
            return showwarning(title='Leeg', message='Vul alle velden in alstublieft')

        ov = self.ovfield.get()
        ww = self.oudwwfield.get()
        ww2 = self.nieuwwwfield.get()

        result = ''

        for i in range(0, len(ww)):
            result = result + chr(ord(ww[i]) - 4)

        ingelogd = open('Ingelogd.txt','r')
        line = ingelogd.readlines()
        for lines in line:
            x = lines.split(';')
            if not ov == x[4].strip('\n'):
                return showwarning(title='Error', message='Het ingevulde OV is niet correct.')
            if not result == x[2]:
                return showwarning(title='Wachtwoord', message='Het ingevoerde oude wachtwoord is niet correct.')
            if len(ww2) < 6:
                return showwarning(title='Wachtwoord', message='Het nieuwe wachtwoord moet minstens 6 karakters bevatten.')
            if self.nieuwwwfield.get() != self.nieuwwwopnieuwfield.get():
                return showwarning(title='Ongelijk', message='De wachtwoorden zijn ongelijk')

        if ov.isdigit():
            nummer = ov
        else:
            nummer = ' '
        if ov is not nummer:
            return showwarning(title='OV', message='OV mag alleen nummers bevatten')

        if len(ov) is not 4:
            return showwarning(title='OV', message='Het OV moet 4 nummers bevatten')

        result2 = ''

        for i in range(0, len(ww2)):
            result2 = result2 + chr(ord(ww2[i]) - 4)

        infile = open('Gegevens.txt', 'r')
        regel = infile.readlines()
        lijst = []
        for zinnen in regel:
            counter = 0
            s = zinnen.split(';')
            if s[0] == x[0] and s[1] == x[1] and s[4] == x[4]:
                counter += 1
            if counter == 0:
                lijst.append(zinnen)

            else:
                zinnen2 = s[0] + ';' + s[1] + ';' + result2 + ';' + s[3] + ';' + s[4]
                lijst.append(zinnen2)

        infile.close()

        write = open('Gegevens.txt','w')
        for regels in range(len(lijst)):
            write.write(lijst[regels])
        write.close()

        fopen = open('Ingelogd.txt','r')
        lees = fopen.readlines()
        for lezen in lees:
            h = lezen.split(';')
        fopen.close()

        ww3 = open('Ingelogd.txt','w')
        gegevens = h[0] + ';' + h[1] + ';' + result2 + ';' + h[3] + ';' + h[4]
        ww3.write(gegevens)
        ww3.close()

        showwarning(title='Wachtwoord veranderd', message='Wachtwoord Succesvol veranderd!')
        return self.menu2()

    def WachtwoordVeranderenWindow(self):
        """
        Creëert de GUI voor het wachtwoord veranderen.
        """
        self.top.withdraw()
        self.top = Toplevel()
        self.top.title("Wachtwoord Veranderen")
        self.top.wm_iconbitmap('ns.ico')
        self.top.geometry("1280x720")
        self.top.configure(bg='gold')

        windowWidth = self.top.winfo_reqwidth()
        windowHeight = self.top.winfo_reqheight()
        positionRight = int(self.top.winfo_screenwidth() / 4 - windowWidth / 1.5)
        positionDown = int(self.top.winfo_screenheight() / 4 - windowHeight / 1.5)
        self.top.geometry("+{}+{}".format(positionRight, positionDown))

        self.label = Label(self.top, text='')
        self.label.grid(row=0, column=20, ipadx=170, sticky=W, pady=50)
        self.label.config(bg='gold')

        self.label = Label(self.top, text='Laatste 4 cijfers van uw OV')
        self.label.grid(row=1, column=20, ipadx=170, sticky=W)
        self.label.config(bg= 'gold',font=("Arial", 16))

        self.label = Label(self.top, text='Oud Wachtwoord')
        self.label.grid(row=2, column=20, ipadx=170, sticky=W)
        self.label.config(bg= 'gold',font=("Arial", 16))

        self.label = Label(self.top, text='Nieuw Wachtwoord')
        self.label.grid(row=3, column=20, ipadx=170, sticky=W)
        self.label.config(bg= 'gold',font=("Arial", 16))

        self.label = Label(self.top, text='Nieuw Wachtwoord Opnieuw')
        self.label.grid(row=4, column=20, ipadx=170, sticky=W)
        self.label.config(bg='gold', font=("Arial", 16))

        self.ovfield = Entry(master=self.top)
        self.ovfield.grid(row=1, column=21, pady=20)

        self.oudwwfield = Entry(master=self.top, show='*')
        self.oudwwfield.grid(row=2, column=21, pady=20)

        self.nieuwwwfield = Entry(master=self.top, show='*')
        self.nieuwwwfield.grid(row=3, column=21, pady=20)

        self.nieuwwwopnieuwfield = Entry(master=self.top, show='*')
        self.nieuwwwopnieuwfield.grid(row=4, column=21, pady=20)

        self.okbutton = Button(self.top, text='Wachtwoord Veranderen', command=self.WachtwoordVeranderen,
                                   bg='DodgerBlue2', relief=FLAT, font='Arial',fg='white',
                                   width=40)
        self.okbutton.grid(row=6, column=21, sticky=E, pady=10)

        self.terugbutton = Button(self.top, text='Terug', command=self.menu2,
                                   bg='goldenrod', relief=FLAT, font='Arial',
                                   width=40)
        self.terugbutton.grid(row=7, column=21, sticky=E)

if __name__ == "__main__":
    window = Window(None)
    window.geometry('1280x720')
    window.title('Home')
    window.wm_iconbitmap('ns.ico')
    window.configure(bg='gold')

    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    positionRight = int(window.winfo_screenwidth() / 4 - windowWidth / 1.5)
    positionDown = int(window.winfo_screenheight() / 4 - windowHeight / 1.5)
    window.geometry("+{}+{}".format(positionRight, positionDown))

    window.mainloop()