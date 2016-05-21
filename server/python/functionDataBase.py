# coding: utf-8

import sqlite3

class FunctionDataBase: 
	"""
	Corresponding to the actions linked to the database (creation, update, remove, ...)
	"""

	def __init__(self):
		"""
		Constructor defining the path of the database
		"""
		self.DATA_PATH = '../../Data Base/DataBase.db' 

	def connect(self):
		"""
		Permit to connect to the database
		"""
		return sqlite3.connect(self.DATA_PATH)

	def close(self,conn):
		"""
		Permit to disconnect to the database
		"""
		return conn.close()



	# ACTIVITY
	def createTableActivity(self,conn):
		"""
		Permit to create Activity table 
		"""
		conn.execute('''CREATE TABLE Activity 
		(ID INT PRIMARY KEY,EquipementID INT, ActCode INT,ActLib TEXT,ActNivLib TEXT,ComInsee INT)''')
	
	def addEntryActivity(self,ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee,conn):
		"""
		Permit to add lines in Activity table
		"""
		conn.execute('''INSERT INTO Activity (ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee) VALUES (?,?,?,?,?,?)''',(ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee))

	def selectActivity(self,act,conn):
		"""
		Permit to select on activity in Activity table
		"""
		return conn.execute('SELECT '+act+' FROM Activity')

	def listeActivity(self,activity,postalCode,level,handicap,conn):
		"""
		Permit to select activities according to parameters in Activity table
		"""
		if(activity == "" and postalCode != "" and level != ""):
			return conn.execute("SELECT * FROM Activity WHERE ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ComInsee":int(postalCode),"ActNivLib":level})
		elif(postalCode == "" and activity != "" and level != ""):
			return conn.execute("SELECT * FROM Activity WHERE ActLib =:ActLib AND ActNivLib=:ActNivLib", {"ActLib":activity,"ActNivLib":level})
		elif(level == "" and activity != "" and postalCode != ""):
			return conn.execute("SELECT * FROM Activity WHERE ActLib =:ActLib AND ComInsee=:ComInsee", {"ActLib":activity,"ComInsee":int(postalCode)})
		elif(activity == "" and postalCode == "" and level != ""):
			return conn.execute("SELECT * FROM Activity WHERE ActNivLib=:ActNivLib", {"ActNivLib":level})
		elif(activity == "" and level == "" and postalCode != ""):
			return conn.execute("SELECT * FROM Activity WHERE ComInsee=:ComInsee", {"ComInsee":int(postalCode)})
		elif(postalCode == "" and level == "" and activity != ""):
			return conn.execute("SELECT * FROM Activity WHERE ActLib =:ActLib", {"ActLib":activity})
		elif(activity == "" and postalCode == "" and level == ""):
			return conn.execute("SELECT * FROM Activity")
		else:
			return conn.execute("SELECT * FROM Activity WHERE ActLib =:ActLib AND ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ActLib":activity,"ComInsee":int(postalCode),"ActNivLib":level})
	
	def selectAllActivity(self,id,conn):
		"""
		Permit to select on line according to his ID in Activity table
		"""
		return conn.execute("SELECT * FROM Activity WHERE ID=:ID", {"ID":int(id)})



	# EQUIPEMENT
	def createTableEquipement(self,conn):
		"""
		Permit to create Equipement table
		"""
		conn.execute('''CREATE TABLE Equipement 
		(ID INT PRIMARY KEY,EquipementID INT, ComLib TEXT,InsNumeroInstall TEXT,InsNom TEXT,EquNom TEXT,EquipementTypeLib TEXT,EquGPSX REAL,EquGPSY REAL)''')

	def addEntryEquipement(self,ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY,conn):
		"""
		Permit to add lines in Equipement table
		"""
		conn.execute('''INSERT INTO Equipement (ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY)
		VALUES (?,?,?,?,?,?,?,?,?)''',(ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY))

	def selectAllEquipement(self,idEquipement,conn):
		"""
		Permit to select one line according to his ID in Equipement table
		"""
		return conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": idEquipement})



	# INSTALLATION
	def createTableInstallation(self,conn):
		"""
		Permit to create Installation table
		"""
		conn.execute('''CREATE TABLE Installation 
		(ID INT PRIMARY KEY,InsNumeroInstall INT, NomVoie TEXT,AmenagementAccesHand BOOLEAN,NbrEquip INT,PlaceParking INT)''')

	def addEntryInstallation(self,ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking,conn):
		"""
		Permit to add lines in Installation table
		"""
		conn.execute('''INSERT INTO Installation (ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking)
		VALUES (?,?,?,?,?,?)''',(ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking))

	def selectAllInstTwoArg(self,InsNumeroInstall,AmenagementAccesHand,conn):
		"""
		Permit to select one installation according to ID and handicap parameter in Installation table
		"""
		return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall AND AmenagementAccesHand=:AmenagementAccesHand", {"InsNumeroInstall": InsNumeroInstall,"AmenagementAccesHand":AmenagementAccesHand})

	def selectAllInstallation(self,InsNumeroInstall,conn):
		"""
		Permit to select one installation according to ID in Installation table
		"""
		return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall ", {"InsNumeroInstall":InsNumeroInstall})



	# ADMINISTRATION
	def createTableAdmin(self,conn):
		"""
		Permit to create Admin table
		"""
		conn.execute('''CREATE TABLE Admin 
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom TEXT, Password TEXT)''')

	def addEntryAdmin(self,Nom,Password,conn):
		"""
		Permit to add lines in Installation table
		"""
		conn.execute('''INSERT INTO Admin (Nom,Password) VALUES (?,?)''',(Nom,Password))
		conn.commit()

	def selectAdmin(self,conn):
		"""
		Permit to select all lines in Admin table
		"""
		return conn.execute('SELECT * FROM Admin')

	def selectPassAdmin(self,name,conn):
		"""
		Permit to select the password of one administrator according to his name in Admin table
		"""
		return conn.execute('SELECT Password FROM Admin WHERE NOM=:Nom',{"Nom": name})

	def selectIdAdmin(self,name,conn):
		"""
		Permit to select the ID of one administrator according to his name in Admin table
		"""
		return conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom',{"Nom": name})

	def selectIdWithpassAdmin(self,name,password,conn):
		"""
		Permit to select the ID of one administrator according to his name and his password in Admin table
		"""
		return conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom AND Password=:Password',{"Nom": name,"Password":password})

	def selectNomAdmin(self,idSelect,conn):
		"""
		Permit to select the name of one administrator according to his ID in Admin table
		"""
		return conn.execute('SELECT Nom FROM Admin WHERE ID=:ID',{"ID":idSelect})

	def updatePassAdmin(self,ids,password,conn):
		"""
		Permit to modify the password of one administrator according to his ID in Admin table
		"""
		conn.execute('UPDATE Admin SET Password=:Password WHERE ID=:ID',{"Password":password,"ID":ids})		
		conn.commit()

	def delAdmin(self,idSelect,conn):
		"""
		Permit to delete one administrator according to his ID in Admin table
		"""
		conn.execute('DELETE FROM Admin WHERE ID=:ID',{"ID":idSelect})
		conn.commit()


	

	
	


	