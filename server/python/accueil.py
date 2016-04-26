from bottle import route, run, template, get, post, request
import bottle
import sqlite3
import os
import hashlib
import sys
import genererBD
import FunctionDataBase

bottle.TEMPLATE_PATH.insert(0, "../template/")

DATA_PATH = '../../Data Base/DataBase.db'


@get('/') # ==> @route('/')
def index():
	"""
		test
	"""
	# if the database already exists
	if os.path.isfile(DATA_PATH):
		# informations from database administrators are selected
		admins = FunctionDataBase.selectAdmin()
		
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
			


@post('/')
def index():
	
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
			# the password is encrypted
			hash_object = hashlib.sha1(passwordCreate.encode())
			hex_digPassword = hash_object.hexdigest()
			
			# the administrator that has been just created is inserted in database
			FunctionDataBase.insertAdmin(nomCreate,hex_digPassword)

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
			# the password linked to the pseudo is selected (it's a sqlite3.Cursor object)
			bdPassword = FunctionDataBase.selectPassAdmin(nom)
			
			# variable that count the number of administrators (number of line in database)
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
				# the password seized is encrypted in order to compare this in database
				hash_object = hashlib.sha1(password.encode())
				hex_digPassword = hash_object.hexdigest()
				
				# if there are different
				if(hex_digPassword != passwordStocker):
					return template('accueil',erreur="Le mot de passe ou le login est erroné.",bd="",admin="")
				# if not, if there are equals 
				else:
					# everything is selected from Admin table in database (still a sqlite3.Cursor object)
					admins = FunctionDataBase.selectAdmin()
					
					# ID linked with the pseudo seized is selected (still a sqlite3.Cursor object)
					bdID = FunctionDataBase.selectIdAdmin(nom)
					
					# the cursor sqlite3 object is traversed containing the ID
					for j in bdID:
						idPers = j[0]
					
					listeAdmin = []
					
					# the cursor sqlite3 object is traversed containing all informations on all administrators
					for personnes in admins:
						# for each line in Admin table, information will be add in this array
						personne = []
						# all informations concerning one administrator (ID, pseudo, password) is traversed
						for information in personnes:
							# an array on these informations is created (so 3 parts)
							personne.append(information)
						# an array of array is got
						listeAdmin.append(personne)
								
					return template('admin',cles=passwordStocker, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="",generation="")
			

@get('/creation')
def index():

	# if the database already exists
	if os.path.isfile(DATA_PATH):
		return template('accueil',erreur="La base de donnée est déjà existante",bd="",admin="")
	# if not, if the database does not exist
	else:
		listeAdmin = []
		# all tables for the database are created
		genererBD.test(listeAdmin)
		return template('accueil',erreur="La base a bien été créé",bd="",admin="True")


@get('/admin')
def index():

	# if the database already exists
	if os.path.isfile(DATA_PATH):
		return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
	# if not, if the database does not exist
	else:
		return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="false",admin="")


