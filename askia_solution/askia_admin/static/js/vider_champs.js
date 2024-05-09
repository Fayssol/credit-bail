$(document).ready(function() {
    
    $("#montant").on("input", function() {
       
        $("#montantError").empty(); 
    });

    $("#montantC").on("input", function() {
        $("#montantError2").empty(); 
    });


    $("#contrat").on("input", function() {
       
        $("#contratError").empty(); 
    });

    $("#date").on("input", function() {
       
        $("#dateError2").empty(); 
    });
    
    // $("#nomClt").on("input", function() {
    //    
    //     $("#contratError").empty(); 
    // });

    $("#contact").on("input", function() {
       
        $("#contactError").empty(); 
    });

    $("#address").on("input", function() {
       
        $("#adresseError").empty(); 
    });

    $("#dateN").on("input", function() {
       
        $("#dnError").empty(); 
    });

    $("#montantC").on("input", function() {
        
        $("#montantError").empty(); 
    });

    $("#dureeC").on("input", function() {
        
        $("#dureeError").empty(); 
    });

    $("#dateS").on("input", function() {
        
        $("#dateSgnError").empty(); 
    });

    $("#nameT:first").on("input", function() {
        
        $("#nametError:first").empty(); 
    });

    $("#phone:first").on("input", function() {
        
        $("#phoneError:first").empty(); 
    });

    $("#adresseT:first").on("input", function() {
        
        $("#adressetError:first").empty(); 
    });

// others
    $("#nameT:last").on("input", function() {
       
        $("#nametError:last").empty(); 
    });

    $("#phone:last").on("input", function() {
       
        $("#phoneError:last").empty(); 
    });

    $("#adresseT:last").on("input", function() {
       
        $("#adressetError:last").empty(); 
    });


    
});
