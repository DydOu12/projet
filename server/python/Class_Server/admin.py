import os
from bottle import template, request
import bottle 
import hashlib

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Admin():

	def get_admin(self,DATA_PATH,db):
		# if the database already exists
		if os.path.isfile(DATA_PATH):
			return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="",admin="")
		# if not, if the database does not exist
		else:
			return template('accueil',erreur="Accès refusé, merci de vous connectez pour accéder à cette partie du site",bd="false",admin="")

	def post_admin(self, db):
		conn = db.connect()

		# contain the password of the administrator when he logged
		password = request.forms.get('cles')
		# contain the pseudo of the administrator when he logged
		nom = request.forms.get('clesVerification')
		
		# ID linked with the pseudo is selected (it's a sqlite3.Cursor object)
		idAdmin = db.selectIdWithpassAdmin(nom,password,conn)
		
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
			conn = db.connect()

			# the type of the form is recovered to know which action will be realised
			types = request.forms.get('types')
			
			# the id of the logged administrator is recovered
			idPers = request.forms.get('idPers')
			
			# the id of the logged administrator is recovered (will be usefull to remove an administrator)
			idSelect = request.forms.get('idSelect')
			
			# everything is selected from the Admin table
			admins = db.selectAdmin(conn)
				
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
				conn = db.connect()

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
					db.updatePassAdmin(idSelect,hex_digPassword,conn)

					return template('admin',cles=hex_digPassword, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Le mot de passe de l'administrateur "+nom+" a bien été modifié",creation="",generation="")
			
			# if the focus form is this to delete an administrator
			elif(types == "delete"):
				# if the administrator wanting to be deleted is the one currently logged
				if(idSelect == idPers):
					return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="Vous ne pouvez pas supprimer "+nom+" car il est actuellement connecté",creation="",generation="")
				# if not, he isn't
				else:
					conn = db.connect()

					# the pseudo of the administrator that will be remove is selected (it's a sqlite3.Cursor object)
					nomPersDel = db.selectNomAdmin(idSelect,conn)
					
					# inside this object, the pseudo is recovered
					for i in nomPersDel:
						nomDel = i[0]
					
					# the administrator is deleted as well
					db.delAdmin(idSelect,conn)
					
					# everything is selected from the Admin table
					admins = db.selectAdmin(conn)
				
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
				conn = db.connect()
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
					nomPersCreate = db.selectIdAdmin(nomCreate,conn)
					
					# variable that count the number of administrators (number of line in database)
					i=0
		
					# the sqlite3.Cursor object is traversed 
					for j in nomPersCreate:
						i = i+1
					
					# if there's something in this object, it's that the pseudo is already used
					if(i != 0):
						return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation=nomCreate + " existe déjà, veuillez rentrer un autre nom",generation="")
					
					# the new administrator and his password are inserted into database
					db.insertAdmin(nomCreate,hex_digPassword,conn)
					
					# everything is selected from the Admin table
					admins = db.selectAdmin(conn)
					
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
				admins = db.selectAdmin(conn)
					
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
				# then it's regenerated
				generateDB.GenerateDB(listeAdmin)
				
				return template('admin',cles=password, clesVerification=nom,admin=listeAdmin,idPers=idPers,information="",creation="",generation="La base a bien été mise à jour")
