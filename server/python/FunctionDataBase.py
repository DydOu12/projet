import sqlite3


DATA_PATH = '../../Data Base/DataBase.db'

def connect():
	"""

	"""
	return sqlite3.connect(DATA_PATH)

def CreateTableAdmin():
	conn = connect()
	conn.execute('''CREATE TABLE Admin 
	(ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom TEXT, Password TEXT)''')

def selectAdmin():
	conn = connect()
	return conn.execute('SELECT * FROM Admin')

def insertAdmin(nom,password):
	conn = connect()
	conn.execute('''INSERT INTO Admin (Nom,Password) VALUES (?,?)''',(nom,password))
	conn.commit()

def selectPassAdmin(nom):
	conn = connect()
	return conn.execute('SELECT Password FROM Admin WHERE NOM=:Nom',{"Nom": nom})

def selectIdAdmin(nom):
	conn = connect()
	return conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom',{"Nom": nom})

def selectIdWithpassAdmin(nom,password):
	conn = connect()
	return conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom AND Password=:Password',{"Nom": nom,"Password":password})

def updatePassAdmin(ids,password):
	conn = connect()
	conn.execute('UPDATE Admin SET Password=:Password WHERE ID=:ID',{"Password":password,"ID":ids})		
	conn.commit()

def selectNomAdmin(idSelect):
	conn = connect()
	return conn.execute('SELECT Nom FROM Admin WHERE ID=:ID',{"ID":idSelect})

def delAdmin(idSelect):
	conn = connect()
	conn.execute('DELETE FROM Admin WHERE ID=:ID',{"ID":idSelect})
	conn.commit()



def selectActivite(act):
	conn = connect()
	return conn.execute('SELECT '+act+' FROM Activite')

def listeActivite(activite,codePostal,niveau,handicap):
	conn = connect()
	if(activite == "" and codePostal != "" and niveau != ""):
		return conn.execute("SELECT * FROM Activite WHERE ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ComInsee":int(codePostal),"ActNivLib":niveau})
	elif(codePostal == "" and activite != "" and niveau != ""):
		return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ActNivLib=:ActNivLib", {"ActLib":activite,"ActNivLib":niveau})
	elif(niveau == "" and activite != "" and codePostal != ""):
		return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ComInsee=:ComInsee", {"ActLib":activite,"ComInsee":int(codePostal)})
	elif(activite == "" and codePostal == "" and niveau != ""):
		return conn.execute("SELECT * FROM Activite WHERE ActNivLib=:ActNivLib", {"ActNivLib":niveau})
	elif(activite == "" and niveau == "" and codePostal != ""):
		return conn.execute("SELECT * FROM Activite WHERE ComInsee=:ComInsee", {"ComInsee":int(codePostal)})
	elif(codePostal == "" and niveau == "" and activite != ""):
		return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib", {"ActLib":activite})
	elif(activite == "" and codePostal == "" and niveau == ""):
		return conn.execute("SELECT * FROM Activite")
	else:
		return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ActLib":activite,"ComInsee":int(codePostal),"ActNivLib":niveau})

def selectEquipement(idEquipement):
	conn = connect()
	return conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": idEquipement})

def selectAllInstTwoArg(InsNumeroInstall,AmenagementAccesHand):
	conn = connect()
	return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall AND AmenagementAccesHand=:AmenagementAccesHand", {"InsNumeroInstall": InsNumeroInstall,"AmenagementAccesHand":AmenagementAccesHand})

def selectAllInstTwoArg(InsNumeroInstall):
	conn = connect()
	return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall", {"InsNumeroInstall": InsNumeroInstall})

def selectAllActivite(id):
	conn = connect()
	return conn.execute("SELECT * FROM Activite WHERE ID=:ID", {"ID":int(id)})

def selectAllEquipement(EquipementID):
	conn = connect()
	return conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": EquipementID})

def selectAllInstallation(InsNumeroInstall):
	conn = connect()
	return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall ", {"InsNumeroInstall":InsNumeroInstall})