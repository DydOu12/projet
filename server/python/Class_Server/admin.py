# coding: utf-8

import os
from bottle import template, request
import bottle 
import hashlib
import generateDB

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Admin():
	"""
	Corresponding to actions made when you are an administrator
	"""

	def get_admin(self,DATA_PATH,db):
		"""
		Permit to know if administrators already exist
		"""

		# if the database already exists
		if os.path.isfile(DATA_PATH):
			return template('home',error="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
		# if not, if the database does not exist
		else:
			return template('home',error="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="false",admin="")

	def post_admin(self, DATA_PATH, db):
		"""
		Permit to treate the cases of delete, add, update an administrator
		and update the database (regeneration)
		"""

		# connexion to the database
		conn = db.connect()

		# contain the password of the administrator when he logged
		password = request.forms.get('keys')
		# contain the pseudo of the administrator when he logged
		name = request.forms.get('keysVerification')
		
		# ID linked with the pseudo is selected (it's a sqlite3.Cursor object)
		idAdmin = db.selectIdWithpassAdmin(name,password,conn)
		
		# variable that count the number of administrators (number of line in database)
		i=0
		
		# the cursor sqlite3 object is traversed containing all informations on all administrators
		for j in idAdmin:
			i = i+1

		# if the number of administrator is equal to 0 (there is no lines in database)
		if(i == 0):
			return template('home',error="Merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
		# if not, if there is (are) administrators in database
		else:
			# the type of the form is recovered to know which action will be realised
			types = request.forms.get('types')
			
			# the id of the logged administrator is recovered
			idPers = request.forms.get('idPers')
			
			# the id of the logged administrator is recovered (will be usefull to remove an administrator)
			idSelect = request.forms.get('idSelect')
			
			# everything is selected from the Admin table
			admins = db.selectAdmin(conn)
				
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
			
			# if the focus form is this to change the password of one administrator
			if(types == "modification"):
				conn = db.connect()

				# the new password seized for the administrator is recovered
				newPassword = request.forms.get('newPassword')
							
				# if the new password is empty	
				if(newPassword == ""):
					return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="Merci de rentrer un mot de passe",creation="",generation="")
				# if not, if it's all right
				else:	
					hash_object = hashlib.sha1(newPassword.encode())
					hex_digPassword = hash_object.hexdigest()
						
					# the new password is edited in the database
					db.updatePassAdmin(idSelect,hex_digPassword,conn)

					# selection of administrator in database
					namePersUpd = db.selectNomAdmin(idSelect,conn)
					
					# inside this object, the pseudo is recovered
					for i in namePersUpd:
						nameUpd = i[0]

					return template('admin',keys=hex_digPassword, keysVerification=name,admin=listAdmin,idPers=idPers,information="Le mot de passe de l'administrateur "+nameUpd+" a bien été modifié",creation="",generation="")
			
			# if the focus form is this to delete an administrator
			elif(types == "delete"):
				# if the administrator wanting to be deleted is the one currently logged
				if(idSelect == idPers):
					return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="Vous ne pouvez pas supprimer "+name+" car il est actuellement connecté",creation="",generation="")
				# if not, he isn't
				else:
					conn = db.connect()

					# the pseudo of the administrator that will be remove is selected (it's a sqlite3.Cursor object)
					namePersDel = db.selectNomAdmin(idSelect,conn)
					
					# inside this object, the pseudo is recovered
					for i in namePersDel:
						nameDel = i[0]
					
					# the administrator is deleted as well
					db.delAdmin(idSelect,conn)
					
					# everything is selected from the Admin table
					admins = db.selectAdmin(conn)
				
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
					

					return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information=nameDel+" a bien été supprimé",creation="",generation="")
			
			# if the focus form is this to add an administrator
			elif(types == "add"):
				conn = db.connect()
				# the pseudo of the new administrator is recovered
				nameCreated = request.forms.get('name')
				# the password of the new administrator is recovered
				passwordCreated = request.forms.get('password')
				
				# if the pseudo is empty
				if(nameCreated == ""):
					return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="",creation="Le nom de l'administrateur est inexistant",generation="")
				# if not, if the password is empty
				elif(passwordCreated == ""):
					return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="",creation="Le mot de passe pour " + nameCreated+ " est inexistant",generation="")
				# if not, if it's all right
				else:
					# the password is encrypted
					hash_object = hashlib.sha1(passwordCreated.encode())
					hex_digPassword = hash_object.hexdigest()
					
					# the ID linked with the pseudo is selected (it's a sqlite3.Cursor object)
					namePersCreate = db.selectIdAdmin(nameCreated,conn)
					
					# variable that count the number of administrators (number of line in database)
					i=0
		
					# the sqlite3.Cursor object is traversed 
					for j in namePersCreate:
						i = i+1
					
					# if there's something in this object, it's that the pseudo is already used
					if(i != 0):
						return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="",creation=nameCreated + " existe déjà, veuillez rentrer un autre nom",generation="")
					
					# the new administrator and his password are inserted into database
					db.addEntryAdmin(nameCreated,hex_digPassword,conn)
					
					# everything is selected from the Admin table
					admins = db.selectAdmin(conn)
					
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
						
					return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="",creation=nameCreated + " a bien été créé",generation="")
			
			#if the focus form is this to regenerate the CSV
			# for example, if the CSV is edited by removing some lines, the database could be regenerate to update the informations for users
			elif(types == "generation"):
				# everything is selected from the Admin table
				admins = db.selectAdmin(conn)
					
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
				
				conn.close()

				# the database is removed
				os.remove(DATA_PATH)
				# then it's regenerated
				generateDB.GenerateDB(listAdmin)
				
				return template('admin',keys=password, keysVerification=name,admin=listAdmin,idPers=idPers,information="",creation="",generation="La base a bien été mise à jour")
