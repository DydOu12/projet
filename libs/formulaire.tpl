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

	<table style="margin:auto;text-align:left">

		<tbody>

			<form action="" method="POST"> 

				<tr>

					<td style="color:#015367">
						<label for="activite"> Choisissez votre activié : </label>
					</td>

					<td>

						<select id="activite" name="activite"> 

							%for activite in liste:
									<option>{{activite}}</option>
							%end

						</select>

					</td> 

				</tr>

				<tr>

					<td style="color:#015367">
						<label for="entrainement"> Niveau d'activité choisi : </label>
					</td>

					<td>
						<select id="entrainement" name="niveau"> 

							%for types in nivact:
								<option>{{ types }}</option>
							%end

						</select> 

					</td>

				</tr>

				<tr>

					<td style="color:#015367">

						<label for="handicap"> Accès handicapé : </label>

					</td>

					<td>

						<select id="handicap" name="handicap">
				
							<option></option>

							<option>Non</option>

							<option>Oui</option>


						</select>

					</td>

				</tr>

				<tr>

					<td style="color:#015367">
			
						<label for="codePostal"> Entez votre code postal : </label>

					</td>

					<td>

						<input type="text" value="" id="codePostal" name="codePostal"/> 

					</td>

				</tr>

				<tr style="height:20px">

				</tr>

				<tr style="text-align:center">

					<td colspan=2>

						<input id="ok" type="submit" value="Valider"/>

					</td>

				</tr>

			</form>

		</tbody>

	</table>

</body>

</html>
