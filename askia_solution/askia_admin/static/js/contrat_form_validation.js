"use strict";

$('#contratBtn').click(function () {

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
        // form.submit(); // Soumettez le formulaire
        // alert("fait");
        // console.log('apres form valid ******');
        // $.ajax({
        //     data: $(form).serialize(), // get the form data
        //     type: $(form).attr('method'), // GET or POST
        //     url: "{% url 'contact_form' %}",
        //     // on success
        //     success: function (response) {
        //         alert("Thankyou for reaching us out " + response.name);
        //     },
        //     // on error
        //     error: function (response) {
        //         // alert the error if any error occurred
        //         alert(response.responseJSON.errors);
        //         console.log(response.responseJSON.errors)
        //     }
        // });
        $('#contratBtn').attr('disabled', true)
        $('#contratBtn .spinner-dr').removeClass("d-none");
        $('#contratBtn .btn-spinner-test-dr').addClass('d-none')
        console.log($(this));
        let formData = {
            nom: client,
            contact: contact,
            adresse: address,
            date_naissance: dateN,
            montantC: montantC,
            duree: dureeC,
            date_sgnture: dateS,
            nomTemoin: nameT,
            contactTemoin: phone,
            adresseTemoin: adresseT,
            superheroAlias: $("#superheroAlias").val(),
        };

        $.ajax({
            type: "POST",
            url: "/contrat_pdf",
            data: formData,
            dataType: "json",
            encode: true,
        }).done(function (data) {
            $('#contratBtn').attr('disabled', false)
            $('#contratBtn .spinner-dr').addClass("d-none");
            $('#contratBtn .btn-spinner-test-dr').removeClass('d-none')
            console.log($(this));
            console.log(data);
        }).catch(function(error){
            $('#contratBtn').attr('disabled', false)
            $('#contratBtn .spinner-dr').addClass("d-none");
            $('#contratBtn .btn-spinner-test-dr').removeClass('d-none')
            console.log($(this));
            console.log(error);
        });
    }

}


);
