
 // Vérification du montant
 function montant_validation(montant) {
    if (isNaN(montant) || montant <= 0) {
        $("#montantError").html("Le montant doit être un nombre supérieur à zéro.");
        //alert('0000000');
        return;
    } else {
        $("#montantError").empty(); // Efface le message d'erreur s'il est valide
        return true;
    }
    
 }
 
 // Vérification du contrat
 function contrat_validation(contrat) {
    const contratRegex = /^[A-Za-z\s\-']+$/;
    if (!contratRegex.test(contrat) || contrat.length < 3) {
        $("#contratError").html("Le contrat ne doit contenir que des lettres et au moins 3 caractères.");
    } else {
        //$("#contratError").empty(); // Efface le message d'erreur s'il est valide
        console.log('54654548');
        return true;
    }
 }
 
//  //vérification de date
function date_validation(date) {
    if (date.trim() === "") {
        $("#dateError").html("La date est requise.");
    } else {
        var parsedDate = new Date(date);
        if (isNaN(parsedDate)) {
            $("#dateError").html("Format de date invalide.");
        } else {
            $("#dateError").empty(); // Efface le message d'erreur s'il est valide
            return true;
        }
    }
}


 

//vider les champs
