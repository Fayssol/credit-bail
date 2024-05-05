"use strict";

let pdfUrl;
console.log("555555555555");
$('#contratsPdf').click(function () {





    $('#contratsPdf').attr('disabled', true)
    $('#contratsPdf .spinner-dr').removeClass("d-none");
    $('#contratsPdf .btn-spinner-test-dr').addClass('d-none')


    

    $.ajax({
        type: "GET",
        url: "/contrats_pdf/",



        xhrFields: {
            responseType: 'blob'
        },

        success: function (data) {
            $('#contratsPdf').attr('disabled', false)
            $('#contratsPdf .spinner-dr').addClass("d-none");
            $('#contratsPdf .btn-spinner-test-dr').removeClass('d-none')
            // console.log($(this));
            // console.log(blob.size);
            console.log("Ok");
            let blob = new Blob([data]);
            pdfUrl = window.URL.createObjectURL(blob);


            let pdfModal = $("#contratDefModal")
            let iframeContainer = $("#iframe-container");
            let iframe = `<iframe src="${pdfUrl}" width="100%" height="600px">
                    </iframe> `;
            iframeContainer.html(iframe);
            pdfModal.modal("show");
        },
        error: function (xhr) {
            $('#contratsPdf').attr('disabled', false)
            $('#contratsPdf .spinner-dr').addClass("d-none");
            $('#contratsPdf .btn-spinner-test-dr').removeClass('d-none')
            console.log("Error");
            console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText);
        }
    })


}

);
$('#contratDownloadBtn').click(function () {

    var link = document.createElement('a');
    link.href = pdfUrl;
    link.download = 'contrat_liste.pdf';
    link.click();
}

);

