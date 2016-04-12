$(document).ready(function()
{
	$('thead th').css({fontWeight:'bold',marginLeft:'0px'});
	$('thead tr th:first-child').css({marginLeft:'0px',textAlign : 'left'});
	$('tfoot tr td').css({border:'none',textAlign:'left',color:'#C0C0C0'});
	$('table tbody tr th').css({color:'blue'});
	$('.tab-total th').css({color:'black',backgroundColor:'grey',fontWeight:'bold'});
	$('th.ventilation').css({color:'#800080'});
	$('tbody tr:odd td').css({backgroundColor:'#C0C0C0'});
	$('tbody tr td:contains("///")').addClass('non-defini');
	$('tbody tr td:contains("...")').addClass('non-defini');
	$('tbody tr td:contains("///")').html('<i style="color:green">abs</i>');
	$('tbody tr td:contains("...")').html('<i style="color:red">n.d</i>');
	$('.note:contains("/// Absence de résultat due à la nature des choses.")').html('<i style="color:green">abs</i> Absence de résultat due à la nature des choses.');
	$('.note:contains("... Résultat non disponible.")').html('<i style="color:red">n.d</i> Résultat non disponible.');
	
	var num = 1;
	$('caption').each(function(){
		$(this).html(num +" ." + $(this).html());
		num++;
	})

	$('#YI21').on('click',function(){trieclick(0,'th');});
	$('#YI32').on('click',function(){trieclick(0,'td');});
	$('#YI33').on('click',function(){trieclick(1,'td');});
	$('#YI34').on('click',function(){trieclick(2,'td');});
	$('#YI35').on('click',function(){trieclick(3,'td');});
	$('#YI36').on('click',function(){trieclick(4,'td');});




	function trieclick(val1,val2)
	{

		$tBody = $("table[id=T13F021T09] tbody") ;
		$fin = $("#eu");
		/* Capture des lignes du tableau
		et on passe en paramètre à sort la fonction de 
		comparaison entre 2 éléments */
		$tBody.children('tr').sort(function(ligneA,ligneB) { 
		// tri suivant l'élément de la 1ère colonne du tableau
		var valeurA = $(ligneA).children(val2).eq(val1).text().replace(/\s+/g, '');
		var valeurB = $(ligneB).children(val2).eq(val1).text().replace(/\s+/g, '');

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
		$tBody.append($fin);

		$('tbody tr:odd td').css({backgroundColor:'#C0C0C0'});
		$('tbody tr:even td').css({backgroundColor:'white'});
	}

});
