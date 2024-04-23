$('#contratBtn').click(function() {
    const form = $('#contratForms').val();
    // client
    const client = $("#contrat").val();
    const contact = $("#contact").val();
    const address = $("#address").val();
    const dateN = $("#dateN").val();
    // contrat
    const montantC = $("#montant").val();
    const dureeC = $("#dureeC").val();
    const dateS = $("#dateS").val();
    // temoins
    const nameT = $("#nameT").val();
    const phone = $("#phone").val();
    const adresseT = $("#adresseT").val();

    // const v1 = montant_validation(montantC);
    const v2 = contrat_validation(client, "#contratError");
    const v3 = date_validation(dateN, "#dnError");
    const v4 = date_validation(dateS, "#dateSgnError");
    const v5 = adresse_validation(address, '#adresseError');
    const v6 = contact_validation(contact);
    const v7 = duree_validation(dureeC);
    // const v8 = nameT_validation(nameT);
    // const v9 = adresseT_validation(adresseT);
    // const v10 = phone_validation(phone);

    if (v2 && v3 && v4 && v5 && v6 && v7) {
        console.log('form valid');
        form.submit();
        alert.html("")
        
    }
    

});