"use strict";
let formData;
const resetForms = () => {
    let forms = document.getElementsByTagName('form');
    for (const element of forms) {
        console.log(element);
        element.reset();
    }
}
let pdfUrl;
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

        $('#contratBtn').attr('disabled', true)
        $('#contratBtn .spinner-dr').removeClass("d-none");
        $('#contratBtn .btn-spinner-test-dr').addClass('d-none')


        formData = $(form).serialize()
        // console.log(formData);
        $.ajax({
            type: "POST",
            url: "/contrat_pdf/",
            data: formData,

            encode: true,
            xhrFields: {
                responseType: 'blob'
            },

            success: function (data) {
                $('#contratBtn').attr('disabled', false)
                $('#contratBtn .spinner-dr').addClass("d-none");
                $('#contratBtn .btn-spinner-test-dr').removeClass('d-none')
                // console.log($(this));
                // console.log(blob.size);
                console.log("Ok");
                let blob = new Blob([data]);
                pdfUrl = window.URL.createObjectURL(blob);
                // var link = document.createElement('a');
                // link.href = url;
                // link.download = 'example.pdf';
                // link.click();

                let pdfModal = $("#contratDefModal")
                let iframeContainer = $("#iframe-container");
                let iframe = `<iframe src="${pdfUrl}" width="100%" height="600px">
                    </iframe> `;
                iframeContainer.html(iframe);
                pdfModal.modal("show");
            },
            error: function (xhr) {
                $('#contratBtn').attr('disabled', false)
                $('#contratBtn .spinner-dr').addClass("d-none");
                $('#contratBtn .btn-spinner-test-dr').removeClass('d-none')
                console.log("Error");
                console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText);
            }
        })

    }
}

);
$('#contratSaveBtn').click(function () {





    $('#contratSaveBtn').attr('disabled', true)
    $('#contratSaveBtn .spinner-dr').removeClass("d-none");
    $('#contratSaveBtn .btn-spinner-test-dr').addClass('d-none')




    $.ajax({
        type: "POST",
        url: "/save/",
        data: formData,

        encode: true,
        dataType: "json",
        success: function (data) {
            $('#contratSaveBtn').attr('disabled', false)
            $('#contratSaveBtn .spinner-dr').addClass("d-none");
            $('#contratSaveBtn .btn-spinner-test-dr').removeClass('d-none')
            // console.log($(this));
            // console.log(blob.size);
            // console.log(data.ok);
            console.log("Ok");

            if (data.ok) {
                var link = document.createElement('a');
                link.href = pdfUrl;
                link.download = 'contrat_definition.pdf';
                link.click();
                location.href = "/contrats"
            } else {
                resetForms()
                location.reload()
            }


        },
        error: function (xhr) {
            $('#contratSaveBtn').attr('disabled', false)
            $('#contratSaveBtn .spinner-dr').addClass("d-none");
            $('#contratSaveBtn .btn-spinner-test-dr').removeClass('d-none')
            console.log("Error");
            console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText);
        }
    })


}

);
// $('#resetForm').click(function () {
//     resetForms()
// }

// );
