# coding: utf-8

import os
from bottle import template,request
import bottle
import hashlib

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Accueil():
	"""
	Corresponding to treatment for the first page the user/administrator will see
	"""

	def get_accueil(self,DATA_PATH,db):
		"""
		Permit to redirect the page to connexion or the creation of the data base
		"""
		# if the database already exists
		if os.path.isfile(DATA_PATH):
			conn = db.connect()
			# informations from database administrators are selected
			admins = db.selectAdmin(conn)
			
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

		# if not, if the database does not exist
		else:
			return template('accueil',erreur="Aucune base de données présente sur le site",bd="false",admin="")

	def post_accueil(self,db):
		"""
		Permit to trate the case of 
			the click on the button allowing the creation of an administrator  
			or to check authentication
		"""
		
		# connexion to the database
		conn = db.connect()
	
		# informations from form are recovered (whether administrator creation, whether authentication)
		types = request.forms.get('types')

		# if it's the administrator creation form
		if(types == "create"):

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
				db.insertAdmin(nomCreate,hex_digPassword,conn)

				return template('accueil',erreur="L'administrateur a bien été créé",bd="",admin="")
					
		# if not, if it's the administrator authentication form	
		else:
			conn = db.connect()

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
				bdPassword = db.selectPassAdmin(nom,conn)
				
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
						admins = db.selectAdmin(conn)
						
						# ID linked with the pseudo seized is selected (still a sqlite3.Cursor object)
						bdID = db.selectIdAdmin(nom,conn)
						
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