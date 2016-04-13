<!DOCTYPE html>

<html lang="fr">

<head>
	<title>Installations Sportives des Pays de la Loire</title>
	<meta charset="utf-8">

	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"> </script>
	
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.js"> </script>
	
	<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />

	<script type="text/javascript" src="../script/script.js"> </script>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" type="text/css" href="style_calendar.css">

	<style>	

		a {
			text-decoration: none;
			color:black;
		}

		tr:hover 
		{
			background-color: #04819E;
		}

		h1{
			color:#38B2CE;
		}
		
		th
		{
			color : #206676
		}

	</style>
</head>

<body style="text-align:center">
	<h1> Installations Sportives des Pays de la Loire </h1>
	
	<form method="GET" action="/recherche" style="margin-bottom:20px;margin-top 20px;">
	
		<input type="submit" value=" Faire une recherche ">	
	
	</form>
	
	
	<table style="text-align:left;margin:auto" cellspacing="0" cellpadding="0" id="table">

		<thead style="background-color:#60B9CE">

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367;" id="sport"> Sport </th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> Niveau </th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> Commune </th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;" id="codeDep"> Code département </th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> Places de parking </th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> Accès handicapé </th>

		</thead>

		<tbody>

			%for proposition in information:
			
				<tr>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}/{{ infoEntrePage[0] }}/{{ infoEntrePage[1] }}/{{ infoEntrePage[2] }}/{{ infoEntrePage[3] }}">
							{{ proposition[3] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}/{{ infoEntrePage[0] }}/{{ infoEntrePage[1] }}/{{ infoEntrePage[2] }}/{{ infoEntrePage[3] }}">
							{{ proposition[4] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}/{{ infoEntrePage[0] }}/{{ infoEntrePage[1] }}/{{ infoEntrePage[2] }}/{{ infoEntrePage[3] }}">
							{{ proposition[8] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}/{{ infoEntrePage[0] }}/{{ infoEntrePage[1] }}/{{ infoEntrePage[2] }}/{{ infoEntrePage[3] }}">
							{{ proposition[5] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}/{{ infoEntrePage[0] }}/{{ infoEntrePage[1] }}/{{ infoEntrePage[2] }}/{{ infoEntrePage[3] }}">
							{{ proposition[20] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}/{{ infoEntrePage[0] }}/{{ infoEntrePage[1] }}/{{ infoEntrePage[2] }}/{{ infoEntrePage[3] }}">
							{{ proposition[18] }}
						</a>
					</td>

					

				</tr>
			


			%end






		</tbody>



	</table>
	
	<script>
	
		$(document).ready(function() 
		{ 
			$('#sport').on('click',function(){ trieclick(0,'th');});
			$('#codeDep').on('click',function(){ trieclickNombre(3,'td');});
			
			function trieclick(val1,val2)
			{
					alert("test");
			}
			
			function trieclickNombre(val1,val2)
			{
				$tBody = $("tbody") ;
				/* Capture des lignes du tableau
				et on passe en paramètre à sort la fonction de 
				comparaison entre 2 éléments */
				$tBody.children('tr').sort(function(ligneA,ligneB) { 
				// tri suivant l'élément de la 1ère colonne du tableau
				var valeurA = $(ligneA).children(val2).eq(val1).text().replace(/\s+/g, '');
				var valeurB = $(ligneB).children(val2).eq(val1).text().replace(/\s+/g, '');
				console.log(valeurA);
				console.log(valeurB);

				if(val2 == 'th')
				{
					return valeurA > valeurB ? 1 : -1 ;
				}

				if(isNaN(valeurA) || parseInt(valeurB) > parseInt(valeurA))
				{
					return 1;
				}

				if(isNaN(valeurB) || parseInt(valeurA) > parseInt(valeurB))
				{
					return -1;
				}



				return valeurA > valeurB ? -1 : 1 ;
				})
				// Les lignes sont ajoutées à $tBody dans l’ordre de tri
				.appendTo($tBody);
			}
			
		}
	); 
	
	
	</script>

</body>

</html>