@post('/admin')
def index():

	# contain the password of the administrator when he logged
	password = request.forms.get('cles')
	# contain the pseudo of the administrator when he logged
	nom = request.forms.get('clesVerification')
	
	# ID linked with the pseudo is selected (it's a sqlite3.Cursor object)
	idAdmin = FunctionDataBase.selectIdWithpassAdmin(nom,password)
	
	# variable that count the number of administrators (number of line in database)
	i=0
	
	# the cursor sqlite3 object is traversed containing all informations on all administrators
	for j in idAdmin:
		i = i+1

	# if the number of administrator is equal to 0 (there is no lines in database)
	if(i == 0):
		return template('accueil',erreur="Merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
	# if not, if there is (are) administrators in database
	else:
		# the type of the form is recovered to know which action will be realised
		types = request.forms.get('types')
		
		# the id of the logged administrator is recovered
		idPers = request.forms.get('idPers')
		
		# the id of the logged administrator is recovered (will be usefull to remove an administrator)
		idSelect = request.forms.get('idSelect')
		
		# everything is selected from the Admin table
		admins = FunctionDataBase.selectAdmin()
			
		listeAdmin = []
		
		# the cursor sqlite3 object is traversed containing all informations on all administrators
		for personnes in admins:
			# for each line in Admin table, information will be add in this array
			personne = []
			# all informations concerning one administrator (ID, pseudo, password) is traversed
			for information in personnes:
				# an array on these informations is created (so 3 parts)
				personne.append(information)
			# an array of array is got 
			listeAdmin.append(personne)
		
		# if the focus form is this to change the password of one administrator
		if(types == "modification"):
			# the new password seized for the administrator is recovered
			newPassword = request.forms.get('newPassword')
						
			# if the new password is empty	
			if(newPassword == ""):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Merci de rentrer un mot de passe",creation="",generation="")
			# if not, if it's all right
			else:	
				hash_object = hashlib.sha1(newPassword.encode())
				hex_digPassword = hash_object.hexdigest()
						
				# the new password is edited in the database
				FunctionDataBase.updatePassAdmin(idSelect,hex_digPassword)

				return template('admin',cles=hex_digPassword, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Le mot de passe de l'administrateur "+nom+" a bien été modifié",creation="",generation="")
		
		# if the focus form is this to delete an administrator
		elif(types == "delete"):
			# if the administrator wanting to be deleted is the one currently logged
			if(idSelect == idPers):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Vous ne pouvez pas supprimer "+nom+" car il est actuellement connecté",creation="",generation="")
			# if not, he isn't
			else:
				# the pseudo of the administrator that will be remove is selected (it's a sqlite3.Cursor object)
				nomPersDel = FunctionDataBase.selectNomAdmin(idSelect)
				
				# inside this object, the pseudo is recovered
				for i in nomPersDel:
					nomDel = i[0]
				
				# the administrator is deleted as well
				FunctionDataBase.delAdmin(idSelect)
				
				# everything is selected from the Admin table
				admins = FunctionDataBase.selectAdmin()
			
				listeAdmin = []
				
				# the cursor sqlite3 object is traversed containing all informations on all administrators
				for personnes in admins:
					# for each line in Admin table, information will be add in this array
					personne = []
					# all informations concerning one administrator (ID, pseudo, password) is traversed
					for information in personnes:
						# an array on these informations is created (so 3 parts)
						personne.append(information)
					# an array of array is got 
					listeAdmin.append(personne)
				

				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information=nomDel+" a bien été supprimé",creation="",generation="")
		
		# if the focus form is this to add an administrator
		elif(types == "add"):
			# the pseudo of the new administrator is recovered
			nomCreate = request.forms.get('nom')
			# the password of the new administrator is recovered
			passwordCreate = request.forms.get('password')
			
			# if the pseudo is empty
			if(nomCreate == ""):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="Le nom de l'administrateur est inexistant",generation="")
			# if not, if the password is empty
			elif(passwordCreate == ""):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="Le mot de passe pour " + nomCreate+ " est inexistant",generation="")
			# if not, if it's all right
			else:
				# the password is encrypted
				hash_object = hashlib.sha1(passwordCreate.encode())
				hex_digPassword = hash_object.hexdigest()
				
				# the ID linked with the pseudo is selected (it's a sqlite3.Cursor object)
				nomPersCreate = FunctionDataBase.selectIdAdmin(nomCreate)
				
				# variable that count the number of administrators (number of line in database)
				i=0
	
				# the sqlite3.Cursor object is traversed 
				for j in nomPersCreate:
					i = i+1
				
				# if there's something in this object, it's that the pseudo is already used
				if(i != 0):
					return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " existe déjà, veuillez rentrer un autre nom",generation="")
				
				# the new administrator and his password are inserted into database
				FunctionDataBase.insertAdmin(nomCreate,hex_digPassword)
				
				# everything is selected from the Admin table
				admins = FunctionDataBase.selectAdmin()
				
				listeAdmin = []
				
				# the cursor sqlite3 object is traversed containing all informations on all administrators
				for personnes in admins:
					# for each line in Admin table, information will be add in this array
					personne = []
					# all informations concerning one administrator (ID, pseudo, password) is traversed
					for information in personnes:
						# an array on these informations is created (so 3 parts)
						personne.append(information)
					# an array of array is got 
					listeAdmin.append(personne)
					
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " a bien été créé",generation="")
		
		#if the focus form is this to regenerate the CSV
		# for example, if the CSV is edited by removing some lines, the database could be regenerate to update the informations for users
		elif(types == "generation"):
			# everything is selected from the Admin table
			admins = FunctionDataBase.selectAdmin()
				
			listeAdmin = []
			
			# the cursor sqlite3 object is traversed containing all informations on all administrators
			for personnes in admins:
				# for each line in Admin table, information will be add in this array
				personne = []
				# all informations concerning one administrator (ID, pseudo, password) is traversed
				for information in personnes:
					# an array on these informations is created (so 3 parts)
					personne.append(information)
				# an array of array is got 
				listeAdmin.append(personne)
			
			# the database is removed
			os.remove(DATA_PATH)
			# the it's regenerate
			genererBD.test(listeAdmin)
			
			return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="",generation="La base a bien été mise à jour")


