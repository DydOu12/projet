$( document ).ready(function() 
{
    function verifCP()
	{
		var regexFrance = /^[0-9]{5}$/;
		var cp = $("#codePostal");

		return regexFrance.test(cp.val());
	}

	$( "form" ).submit(function( event ) 
	{
		if ( verifCP() ) 
			return;

		$( ".erreur" ).text( "Code postal incorrect !" ).show().fadeOut( 3000 );
		event.preventDefault();
	});

});