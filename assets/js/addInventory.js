(function ($) {


    $(document).ready(function () {
        //Add inventory
        $('#id_productPackID').click(function () {

           productPackingID=this.value;
           alert(productPackingID);
           reqURL=window.location.origin+'/getProductPackingDetail/';
            // formData=$('#addinventory_form').serialize();
           // $.ajax({
           //        type: "POST",
           //        url: reqURL,
           //        data: formData,
           // }).done(function (data) {
           //     console.log(data);
           //
           //     weightPerBag=data.contractDetails.weightPerBag;
           //     conesPerBag=data.contractDetails.conesPerBag;
           //     noOfAdditional=data.contractDetails.noOfAdditional;
           //     weightPerCone=data.contractDetails.weightPerCone;
           //     conesPerBag=data.contractDetails.conesPerBag;
           //     noOfBags=data.contractDetails.noOfBags;
           //     totalWeight=(noOfAdditional*weightPerCone)+(weightPerBag*noOfBags);
           //
           //     console.log("cones"+noOfAdditional+"*"+conesPerBag);
           //
           //
           //
           //     console.log(totalWeight);
           //
           //
           // });
        });

    });
})(django.jQuery);

