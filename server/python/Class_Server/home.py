# coding: utf-8

import os
from bottle import template,request
import bottle
import hashlib

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Home():
	"""
	Corresponding to treatment for the first page the user/administrator will see
	"""

	def get_home(self,DATA_PATH,db):
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
				return template('home',error="",bd="",admin="True")
			# if not, there is (are)
			else:
				return template('home',error="",bd="",admin="")

		# if not, if the database does not exist
		else:
			return template('home',error="Aucune base de données présente sur le site",bd="false",admin="")

	def post_home(self,db):
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

			nameCreated = request.forms.get('nameCreated')
			passwordCreated = request.forms.get('passwordCreated')
			
			# if the pseudo is empty
			if(nameCreated == ""):
				return template('home',error="Un nom est obligatoire pour l'administrateur",bd="",admin="True")
			# if the password is empty
			elif(passwordCreated == ""):
				return template('home',error="Un mot de passe est obligatoire pour l'administrateur",bd="",admin="True")
			# if it's OK
			elif(nameCreated != "" and passwordCreated != ""):
				# the password is encrypted
				hash_object = hashlib.sha1(passwordCreated.encode())
				hex_digPassword = hash_object.hexdigest()
				
				# the administrator that has been just created is inserted in database
				db.addEntryAdmin(nameCreated,hex_digPassword,conn)

				return template('home',error="L'administrateur a bien été créé",bd="",admin="")
					
		# if not, if it's the administrator authentication form	
		else:
			conn = db.connect()

			# the pseudo and the password seized by the user is recovered
			name = request.forms.get('name')
			password = request.forms.get('password')
			
			# if the pseudo is empty
			if(name == ""):
				return template('home',error="Un administrateur a un name",bd="",admin="")
			# if the password is empty
			elif(password == ""):
				return template('home',error="Mot de passe obligatoire",bd="",admin="")
			# if it's OK
			elif(name != "" and password != ""):
				# the password linked to the pseudo is selected (it's a sqlite3.Cursor object)
				bdPassword = db.selectPassAdmin(name,conn)
				
				# variable that count the number of administrators (number of line in database)
				i=0
				
				# the cursor sqlite3 object is traversed containing the password
				for j in bdPassword:
					# the number of administrator is incremented 
					i = i+1
					# the password in database is stored
					passwordStored = j[0]

				# if the number of administrator is equal to 0 (there is no lines in database)
				if(i == 0):
					return template('home',error="L'administrateur n'existe pas",bd="",admin="")
				# if not, if there is (are) administrators in database
				else:
					# the password seized is encrypted in order to compare this in database
					hash_object = hashlib.sha1(password.encode())
					hex_digPassword = hash_object.hexdigest()
					
					# if there are different
					if(hex_digPassword != passwordStored):
						return template('home',error="Le mot de passe ou le login est erroné.",bd="",admin="")
					# if not, if there are equals 
					else:
						# everything is selected from Admin table in database (still a sqlite3.Cursor object)
						admins = db.selectAdmin(conn)
						
						# ID linked with the pseudo seized is selected (still a sqlite3.Cursor object)
						bdID = db.selectIdAdmin(name,conn)
						
						# the cursor sqlite3 object is traversed containing the ID
						for j in bdID:
							idPers = j[0]
						
						listAdmin = []
						
						# the cursor sqlite3 object is traversed containing all informations on all administrators
						for people in admins:
							# for each line in Admin table, information will be add in this array
							person = []
							# all informations concerning one administrator (ID, pseudo, password) is traversed
							for information in people:
								# an array on these informations is created (so 3 parts)
								person.append(information)
							# an array of array is got
							listAdmin.append(person)
									
						return template('admin',keys=passwordStored, keysVerification=name,admin=listAdmin,idPers=idPers,information="",creation="",generation="")