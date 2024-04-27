

$('#transactionBtn').click(function() {
    const note = $("#note").val();
    const montant = parseInt($("#montant").val());
    const contrat = $("#contrat").val();
    const date = $("#date").val();
    const form = $("#transactionForm");
    const alert = $("#myAlert");
    
    // Vérification du montant
   const v1 = montant_validation(montant);
    
    // Vérification du contrat
   const v2 = contrat_validation(contrat, "#contratError");
    
   // Vérification de date
   const v3 = date_validation(date, "#dateError");
  if (v1 && v2 && v3) {
    console.log('form valid');
    form.submit();
    alert.html("")
    
  }
 
   
});
