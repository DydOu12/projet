$(document).ready(function()
{
	$("#long").hide();
	$("#lat").hide();

	var cartes =new GMaps({
	  div: '#map',
	  lat: $("#long").text(),
	  lng: $("#lat").text(),
	  zoom : 15
	  });




})