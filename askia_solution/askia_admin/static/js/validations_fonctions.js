
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
 function contrat_validation(contrat, id) {
    const contratRegex = /^[A-Za-z\s\-']+$/;
    if (!contratRegex.test(contrat) || contrat.length < 3) {
        $(id).html("Le nom ne doit contenir que des lettres et au moins 3 caractères.");
    } else {
        //$("#contratError").empty(); // Efface le message d'erreur s'il est valide
        console.log('54654548');
        return true;
    }
 }
 
//  //vérification de date
function date_validation(date,id) {
    if (date.trim() === "") {
        $(id).html("La date est requise.");
    } else {
        var parsedDate = new Date(date);
        if (isNaN(parsedDate)) {
            $(id).html("Format de date invalide.");
        } else {
            $(id).empty(); // Efface le message d'erreur s'il est valide
            return true;
        }
    }
}

function adresse_validation(adresse, id){
    if(adresse.trim() === ""){
        $(id).html("L' adresse est requise.");
    }else{
        return true
    }
}

function contact_validation(contact){
    if(contact.trim() === ""){
        $("#contactError").html("Le contact est requis.");
    }else{
        return true
    }
}

function duree_validation(duree){
    if(duree.trim() === ""){
        $("#dureeError").html("La durée est requise.");
    }else{
        return true
    }
}

function nameT_validation(name){
    if(name.trim() === ""){
        $("#nametError").html("Le nom est requis.");
    }else{
        return true
    }
}
function phone_validation(phone){
    if(phone.trim() === ""){
        $("#phoneError").html("Le phone est requis.");
    }else{
        return true
    }
}

function adresseT_validation(add){
    if(add.trim() === ""){
        $("#adressetError").html("L'adresse est requise.");
    }else{
        return true
    }
}


function montant_validation2(montant) {
    if (isNaN(montant) || montant <= 0) {
        $("#montantError2").html("Le montant doit être un nombre supérieur à zéro.");
        //alert('0000000');
        return;
    } else {
        $("#montantError2").empty(); // Efface le message d'erreur s'il est valide
        return true;
    }
    
 }
 
 

//vider les champs
