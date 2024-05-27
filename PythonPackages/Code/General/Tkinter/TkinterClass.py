# Tkinter class

import requests
import tkinter as tk

class Menu_Leiste(tk.Menu):
	def __init__(self, parent):
		tk.Menu.__init__(self, parent)	
		
		Datei_Menu = tk.Menu(self, tearoff=False)
		self.add_cascade(label = "Datei", menu = Datei_Menu)
		Datei_Menu.add_command(label = "Beenden", command = self.quit, accelerator="Alt+F4")

class Loginerfolg(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.Widgets()	
		
	def Widgets(self):
		self.message_erfolg = tk.Message(self, text="Sie haben sich erfolgreich eingeloggt.", width=160, justify="center")
		self.message_erfolg.grid(row=0, column=0)

class Loginframe(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.Widgets()	
		
	def Widgets(self):	
        self.message_beschreibung = tk.Message(self, text="Gib Deine Logindaten fuer Heise Online ein und druecke dann den Button.", width=240, justify="center")
        
        self.label_benutzername = tk.Label(self, text="Benutzername:")
		self.label_passwort = tk.Label(self, text="Passwort:")
		
		self.entry_benutzername = tk.Entry(self, width=15)
		self.entry_passwort = tk.Entry(self, show="*", width=15)

		self.button_login = tk.Button(self, text="Einloggen", command = self.Button_login_geklickt)
		self.parent.bind('<Return>', self.Button_login_geklickt)
		
		self.message_beschreibung.grid(row=0, column=0, columnspan=2)
		self.label_benutzername.grid(row=1, column=0, sticky="e")
		self.label_passwort.grid(row=2, column=0, sticky="e")
		self.entry_benutzername.grid(row=1, column=1, sticky="w")
		self.entry_passwort.grid(row=2, column=1, sticky="w")		
		self.button_login.grid(row=3, column=0, columnspan=2)
		
		self.entry_benutzername.focus()
	
	def Button_login_geklickt(self, event=None):
		self.benutzername = self.entry_benutzername.get()
		self.passwort = self.entry_passwort.get()
		
		self.fake_browser = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
		self.login_daten = {"username":self.benutzername, "password":self.passwort, "action":"/sso/login/login"}
		
		self.login = requests.Session().post(url="https://www.heise.de/sso/login/login", data=self.login_daten, headers=self.fake_browser)
		
		if "Der Benutzername oder das Passwort ist falsch." in self.login.text:
			self.message_beschreibung.config(text="Fehler: Der Benutzername oder das Passwort ist falsch.", width=160, fg="red")
		else:
			self.destroy()
			self.parent.loginerfolg.grid(row=0, column=0)
		
		
class Programm(tk.Tk):
	def __init__(self, parent):
		tk.Tk.__init__(self, parent)
		self.parent = parent

		self.title("Heise-Online-Login")
		self.minsize(300, 130) 
		self.resizable(width=False, height=False)
		
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		
		self.loginframe = Loginframe(self)
		self.loginerfolg = Loginerfolg(self)
		
		self.loginframe.grid(row=0, column=0)
		
		self.config(menu=Menu_Leiste(self))

programm=Programm(None)
programm.mainloop()