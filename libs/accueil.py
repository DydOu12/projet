from bottle import route, run, template, get, post, request
import sqlite3
import os
import hashlib
import sys
import genererBD


@get('/') # ==> @route('/')
def index():
	"""
		test
	"""
	# if database exists
	if os.path.isfile('../BD/BaseDeDonnee.db'):
		# it connects into
		conn = sqlite3.connect('../BD/BaseDeDonnee.db')
		
		# informations from database administrators are selected
		admins = conn.execute('SELECT * FROM Admin')
		
		# variable that count the number of administrators (number if line in database)
		i = 0
		
		# for selected lines in database
		for pers in admins:
			# the number of administrator is incremented 
			i = i+1
		
		# if there's not administrators in database
		if(i == 0):
			return template('accueil',erreur="",bd="",admin="True")
		# if not, there is (are)
		else:
			return template('accueil',erreur="",bd="",admin="")
		
	# if the database does not exist 
	else:
		return template('accueil',erreur="",bd="false",admin="")
			


@post('/')
def index():
	# it connects to the database
	conn = sqlite3.connect('../BD/BaseDeDonnee.db')
	
	# informations from form are recovered (whether administrator creation, whether authentication)
	types = request.forms.get('types')
	
	# if it's the administrator creation form
	if(types == "create"):
		# the pseudo and the password 's new administrator
		nomCreate = request.forms.get('nomCreate')
		passwordCreate = request.forms.get('passwordCreate')
		
		# if the pseudo is empty
		if(nomCreate == ""):
			return template('accueil',erreur="Un nom est obligatoire pour l'administrateur",bd="",admin="True")
		# if the password is empty
		elif(passwordCreate == ""):
			return template('accueil',erreur="Un mot de passe est obligatoire pour l'administrateur",bd="",admin="True")
		# if it's OK
		elif(nomCreate != "" and passwordCreate != ""):
			
			# the password is crypted
			hash_object = hashlib.sha1(passwordCreate.encode())
			hex_digPassword = hash_object.hexdigest()
			
			# the administrator that has been just created is inserted in database
			conn.execute('''INSERT INTO Admin (Nom,Password) VALUES (?,?)''',(nomCreate,hex_digPassword))
			conn.commit()
			return template('accueil',erreur="L'administrateur a bien été créé",bd="",admin="")
			
	# if not, if it's the administrator authentication form
	else:
		# the pseudo and the password seized by the user is recovered
		nom = request.forms.get('nom')
		password = request.forms.get('password')
		
		# if the pseudo is empty
		if(nom == ""):
			return template('accueil',erreur="Un administrateur a un nom",bd="",admin="")
		# if the password is empty
		elif(password == ""):
			return template('accueil',erreur="Mot de passe obligatoire",bd="",admin="")
		# if it's OK
		elif(nom != "" and password != ""):
			# the password linked to the pseudo is selected (it's an sqlite3.Cursor object)
			bdPassword = conn.execute('SELECT Password FROM Admin WHERE NOM=:Nom',{"Nom": nom})

			# variable that count the number of administrators (number if line in database)
			i=0
			
			# the cursor sqlite3 object is traversed containing the password
			for j in bdPassword:
				# the number of administrator is incremented 
				i = i+1
				# the password in database is stored
				passwordStocker = j[0]

			# if the number of administrator is equal to 0 (there is no lines in database)
			if(i == 0):
				return template('accueil',erreur="L'administrateur n'existe pas",bd="",admin="")
			# if not, if there is (are) administrators in database
			else:
				# Vérifier si le mot de passe écrit encoder corresponds à celui en base
				
				hash_object = hashlib.sha1(password.encode())
				hex_digPassword = hash_object.hexdigest()
				
				# Si les mots de passe de correspondent pas alors message d'erreur
				
				if(hex_digPassword != passwordStocker):
					return template('accueil',erreur="Le mot de passe ou le login est erroné.",bd="",admin="")
				else:
					
					admins = conn.execute('SELECT * FROM Admin')
					
					bdID = conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom',{"Nom": nom})
					
					for j in bdID:
						idPers = j[0]
					
					listeAdmin = []
					
					for personnes in admins:
						personne = []
						for information in personnes:
							personne.append(information)
						listeAdmin.append(personne)
							
					
					return template('admin',cles=passwordStocker, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="",generation="")
			

