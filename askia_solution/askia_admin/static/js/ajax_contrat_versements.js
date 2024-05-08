'use strict'

$(document).ready(function() {
    $('#vers_contrat_table')
    .addClass( 'nowrap' )
    .dataTable( {
        responsive: true,
        columnDefs: [
            { targets: [-1, -3], className: 'dt-body-right' }
        ]
    });
});

   
var TOKEN = $('input[name="csrfmiddlewaretoken"]').val();
var id_contrat=$('#contratId').val();
function loadData(initial_date, finale_date) {

    new DataTable('#vers_contrat_table', {
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
            url : "/ajax_transaction_list_contrat/",
            type: 'POST',
            headers: {
            'X-CSRFToken': TOKEN
            },
            data: {

            "from_date": initial_date,
            "to_date": finale_date,
            "id": id_contrat
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
            { data: 'nom', visible: true ,title:"Clients",
            render: function ( data, type, row ) {
                return '<div class="input-group text-center p-2 d-flex align-items-center">' +
                    '<img src="/static/img/user-solid.svg" alt="">' +
                    '<span class="fw-bolder">'+row.nom+'</span>' +
                    '</div>';
                }
            },

            { data: 'contact', visible: true, title:"Contacts"},
            { data: 'date_versement', visible: true,title:"Date Vers." },
            { data: 'montant_versement', visible: true,title:"Montant Versé" },

            { data: 'montant_total_paye',
                visible: true, 
                title:"Total Versé",
                render: function ( data, type, row ) {
                   
                        return '<span class="text-secondary">'+row.montant_total_paye+'</span>';
                   
                }
            },

            { data: 'montant_contrat', visible: true,title:"À Payé", },

            { data: 'reste', visible: true,title:"Reste",
                render: function ( data, type, row ) {
                    
                    return '<span class="text-primary">'+row.reste+'</span>';
            
                 }
             },


            { data: 'note', visible: true, title:"Notes" }
        ],
        columnDefs: [
            
            //  { className: "dt-center", targets: "_all" }, // Centrer tous les contenus de colonnes
             { targets: "_all", className: 'dt-right' },
           



            
        ],
     
});

}




$(document).ready(function () {

loadData()

$('form#date_filter').on('submit', function (e) {

    e.preventDefault();

    var from_date = $('#from_date').val()
    var to_date = $('#to_date').val()
    $('#transactions_table').DataTable().destroy()
    loadData(from_date, to_date)

});



$('#from_date').on('change', function () {

$('#to_date').removeAttr("readonly")
$('#to_date').attr("min", $(this).val())
$('#to_date').val($(this).val())

});

});