@get('/recherche') # ==> @route('/recherche')
def index():
	
	liste = []

	# ActLib attribute is selected from Activite table
	activites = FunctionDataBase.selectActivite('ActLib')

	# all activities are traversed 
	for i in activites:
		# check if the current element is in the list
		present = i[0] in liste 
		# if the current element isn't present in the list
		if(present == False):
			# it's add to the list
			liste.append(i[0])
	
	# the list is sorted
	liste.sort()
	# the head of the column of the CSV is removed
	liste.remove('ActLib')

	entrainement = []

	# ActLib attribute is selected from Activite table
	nivact = FunctionDataBase.selectActivite('ActNivLib')

	# all levels are traversed 
	for j in nivact:
		# check if the current element is in the list
		present = j[0] in entrainement
		# if the current element isn't present in the list
		if(present == False):
			# it's add to the list
			entrainement.append(j[0])

	# the head of the column of the CSV is removed
	entrainement.remove('ActNivLib')
	# the list is sorted
	entrainement.sort()

	return template('formulaire',liste=liste, nivact=entrainement)

@post('/recherche')
def post():
	
	# each information necessary are recovered
	activite = request.forms.get('activite')
	codePostal = request.forms.get('codePostal')
	niveau = request.forms.get('niveau')
	handicap = request.forms.get('handicap')

	information = []

	# informations are selected according on what the user choose
	listeActivite = FunctionDataBase.listeActivite(activite,codePostal,niveau,handicap)
	
	# the cursor sqlite3 object is traversed containing all informations of the research
	for i in listeActivite:
		# all necessary information will be add in this array
		valeurListe = []
		# all informations concerning one response of the request made by the user
		for j in i:
			# an array on these informations is created 
			valeurListe.append(j)
		
		# informations linked to Equipement table are recovered (it's a cursor sqlite3 object)
		listeEquipement = FunctionDataBase.selectEquipement(valeurListe[1])

		# all informations concerning one request linked to Equipement
		for k in listeEquipement:
			# in this request
			for l in k:
				# each element are add in the list
				valeurListe.append(l)

		# if the user don't specify anything about handicap
		if(handicap != ""):
			listeInstallation = FunctionDataBase.selectAllInstTwoArg(valeurListe[9],handicap)
		# if not
		else:
			listeInstallation = FunctionDataBase.selectAllInstOneArg(valeurListe[9])

		# all informations concerning one request linked to Installation
		for m in listeInstallation:
			# in this request
			for n in m:
				# each element are add in the list
				valeurListe.append(n)

		# if the list length is out of 20, informations are added to the list because 
		# all informations must be taken into account
		if(len(valeurListe) > 20):
			information.append(valeurListe)
			
	return template('resultat',information = information)

@get('/recherche/<id>')
def index(id):

	information =[]

	# everything is selected with one specific ID
	listeActivite = FunctionDataBase.selectAllActivite(int(id))

	# the cursor sqlite3 object is traversed containing all informations of the research
	for i in listeActivite:
		# all necessary information will be add in this array
		valeurListe = []
		# all informations concerning one response of the request made by the user
		for j in i:
			# an array on these informations is created 
			information.append(j)
	
		# informations linked to Equipement table are recovered (it's a cursor sqlite3 object)
		listeEquipement = FunctionDataBase.selectAllEquipement(information[1])

		# all informations concerning one request linked to Equipement
		for k in listeEquipement:
			# in this request
			for l in k:
				# each element are add in the list
				information.append(l)

		# informations linked to Installation table are recovered (it's a cursor sqlite3 object)
		listeInstallation = FunctionDataBase.selectAllInstallation(information[9])

		# all informations concerning one request linked to Installation
		for m in listeInstallation:
			# in this request
			for n in m:
				# each element are add in the list
				information.append(n)

	return template('carte',information = information)

# lauching of the server
run(host='localhost', port=8080)