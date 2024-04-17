$(document).ready(function() {
    $('#contrats-table')
    .addClass( 'nowrap' )
    .dataTable( {
        responsive: true,
        columnDefs: [
            { targets: [-1, -3], className: 'dt-body-right' }
        ]
    });
});


   
   var TOKEN = $('input[name="csrfmiddlewaretoken"]').val();
   function loadData(initial_date, finale_date) {
   
       new DataTable('#contrats_table', {
       responsive: true,
       // rowReorder: true,
       // rowReorder: {
       //     selector: 'td:nth-child(2)'
       // },
       
       serverSide: true,
       paging: true,
       processing: true,
       stateSave: true,
       'lengthMenu': [10, 25, 50, 100, 150, 200, 300, 500],
       searching: true,
       sort: true,
       ajax: {
               url : "/ajax_contrat_list",
               type: 'POST',
               headers: {
               'X-CSRFToken': TOKEN
               },
               data: {
   
               "from_date": initial_date,
               "to_date": finale_date,
   
               },
           
           },
           language: {
               processing: "Traitement en cours...",
               search: "Rechercher&nbsp;:",
               lengthMenu: "Afficher _MENU_ &eacute;l&eacute;ments",
               info: "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
               infoEmpty: "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
               infoFiltered: "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
               infoPostFix: "",
               loadingRecords: "Chargement en cours...",
               zeroRecords: "Aucun &eacute;l&eacute;ment &agrave; afficher",
               emptyTable: "Aucune donnée disponible dans le tableau",
               paginate: {
                   first: "Premier",
                   previous: "Pr&eacute;c&eacute;dent",
                   next: "Suivant",
                   last: "Dernier"
               },
               aria: {
                   sortAscending: ": activer pour trier la colonne par ordre croissant",
                   sortDescending: ": activer pour trier la colonne par ordre décroissant"
               }
           },
          // langage: langage,
           columns: [
               // {data: 'id', visible: false},
               { data: 'date_contrat', visible: true ,title:"Date Sign."},
               { data: 'client', visible: true, title:"Nom du Client" },
               { data: 'montant_contrat', visible: true,title:"Montant A Payer" },
               { data: 'duree', visible: true,title:"Durée (mois)" },
               { data: 'status', visible: true, title:"Status" },
               { data: 'etat', visible: true,title:"Etat" },
               
           ],
           columnDefs: [
               
               //  { className: "dt-center", targets: "_all" }, // Centrer tous les contenus de colonnes
                { targets: "_all", className: 'dt-right' }
              
   
   
   
               
           ],
        
   });
   
   }
   
   
   
   
   $(document).ready(function () {
   
   loadData()
   
   $('form#date_filter').on('submit', function (e) {
   
       e.preventDefault();
   
       var from_date = $('#from_date').val()
       var to_date = $('#to_date').val()
       $('#contrats_table').DataTable().destroy()
       loadData(from_date, to_date)
   
   });
   
   
   
   $('#from_date').on('change', function () {
   
   $('#to_date').removeAttr("readonly")
   $('#to_date').attr("min", $(this).val())
   $('#to_date').val($(this).val())
   
   });
   
   });
   
