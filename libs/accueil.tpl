<!DOCTYPE html>

<html lang="fr">

<head>
	<title>Installations Sportives des Pays de la Loire</title>
	<meta charset="utf-8">

	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"> </script>

	<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />

	<script type="text/javascript" src="../script/script.js"> </script>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" type="text/css" href="style_calendar.css">

	<style>	

		a {
			text-decoration: none;
			color:black;
		}


		h1{
			color:#38B2CE;
		}

	</style>
</head>

<body style="text-align:center">
	<h1> Installations Sportives des Pays de la Loire </h1>
	
	%if bd == "false":
		<form style="margin:auto;width:465px;">
	
			<fieldset style="padding:20px;border-radius:20px">
				<legend align="center" style="color:#04819E"> Accès au site impossible</legend>
				
				<p> Votre site contient aucune donnée</p>
				
				
					
					<input type="button" value="Créer la base de données" onclick="creation()">
					
				
				
				<script>
					
					function creation() 
					{
						window.location.href = "/creation";
					}
				</script>
				
			</fieldset>
		
		</form>
	%else:
	
		<form action="/" method="POST" style="margin:auto;width:470px;">
		  <fieldset style="padding:20px;border-radius:20px">
			<legend align="center" style="color:#04819E"> Accès au site </legend>
			
				<table style="text-align:left">
					
					%if admin == "":
						<input type="text" name="types" style="visibility:hidden;position:absolute" value="exist">
					
						<tr>
							
							<td>
					
								<label for="nom" style="color: #04819E"> Nom : </label>
						
							</td>
							
							<td>
					
								<input type="text" size="30" id="nom" name="nom">
							
							</td>
						
						</tr>
						
						<tr>
							
							<td>
					
								<label for="password" style="color: #04819E"> Password : </label>
								
							</td>
							
							<td>
					
								<input type="password" size="30" id="password" name="password">
								
							</td>
						
						</tr>
						
						<tr>
							
							<td td colspan=2 style="text-align:center">
						
								<input type="submit" value="Connection administrateur">
								
							</td>
							
						</tr>
						
					%else:
						<input type="text" name="types" style="visibility:hidden;position:absolute" value="create">
						
					
						<tr>
						
							<td colspan=2 style="text-align:center">
								
								Votre base de donnée ne contient aucun administrateur, créer en un :
							
							</td>
						
						</tr>
					
					
						<tr>
							
							<td>
					
								<label for="nomCreate" style="color: #04819E"> Nom : </label>
						
							</td>
							
							<td>
					
								<input type="text" size="30" id="nomCreate" name="nomCreate">
							
							</td>
						
						</tr>
						
						<tr>
							
							<td>
					
								<label for="passwordCreate" style="color: #04819E"> Password : </label>
								
							</td>
							
							<td>
					
								<input type="password" size="30" id="passwordCreate" name="passwordCreate">
								
							</td>
						
						</tr>
						
						<tr>
							
							<td td colspan=2 style="text-align:center">
						
								<input type="submit" value="Créer administrateur">
								
							</td>
							
						</tr>
					
					%end
					
					<tr style="height:30px">
					
					</tr>
					
					<tr >
						
						<td colspan=2 style="text-align:center">
					
							<input type="button" value="Connection utilisateur" onclick="connection()">
							
						</td>
						
					</tr>
					
					%if erreur != "":
						<tr >
						
							<td colspan=2 style="text-align:center">
						
								<p>{{ erreur }}</p>
								
							</td>
						
						</tr>
					%end
				
				</table>
				
				
		  </fieldset>
		</form>
		
		<script>
			function connection() 
			{
				window.location.href = "/recherche";
			}
		</script>
	
	%end
	


</body>

</html>