@get('/creation')
def index():
	if os.path.isfile('../BD/BaseDeDonnee.db'):
		return template('accueil',erreur="La base de donnée est déjà existante",bd="",admin="")
	else:
		listeAdmin = []
		genererBD.test(listeAdmin)
		return template('accueil',erreur="La base a bien été créé",bd="",admin="True")


@get('/admin')
def index():
	if os.path.isfile('../BD/BaseDeDonnee.db'):
		return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
	else:
		return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="false",admin="")


@post('/admin')
def index():
	conn = sqlite3.connect('../BD/BaseDeDonnee.db')
	
	password = request.forms.get('cles')
	nom = request.forms.get('clesVerification')
	
	idAdmin = conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom AND Password=:Password',{"Nom": nom,"Password":password})
	
	i=0
	
	for j in idAdmin:
		i = i+1

	
	if(i == 0):
		return template('accueil',erreur="Merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
	else:
		types = request.forms.get('types')
		
		idPers = request.forms.get('idPers')
		
		idSelect = request.forms.get('idSelect')
		
		admins = conn.execute('SELECT * FROM Admin')
			
		listeAdmin = []
		
		for personnes in admins:
			personne = []
			for information in personnes:
				personne.append(information)
			listeAdmin.append(personne)
		
		if(types == "modification"):
			newPassword = request.forms.get('newPassword')
						
			if(newPassword == ""):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Merci de rentrer un mot de passe",creation="",generation="")
			else:	
				hash_object = hashlib.sha1(newPassword.encode())
				hex_digPassword = hash_object.hexdigest()
						
				conn.execute('UPDATE Admin SET Password=:Password WHERE ID=:ID',{"Password":hex_digPassword,"ID":idSelect})
				
				conn.commit()
				
				return template('admin',cles=hex_digPassword, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Le mot de passe de l'administrateur "+nom+" a bien été modifié",creation="",generation="")
			
		elif(types == "delete"):
			if(idSelect == idPers):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Vous ne pouvez pas supprimer "+nom+" car il est actuellement connecté",creation="",generation="")
			else:
				nomPersDel = conn.execute('SELECT Nom FROM Admin WHERE ID=:ID',{"ID":idSelect})
				
				for i in nomPersDel:
					nomDel = i[0]
					
				conn.execute('DELETE FROM Admin WHERE ID=:ID',{"ID":idSelect})
				
				conn.commit()
				
				admins = conn.execute('SELECT * FROM Admin')
			
				listeAdmin = []
				
				for personnes in admins:
					personne = []
					for information in personnes:
						personne.append(information)
					listeAdmin.append(personne)
				

				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information=nomDel+" a bien été supprimé",creation="",generation="")
		elif(types == "add"):
			
			nomCreate = request.forms.get('nom')
		
			passwordCreate = request.forms.get('password')
			
			if(nomCreate == ""):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="Le nom de l'administrateur est inexistant",generation="")
			elif(passwordCreate == ""):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="Le mot de passe pour " + nomCreate+ " est inexistant",generation="")
			else:
				hash_object = hashlib.sha1(passwordCreate.encode())
				hex_digPassword = hash_object.hexdigest()
				
				nomPersCreate = conn.execute('SELECT ID FROM Admin WHERE Nom=:Nom',{"Nom":nomCreate})
				
				i=0
	
				for j in nomPersCreate:
					i = i+1
					
				if(i != 0):
					return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " existe déjà, veuillez rentrer un autre nom",generation="")
				
				conn.execute('''INSERT INTO Admin (Nom,Password) VALUES (?,?)''',(nomCreate,hex_digPassword))
				
				conn.commit()
				
				admins = conn.execute('SELECT * FROM Admin')
				
				listeAdmin = []
				
				for personnes in admins:
					personne = []
					for information in personnes:
						personne.append(information)
					listeAdmin.append(personne)
					
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " a bien été créé",generation="")
				
		elif(types == "generation"):
			
			admins = conn.execute('SELECT * FROM Admin')
				
			listeAdmin = []
			
			for personnes in admins:
				personne = []
				for information in personnes:
					personne.append(information)
				listeAdmin.append(personne)
			
			os.remove("../BD/BaseDeDonnee.db")
			genererBD.test(listeAdmin)
			#os.system("../BD/genererBD.py")
			
			return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="",generation="La base a bien été mise à jour")



