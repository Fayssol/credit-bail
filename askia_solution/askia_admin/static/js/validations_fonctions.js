
 // Vérification du montant
 function montant_validation(montant) {
    if(isNaN(montant)){
        $("#montantError").html("Le montant est requis.");
        return false;
    }else if(Number.isInteger(montant) && montant <0){
        $("#montantError").html("Le montant est positif.");
        return false;
    }else{
        return true
    }
}

 
 // Vérification du contrat
 function contrat_validation(contrat, id) {
    const contratRegex = /^[A-Za-z\s\-']+$/;
    if (!contratRegex.test(contrat) || contrat.length < 3) {
        $(id).html("Le nom ne doit contenir que des lettres et au moins 3 caractères.");
        return false;
    } else {
        //$("#contratError").empty(); // Efface le message d'erreur s'il est valide
       
        return true;
    }
 }
 
//  //vérification de date
function date_validation(date,id) {
    if (date.trim() === "") {
        $(id).html("La date est requise.");
        return false;
    } else {
        var parsedDate = new Date(date);
        if (isNaN(parsedDate)) {
            $(id).html("Format de date invalide.");
            return false;
        } else {
            $(id).empty(); // Efface le message d'erreur s'il est valide
            return true;
        }
    }
}

function adresse_validation(adresse, id){
    if(adresse.trim() === ""){
        $(id).html("L' adresse est requise.");
        return false;
    }else{
        return true
    }
}

function contact_validation(contact){
   
    if(isNaN(contact)){
        $("#contactError").html("Le contact est requis.");
        return false;
    } else if(Number.isInteger(contact) && contact.toString().length !== 8 ) {
        $("#contactError").html("Le contact doit contenir exactement 8 caractères.");
        return false;
    } else {
        return true;
    }
}


function duree_validation(duree){
    if(isNaN(duree)){
        $("#dureeError").html("La durée est requise.");
        return false;
    }else if(Number.isInteger(duree) && duree <0){
        $("#dureeError").html("La durée est positive.");
        return false;
    }else{
        return true
    }
}

//
function nameT_validation(name){
    const contratRegex = /^[A-Za-z\s\-']+$/;
    if(name.trim() === ""){
        $("#nametError").html("Le nom est requis.");
        return false;
    }else if(!contratRegex.test(name) || name.length < 3){
        $("#nametError").html("Le nom ne doit contenir que des lettres et au moins 3 caractères.");
        return false;
    }else{
        return true
    }
} 
//

function phone_validation(phone){
   
    if(isNaN(phone)){
        $("#phoneError").html("Le phone est requis.");
        return false;
    } else if(Number.isInteger(phone) && phone.toString().length !== 8 ) {
        $("#phoneError").html("Le phone doit contenir exactement 8 caractères.");
        return false;
    } else {
        return true;
    }

}

function adresseT_validation(add){
    if(add.trim() === "" || Number.isInteger(parseInt(add))){
        $("#adressetError").html("L'adresse est requise.");
        return false;
    }else{
        return true
    }
}


function montant_validation2(montant) {
    if(isNaN(montant)){
        $("#montantError2").html("Le montant est requis.");
        return false;
    }else if(Number.isInteger(montant) && montant <0){
        $("#montantError2").html("Le montant est positif.");
        return false;
    }else{
        return true
    }

    
 }
 
 

//vider les champs
