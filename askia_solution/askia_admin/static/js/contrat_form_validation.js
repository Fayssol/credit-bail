$('#contratBtn').click(function() {
    const form = $('#contratForms'); // Sélectionnez le formulaire

    // client
    const client = $("#contrat").val();
    const contact = parseInt($("#contact").val());

    const address = $("#address").val();
    const dateN = $("#dateN").val();
    // contrat
    const montantC = parseInt($("#montantC").val());
    const dureeC = parseInt($("#dureeC").val());
    const dateS = $("#dateS").val();
    // temoins
    const nameT = $("#nameT:first").val();
    const phone = parseInt($("#phone:first").val());
    const adresseT = $("#adresseT:first").val();

    const v1 = montant_validation2(montantC);
    const v2 = contrat_validation(client, "#contratError");
    const v3 = date_validation(dateN, "#dnError");
    const v4 = date_validation(dateS, "#dateSgnError");
    const v5 = adresse_validation(address, '#adresseError');
    // alert(contact);
    const v6 = contact_validation(contact);
    const v7 = duree_validation(dureeC);

    const v8 = nameT_validation(nameT);
    const v9 = adresseT_validation(adresseT);
    const v10 = phone_validation(phone);

    if (v2 && v3 && v4 && v5 && v6 && v7 && v8 && v9 && v10 && v1) {
        // console.log('form valid');
        form.submit(); // Soumettez le formulaire
        // alert("fait");
        // console.log('apres form valid ******');
        
        
    }
    

});
