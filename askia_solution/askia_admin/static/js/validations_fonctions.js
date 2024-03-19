
 // Vérification du montant
 function montant_validation(montant) {
    if (isNaN(montant) || montant <= 0) {
        $("#montantError").html("Le montant doit être un nombre supérieur à zéro.");
    } else {
        $("#montantError").empty(); // Efface le message d'erreur s'il est valide
    }
    
 }
 
 // Vérification du contrat
 function contrat_validation(contrat) {
    const contratRegex = /^[A-Za-z\s\-']+$/;
    if (!contratRegex.test(contrat) || contrat.length < 3) {
        $("#contratError").html("Le contrat ne doit contenir que des lettres et au moins 3 caractères.");
    } else {
        $("#contratError").empty(); // Efface le message d'erreur s'il est valide
    }
 }

 //vérification de date
 function date_validation(date) {
    if (isNaN(date) || date == "") {
        $("#dateError").html("La date est requise.");
    } else {
        $("#dateError").empty(); // Efface le message d'erreur s'il est valide
    }
    
 }



 

//vidons les champs d'errors lors de la saisie

// $().ready(function(){
//     $("contrat").input(function(){
//         $("#contratError").empty(); 
//     })
// })