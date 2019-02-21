(function ($) {


    $(document).ready(function () {
        //Add inventory
        $('#id_purchaseContractID').click(function () {

           contractID=this.value;
           reqURL=window.location.origin+'/getContractDetail/';
            formData=$('#inventoryin_form').serialize();
           $.ajax({
                  type: "POST",
                  url: reqURL,
                  data: formData,
           }).done(function (data) {
               console.log(data);

               weightPerBag=data.contractDetails.weightPerBag;
               conesPerBag=data.contractDetails.conesPerBag;
               noOfAdditional=data.contractDetails.noOfAdditional;
               weightPerCone=data.contractDetails.weightPerCone;
               conesPerBag=data.contractDetails.conesPerBag;
               noOfBags=data.contractDetails.noOfBags;
               totalWeight=(noOfAdditional*weightPerCone)+(weightPerBag*noOfBags);
               remainingBags=noOfBags-data.remainingBags;


                elementTotalWeight='<div class="form-group"><div><label class="required">Total Weight:</label><input type="text" disabled value="'+totalWeight+'"/></div></div>';
                elementnoOfBags='<div class="form-group"><div><label class="required">Total Bags:</label><input type="text" disabled value="'+noOfBags+'"/></div></div>';
                elementRemainingBags='<div class="form-group"><div><label class="required">Remaining Bags:</label><input type="text" disabled value="'+remainingBags+'"/></div></div>';

                $('.module').append(elementnoOfBags,elementRemainingBags,elementTotalWeight);
               console.log(totalWeight);


           });
        });

    });
})(django.jQuery);

