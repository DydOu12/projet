<!DOCTYPE html>

<html lang="fr">

<head>
	<title>Installations Sportives des Pays de la Loire</title>
	<meta charset="utf-8">

	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"> </script>
	
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.js"> </script>
	
	<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />

	<style>	
		a {
			text-decoration: none;
			color:black;
		}

		tbody tr:hover {
			background-color: #04819E;
		}

		h1{
			color:#38B2CE;
		}
		
		th {
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
			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367;" id="sport"> 
				Sport 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> 
				Niveau 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> 
				Commune 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;" id="codeDep"> 
				Code département 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> 
				Places de parking 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;"> 
				Accès handicapé 
			</th>
		</thead>

		<tbody>
			<!-- proposition corresponds to each element responding to the request of the user -->
			%for proposition in information:
				<tr>
					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}">
							{{ proposition[3] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}">
							{{ proposition[4] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}">
							{{ proposition[8] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}">
							{{ proposition[5] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}">
							{{ proposition[20] }}
						</a>
					</td>

					<td style="padding:10px;border-right:1px solid #015367;border-right:1px solid #015367;border-bottom:1px solid #015367">
						<a href="/recherche/{{ proposition[0] }}">
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
			// function trieclickNombre is associate to postal code and activity name columns
			$('#sport').on('click',function(){ trieclickNombre(0,'td');});
			$('#codeDep').on('click',function(){ trieclickNombre(3,'td');});
			
			function trieclickNombre(val1,val2)
			{
				$tBody = $("tbody") ;
				/* table lines are captured and comparison function 
				is passed in parameter to compare two by two elements */
				$tBody.children('tr').sort(function(ligneA,ligneB) 
				{ 
					// sorting according to the element of the first column of the table
					var valeurA = $(ligneA).children(val2).eq(val1).text().replace(/\s+/g, '');
					var valeurB = $(ligneB).children(val2).eq(val1).text().replace(/\s+/g, '');

					// testing if element is an integer
					if(isNaN(valeurA) || parseInt(valeurB) > parseInt(valeurA))
					{
						return 1;
					}

					if(isNaN(valeurB) || parseInt(valeurA) > parseInt(valeurB))
					{
						return -1;
					}

					// if not, it's a sort alphabetically
					return valeurA > valeurB ? -1 : 1 ;
				})
				// lines are added to $ tBody in the sort order
				.appendTo($tBody);
			}
		}
	); 
	
	</script>

</body>

</html>
