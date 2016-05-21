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

		h1 {
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
						<label for="activity"> Choisissez votre activité : </label>
					</td>

					<td>
						<select id="activity" name="activity"> 
							<!-- activity  corresponds to each element of sports without duplicates -->
							%for activity in list:
								<option>{{activity}}</option>
							%end
						</select>
					</td> 
				</tr>

				<tr>
					<td style="color:#015367">
						<label for="training"> Niveau d'activité choisi : </label>
					</td>

					<td>
						<select id="training" name="level"> 
							<!-- types  corresponds to each element of levels of competition without duplicates -->
							%for types in levAct:
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
						<label for="postalCode"> Entez votre code postal : </label>
					</td>

					<td>
						<input type="text" value="" id="postalCode" name="postalCode"/> 
					</td>
				</tr>

				<tr style="height:20px"> </tr>

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