@get('/recherche') # ==> @route('/recherche')
def index():
	conn = sqlite3.connect('../BD/BaseDeDonnee.db')
	
	liste = []

	activites = conn.execute('SELECT ActLib FROM Activite')

	for i in activites:
		present = i[0] in liste 
		if(present == False):
			liste.append(i[0])
	
	liste.sort()
	liste.remove('ActLib')

	entrainement = []

	nivact = conn.execute('SELECT ActNivLib FROM Activite')

	for j in nivact:
		present = j[0] in entrainement
		if(present == False):
			entrainement.append(j[0])

	entrainement.remove('ActNivLib')
	entrainement.sort()

	return template('formulaire',liste=liste, nivact=entrainement)

@post('/recherche')
def post():
	conn = sqlite3.connect('../BD/BaseDeDonnee.db')
	
	activite = request.forms.get('activite')
	codePostal = request.forms.get('codePostal')
	niveau = request.forms.get('niveau')
	handicap = request.forms.get('handicap')

	information = []


	# listeActivite = conn.execute('''SELECT * FROM Activite WHERE ActLib=? AND ComInsee=?''', (activite,codePostal))
	if(activite == "" and codePostal != "" and niveau != ""):
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ComInsee":int(codePostal),"ActNivLib":niveau})
	elif(codePostal == "" and activite != "" and niveau != ""):
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ActNivLib=:ActNivLib", {"ActLib":activite,"ActNivLib":niveau})
	elif(niveau == "" and activite != "" and codePostal != ""):
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ComInsee=:ComInsee", {"ActLib":activite,"ComInsee":int(codePostal)})
	elif(activite == "" and codePostal == "" and niveau != ""):
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ActNivLib=:ActNivLib", {"ActNivLib":niveau})
	elif(activite == "" and niveau == "" and codePostal != ""):
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ComInsee=:ComInsee", {"ComInsee":int(codePostal)})
	elif(codePostal == "" and niveau == "" and activite != ""):
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib", {"ActLib":activite})
	elif(activite == "" and codePostal == "" and niveau == ""):
		listeActivite = conn.execute("SELECT * FROM Activite")
	else:
		listeActivite = conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ActLib":activite,"ComInsee":int(codePostal),"ActNivLib":niveau})

	for i in listeActivite:
		valeurListe = []
		for j in i:
			valeurListe.append(j)
	
		listeEquipement = conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": valeurListe[1]})

		for k in listeEquipement:
			for l in k:
				valeurListe.append(l)

		if(handicap != ""):
			listeInstallation = conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall AND AmenagementAccesHand=:AmenagementAccesHand", {"InsNumeroInstall": valeurListe[9],"AmenagementAccesHand":handicap})
		else:
			listeInstallation = conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall", {"InsNumeroInstall": valeurListe[9]})


		for m in listeInstallation:
			for n in m:
				valeurListe.append(n)

		if(len(valeurListe) > 20):
			information.append(valeurListe)
			
	
	return template('resultat',information = information)

@get('/recherche/<id>')
def index(id):
	
	conn = sqlite3.connect('../BD/BaseDeDonnee.db')

	information =[]

	listeActivite = conn.execute("SELECT * FROM Activite WHERE ID=:ID", {"ID":int(id)})

	for i in listeActivite:
		valeurListe = []
		for j in i:
			information.append(j)
	
		listeEquipement = conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": information[1]})

		for k in listeEquipement:
			for l in k:
				information.append(l)


		listeInstallation = conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall ", {"InsNumeroInstall": information[9]})

		for m in listeInstallation:
			for n in m:
				information.append(n)

	return template('carte',information = information)

run(host='localhost', port=8080)







