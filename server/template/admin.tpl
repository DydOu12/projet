<!DOCTYPE html>

<html lang="fr">

<head>
	<title>Installations Sportives des Pays de la Loire</title>
	<meta charset="utf-8">

	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"> </script>

	<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />

	<style>	
		a {
			text-decoration: none;
			color:black;
		}

		h1,h2 {
			color:#38B2CE;
		}

		th {
			color : #206676
		}
		
		thead {
			background-color:#60B9CE;
		}
	</style>
</head>

<body style="text-align:center">

	<h1> Installations Sportives des Pays de la Loire </h1>
	
	<h2>Administration du site</h2>
	
	<h3 style="margin-left:200px;text-align:left"><u>Base de données des administrateurs :</u></h3>
	
	<form>
		<input type="button" value="Déconnexion" onclick="disconnect()" style="float:right">
	</form>
	
	<script>
		function disconnect() 
		{
			window.location.href = "/";
		}
	</script>
	
	<table cellspacing="0" cellpadding="0" style="margin-left:200px;">
		<thead>
			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367;">
				Nom 
			</th>
			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> 
				Modifier password 
			</th>
			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> 
				Supprimer administrateur 
			</th>
		</thead>
	
		<tbody>
			<!-- person attribute corresponds to each administrators in database -->
			%for person in admin:
			<tr>
				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367">
					<!-- Corresponding to the pseudo of all administrators -->
					{{ person[1] }}
				</td>

				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367"> 
					<form method="POST" action="/admin">
						<input name="keys" type="hidden" value={{ keys }}>
						<input name="keysVerification" type="hidden" value={{ keysVerification }}>
						<input name="idPers" type="hidden" value={{ idPers }}>
						<input type="hidden" value="{{ person[0] }}" name="idSelect">
						<input type="hidden" value="modification" name="types">
										
						<input type="password" name="newPassword">
						<input type="submit" value="Modifier mot de passe">
					</form>
				</td>
				
				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367;text-align:center">

					<!-- idPers contains the administrator's ID currently logged 
					So if the administrator's ID currenty logged is equal to this of the currently traversed administrator 
					it's impossible to delete him -->
					%if int(person[0]) == int(idPers):
						 Suppression impossible car connecté 
					<!-- if not, it's possible to delete the administrator because he is not logged -->
					%else:
						<form method="POST" action="/admin">
							<input name="keys" type="hidden" value={{ keys }}>
							<input name="keysVerification" type="hidden" value={{ keysVerification }}>
							<input type="hidden" value="{{ person[0] }}" name="idSelect">
							<input name="idPers" type="hidden" value={{ idPers }}>
							<input type="hidden" value="delete" name="types">
							
							<input type="submit" value="Supprimer">
						</form>
					%end
				</td>
			</tr>	
			%end
		</tbody>
	</table>
	
	<!-- if an action has been performed relevant to delete or update an administrator, it is reported here -->
	%if information != "":
		<p>{{ information }}</p>
	%end
	
	<h3 style="margin-left:200px;text-align:left;margin-top:100px;"><u>Ajout d'un administrateur :</u></h3>
	
	<table style="margin-left:200px;">
		<form method="POST" action="/admin">
			<tr>
				<input name="keys" type="hidden" value={{ keys }}>
				<input name="keysVerification" type="hidden" value={{ keysVerification }}>
				<input name="idPers" type="hidden" value={{ idPers }}>
				<input type="hidden" value="add" name="types">
				
				<td> 
					Nom : 
				</td>

				<td> 
					<input type="text" name="name">
				</td>
				
				<td> 
					Password : 
				</td>
				
				<td>
					<input type="password" name="password">
				</td>
				
				<td>
					<input type="submit" value="Créer">
				</td>
			</tr>
		</form>
	</table>
	
	<!-- if an action has been performed relevant to creation of new administrators, it is reported here -->
	%if creation != "":
		<p>{{ creation }}</p>
	%end
	
	<h3 style="margin-left:200px;text-align:left;margin-top:100px;"><u>Regénérer la base de donnée (si csv modifié)</u></h3>
	
	<form method="POST" action="/admin" style="text-align:left">
		<input name="keys" type="hidden" value={{ keys }}>
		<input name="keysVerification" type="hidden" value={{ keysVerification }}>
		<input name="idPers" type="hidden" value={{ idPers }}>
		
		<input type="hidden" value="generation" name="types">
		<input type="submit" value="Générer" style="margin-left:200px;margin-top:20px">
	</form>

	<!-- if an action has been performed relevant to regerate database from CSV, it is reported here -->
	%if generation != "":
		<p style="float:left;margin-left:200px;margin-top:20px">{{ generation }}</p>
	%end

</body>

</html>
