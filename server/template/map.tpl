<!DOCTYPE html>

<html lang="fr">

<head>
	<title>Installations Sportives des Pays de la Loire</title>
	<meta charset="utf-8">

	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"> </script>

	<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />

	<script src="https://maps.googleapis.com/maps/api/js"></script>

	<script type="text/javascript" src="https://raw.githubusercontent.com/HPNeo/gmaps/master/gmaps.js"> </script>

	<style>	
		h1{
			color:#38B2CE;
		}
	</style>
</head>

<body style="text-align:center">
	<h1> Installations Sportives des Pays de la Loire </h1>
	
	<table style="text-align:center;margin-right:auto;margin-left:auto;margin-top:60px" cellspacing="0" cellpadding="0">
		<thead style="background-color:#60B9CE">
			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;border-left:1px solid #015367;color:#206676"> 
				Sport 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;color:#206676"> 
				Niveau
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;color:#206676"> 
				Commune 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;color:#206676"> 
				Code département 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;color:#206676"> 
				Places de parking 
			</th>

			<th style="padding:10px;border-right:1px solid #015367;border-top:1px solid #015367;border-bottom:1px solid #015367;color:#206676"> 
				Accès handicapé 
			</th>
		</thead>

		<!-- information is an array containing results related to the request made by the user -->
		<tbody>
			<tr>
				<td style="padding:10px;border-left:1px solid #015367;border-bottom:1px solid #015367;border-right:1px solid #015367">
					{{ information[3] }}
				</td>

				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
					{{ information[4] }}
				</td>

				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
					{{ information[8] }}
				</td>

				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
					{{ information[5] }}
				</td>

				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
					{{ information[20] }}
				</td>

				<td style="padding:10px;border-right:1px solid #015367;border-bottom:1px solid #015367">
					{{ information[18] }}
				</td>
			</tr>
		</tbody>

		<p id="long">{{ information[13] }}</p>
		<p id="lat">{{ information[14] }}</p>
	</table>

	<div id="map" style="width:600px;height:600px;margin-top:50px;margin-left:auto;margin-right:auto"> 

	</div>

</body>

<script>
	$("#long").hide();
	$("#lat").hide();

	// map display
	var cartes =new GMaps({
		div: '#map',
		lat: $("#lat").html(),
		lng: $("#long").html(),
		zoom : 15
	});

	// marker display
	cartes.addMarker({
	    lat: $("#lat").html(),
	    lng: $("#long").html(),
	    infoWindow: {
	    	content: '{{ information[17] }}'
	  	}
  	});
</script>

</html>
