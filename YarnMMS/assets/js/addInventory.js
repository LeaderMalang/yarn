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
        //ADD calculated Weight
        $('#id_conesPerBag').focusout(function () {
            conePerBag=this.value;
            weightPerBag=$('#id_weightPerBag').val();
           weightPerCone= $('.field-weightPerCone').find('div.readonly');
           weightPerConeValue=weightPerBag/conePerBag
           weightPerConeInput='<input type="text" name="weightPerCone" value="'+weightPerConeValue+'" disabled/>';

           weightPerCone.html(weightPerConeInput);
        });

    });
})(django.jQuery);

