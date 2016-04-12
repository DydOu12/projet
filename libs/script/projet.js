$(document).ready(function()
{
    var t = $('#table').DataTable({
          "language" : {
    "sProcessing":     "Traitement en cours...",
    "sSearch":         "Rechercher&nbsp;:",
    "sLengthMenu":     "Afficher _MENU_ &eacute;l&eacute;ments",
    "sInfo":           "Affichage de l'&eacute;l&eacute;ment _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
    "sInfoEmpty":      "Affichage de l'&eacute;l&eacute;ment 0 &agrave; 0 sur 0 &eacute;l&eacute;ment",
    "sInfoFiltered":   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
    "sInfoPostFix":    "",
    "sLoadingRecords": "Chargement en cours...",
    "sZeroRecords":    "Aucun &eacute;l&eacute;ment &agrave; afficher",
    "sEmptyTable":     "Aucune donn&eacute;e disponible dans le tableau",
    "oPaginate": {
        "sFirst":      "Premier",
        "sPrevious":   "Pr&eacute;c&eacute;dent",
        "sNext":       "Suivant",
        "sLast":       "Dernier"
    },
    "oAria": {
        "sSortAscending":  ": activer pour trier la colonne par ordre croissant",
        "sSortDescending": ": activer pour trier la colonne par ordre d&eacute;croissant"
    }
  }
});
    var maps = [];
    var station = [];
    $("#ville").val("");
    $.ajax
    ({       
      url : 'https://api.jcdecaux.com/vls/v1/contracts',       
      type : 'GET',       
      dataType : 'json',
      data : "apiKey=d32a0c77640f93610853ed89812d9d5ccd3a8a17",      
        success : function(data)
        {
          /*On stocke toutes les valeurs dans un tableau*/
          $.map(data, function(objet)
          {
                  maps.push(objet.name);
                  /*On rajoute une option pour chacune des villes*/
                  if(objet.name == "Nantes")
                  {
                    $("#liste").append("<option selected=selected>"+objet.name+"</option>");
                  }else
                  {
                    $("#liste").append("<option>"+objet.name+"</option>");
                  }
                  
          });
        }


         
    });

    var carte =new GMaps({
      div: '#map',
      lat: 47.212108463141774,
      lng: -1.553049129320471,
      zoom : 15
    });

      carte.addMarker({
      lat: 47.212108463141774,
      lng: -1.553049129320471,
      infoWindow: {
      content: '<p>Nantes</p>'
    }
    });

    

    $( "#ville" ).autocomplete({
      source: map,
      /*Le tableau d'autocomplete va prendre la valeur du tableau*/
      // source : map;
      
      /* On autocomplète a partir de 3 caractères*/
      minLength : 3,

    });

    /*Permet d'afficher le titre lié à l'id lorsque l'on passe ça souris dessus*/
     $( "#ville" ).tooltip({
        hide: { effect: "explode", duration: 1000 }
      });

       $(function() {
      $( "#tabs" ).tabs();
       });



    $("#rechercher").on('click', function()
    {
      $("#tableau").empty();
      /*On teste si la personne a rentrer quelque chose dans le texte*/
      var ville ="";

      t.clear();
      var coord = [];
      
      //Si rien n'a été rentrer on prends la ville de la liste
      if($("#ville").val() == "")
      {
        ville = $('#liste').val();
      /* Sinon on prends le texte saisie*/
      }else
      {
        console.log("CAMESOUALE");
        ville = $("#ville").val();
      }


      $.ajax
      ({       
        url : 'https://api.jcdecaux.com/vls/v1/stations',       
        type : 'GET',       
        dataType : 'json',
        data : 'contract='+ville+ "&apiKey=d32a0c77640f93610853ed89812d9d5ccd3a8a17",      
          success : function(data)
          {
            
            /*On stocke toutes les valeurs dans un tableau*/
            $.map(data, function(objet)
            {
                    coord.push(objet.position);

                    /*On construit le tableau*/
                    t.row.add( [
                        objet.number,
                        objet.name,
                        objet.address,
                        objet.available_bike_stands,
                        objet.available_bikes
                    ] ).draw( false );
            });


          }
           
      })

      $.ajax
      ({       
        url : 'http://maps.google.com/maps/api/geocode/json',       
        type : 'GET',       
        dataType : 'json',
        data : 'address='+ville+ "&sensor=false",      
          success : function(data)
          {
            
            /*On stocke toutes les valeurs dans un tableau*/
            $.map(data.results, function(objet)
            {
                   lat = objet.geometry.location.lat;
                   lng = objet.geometry.location.lng;
            });

            var cartes =new GMaps({
                  div: '#map',
                  lat: lat,
                  lng: lng,
                  zoom : 15
                  });

            jQuery.each( coord, function( i, val ) 
            {
              // console.log(val);
              if(i != 0)
              {
                  cartes.addMarker({
                    lat: val.lat,
                    lng: val.lng,
                    infoWindow: {
                    content: '<p>Nantes</p>'
                  }
                  });
              }
            });


          }
           
      })

      




    })

 







});

