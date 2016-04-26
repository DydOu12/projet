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
	if os.path.isfile(DATA_PATH):
		
		admins = FunctionDataBase.selectAdmin()
		
		i = 0
		
		for pers in admins:
			i = i+1
			
		if(i == 0):
			return template('accueil',erreur="",bd="",admin="True")
		else:
			return template('accueil',erreur="",bd="",admin="")
			


@post('/')
def index():
	
	types = request.forms.get('types')
	
	if(types == "create"):
		
		nomCreate = request.forms.get('nomCreate')
		passwordCreate = request.forms.get('passwordCreate')
		
		if(nomCreate == ""):
			return template('accueil',erreur="Un nom est obligatoire pour l'administrateur",bd="",admin="True")
		elif(passwordCreate == ""):
			return template('accueil',erreur="Un mot de passe est obligatoire pour l'administrateur",bd="",admin="True")
		elif(nomCreate != "" and passwordCreate != ""):
			
			hash_object = hashlib.sha1(passwordCreate.encode())
			hex_digPassword = hash_object.hexdigest()
			
			# FunctionDataBase.CreateTableAdmin()
			FunctionDataBase.insertAdmin(nomCreate,hex_digPassword)

			return template('accueil',erreur="L'administrateur a bien été créé",bd="",admin="")
			
		
			
		
	else:
	
		nom = request.forms.get('nom')
		password = request.forms.get('password')
		
		if(nom == ""):
			return template('accueil',erreur="Un administrateur a un nom",bd="",admin="")
		elif(password == ""):
			return template('accueil',erreur="Mot de passe obligatoire",bd="",admin="")
		elif(nom != "" and password != ""):
		
			bdPassword = FunctionDataBase.selectPassAdmin(nom)
			
			i=0
			
			for j in bdPassword:
				i = i+1
				passwordStocker = j[0]

			
			if(i == 0):
				return template('accueil',erreur="L'administrateur n'existe pas",bd="",admin="")
			else:
				
				# Vérifier si le mot de passe écrit encoder corresponds à celui en base
				
				hash_object = hashlib.sha1(password.encode())
				hex_digPassword = hash_object.hexdigest()
				
				# Si les mots de passe de correspondent pas alors message d'erreur
				
				if(hex_digPassword != passwordStocker):
					return template('accueil',erreur="Le mot de passe ou le login est erroné.",bd="",admin="")
				else:
					
					admins = FunctionDataBase.selectAdmin()
					
					bdID = FunctionDataBase.selectIdAdmin(nom)
					
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
	if os.path.isfile(DATA_PATH):
		return template('accueil',erreur="La base de donnée est déjà existante",bd="",admin="")
	else:
		listeAdmin = []
		genererBD.test(listeAdmin)
		return template('accueil',erreur="La base a bien été créé",bd="",admin="True")


@get('/admin')
def index():
	if os.path.isfile(DATA_PATH):
		return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
	else:
		return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="false",admin="")


@post('/admin')
def index():
	
	password = request.forms.get('cles')
	nom = request.forms.get('clesVerification')
	
	idAdmin = FunctionDataBase.selectIdWithpassAdmin(nom,password)
	
	i=0
	
	for j in idAdmin:
		i = i+1

	
	if(i == 0):
		return template('accueil',erreur="Merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
	else:
		types = request.forms.get('types')
		
		idPers = request.forms.get('idPers')
		
		idSelect = request.forms.get('idSelect')
		
		admins = FunctionDataBase.selectAdmin()
			
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
						

				FunctionDataBase.updatePassAdmin(idSelect,hex_digPassword)

				return template('admin',cles=hex_digPassword, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Le mot de passe de l'administrateur "+nom+" a bien été modifié",creation="",generation="")
			
		elif(types == "delete"):
			if(idSelect == idPers):
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Vous ne pouvez pas supprimer "+nom+" car il est actuellement connecté",creation="",generation="")
			else:
				nomPersDel = FunctionDataBase.selectNomAdmin(idSelect)
				
				for i in nomPersDel:
					nomDel = i[0]
					
				FunctionDataBase.delAdmin(idSelect)
				
				admins = FunctionDataBase.selectAdmin()
			
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
				
				nomPersCreate = FunctionDataBase.selectIdAdmin(nomCreate)
				
				i=0
	
				for j in nomPersCreate:
					i = i+1
					
				if(i != 0):
					return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " existe déjà, veuillez rentrer un autre nom",generation="")
				
				FunctionDataBase.insertAdmin(nomCreate,hex_digPassword)
				
				admins = FunctionDataBase.selectAdmin()
				
				listeAdmin = []
				
				for personnes in admins:
					personne = []
					for information in personnes:
						personne.append(information)
					listeAdmin.append(personne)
					
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " a bien été créé",generation="")
				
		elif(types == "generation"):
			
			admins = FunctionDataBase.selectAdmin()
				
			listeAdmin = []
			
			for personnes in admins:
				personne = []
				for information in personnes:
					personne.append(information)
				listeAdmin.append(personne)
			
			os.remove(DATA_PATH)
			genererBD.test(listeAdmin)
			#os.system("../BD/genererBD.py")
			
			return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="",generation="La base a bien été mise à jour")



@get('/recherche') # ==> @route('/recherche')
def index():
	
	liste = []

	activites = FunctionDataBase.selectActivite('ActLib')

	for i in activites:
		present = i[0] in liste 
		if(present == False):
			liste.append(i[0])
	
	liste.sort()
	liste.remove('ActLib')

	entrainement = []

	nivact = FunctionDataBase.selectActivite('ActNivLib')

	for j in nivact:
		present = j[0] in entrainement
		if(present == False):
			entrainement.append(j[0])

	entrainement.remove('ActNivLib')
	entrainement.sort()

	return template('formulaire',liste=liste, nivact=entrainement)

@post('/recherche')
def post():
	
	activite = request.forms.get('activite')
	codePostal = request.forms.get('codePostal')
	niveau = request.forms.get('niveau')
	handicap = request.forms.get('handicap')

	information = []

	listeActivite = FunctionDataBase.listeActivite(activite,codePostal,niveau,handicap)
	
	for i in listeActivite:
		valeurListe = []
		for j in i:
			valeurListe.append(j)
	
		listeEquipement = FunctionDataBase.selectEquipement(valeurListe[1])

		for k in listeEquipement:
			for l in k:
				valeurListe.append(l)

		if(handicap != ""):
			listeInstallation = FunctionDataBase.selectAllInstTwoArg(valeurListe[9],handicap)
		else:
			listeInstallation = FunctionDataBase.selectAllInstOneArg(valeurListe[9])


		for m in listeInstallation:
			for n in m:
				valeurListe.append(n)

		if(len(valeurListe) > 20):
			information.append(valeurListe)
			
	
	return template('resultat',information = information)

@get('/recherche/<id>')
def index(id):

	information =[]

	listeActivite = FunctionDataBase.selectAllActivite(int(id))

	for i in listeActivite:
		valeurListe = []
		for j in i:
			information.append(j)
	
		listeEquipement = FunctionDataBase.selectAllEquipement(information[1])

		for k in listeEquipement:
			for l in k:
				information.append(l)


		listeInstallation = FunctionDataBase.selectAllInstallation(information[9])

		for m in listeInstallation:
			for n in m:
				information.append(n)

	return template('carte',information = information)

run(host='localhost', port=8080)