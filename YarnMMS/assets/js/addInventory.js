(function ($) {


    $(document).ready(function () {
        //Add inventory
        $('#id_contractID').click(function () {

           contractID=this.value;
           reqURL=window.location.origin+'/getContractDetail/';
            formData=$('#addinventory_form').serialize();
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
               totalCones=noOfAdditional+(conesPerBag*noOfBags);


           });
        });

    });
})(django.jQuery);

