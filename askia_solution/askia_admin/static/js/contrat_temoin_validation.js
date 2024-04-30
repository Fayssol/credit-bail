
  $(document).ready(function () {
      // Add temoin
      $(".add-temoin").click(function () {
          if (validateTemoin()) {
              var clone = $(".temoin:first").clone(true);
              clone.find("input").val(""); 
              clone.find(".add-temoin").remove(); 
              clone.find(".remove-temoin").show();
              $("#temoins").append(clone);
          }
      });

      // Remove temoin
      $("#temoins").on("click", ".remove-temoin", function () {
          $(this).closest(".temoin").remove();
      });

      // Validation function
      function validateTemoin() {
          var isValid = true;
          $(".temoin").each(function () {
              var fullname = $(this).find("input[name='nomTemoin']").val();
              var telephone = $(this).find("input[name='contactTemoin']").val();
              var telephone = parseInt(telephone);
              var address = $(this).find("input[name='adresseTemoin']").val();

              

            const contratRegex = /^[A-Za-z\s\-']+$/;
              if (fullname == "") {
                  $(this).find("#nametError").text("Le nom est requis");
                  isValid = false;
              } else if(!contratRegex.test(fullname) || fullname.length < 3){
                    $(this).find("#nametError").text("Le nom ne doit contenir que des lettres et au moins 3 caractères.");
                    isValid = false;
              }else {
                  $(this).find("#nametError").text("");
              }

              if (isNaN(telephone)) {
                  $(this).find("#phoneError").text("Le phone est requis");
                  isValid = false;
              }else if(Number.isInteger(telephone) && telephone.toString().length !== 8 ) {
                 $(this).find("#phoneError").text("Le phone doit contenir exactement 8 caractères.");
                 isValid = false;
              }else {
                  $(this).find("#phoneError").text("");
              }




              if (address == "" || Number.isInteger(parseInt(address))) {
                  $(this).find("#adressetError").text("L'adresse est requise");
                  isValid = false;
              } else {
                  $(this).find("#adressetError").text("");
              }

          });
          return isValid;
      }
      
  });
