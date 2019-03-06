(function ($) {


    $(document).ready(function () {
        //Add inventory
        $('#id_contractdetails_set-0-productPackingID').click(function () {

           productPackingID=this.value;
           reqURL=window.location.origin+'/getProductPackingDetail/';
           csrf=$('input[name="csrfmiddlewaretoken"]').val();
           $.ajax({
                  type: "POST",
                  url: reqURL,
                  data: {'productPackingID':productPackingID,'csrfmiddlewaretoken':csrf},
           }).done(function (data) {
               console.log(data.packingRecord);
               elementWeightPerBag='<div class="form-row field-weightPerBag">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="id_weightPerBag">Weight Per Bag:</label>\n' +
                   '                        \n' +
                   '                            <input type="text" name="weightPerBag" value="'+data.packingRecord.weightPerBag+'" class="vTextField" disabled maxlength="100"  id="id_weightPerBag">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
               elementConesPerBag='<div class="form-row field-conesPerBag">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="id_conesPerBag">Cones Per Bag:</label>\n' +
                   '                        \n' +
                   '                            <input type="text" name="conesPerBag" value="'+data.packingRecord.conesPerBag+'" class="vTextField" disabled maxlength="100"  id="id_conesPerBag">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
               elementWeightPerCone='<div class="form-row field-weightPerCone">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="id_weightPerCone">Weight Per Cone:</label>\n' +
                   '                        \n' +
                   '                            <input type="text" name="weightPerCone" value="'+data.packingRecord.weightPerCone+'" class="vTextField" disabled maxlength="100"  id="id_weightPerCone">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';

               $(elementWeightPerBag).insertAfter( "#contractdetails_set-group" );
               $(elementConesPerBag).insertAfter( "#contractdetails_set-group" );
               $(elementWeightPerCone).insertAfter( "#contractdetails_set-group" );



           });
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
        //Calculate Total Weight
        $('#id_contractdetails_set-0-noOfAdditional').focusout(function () {
            noOfAddCones=this.value;
            noOfBags=$("#id_contractdetails_set-0-noOfBags").val();
            weightPerBag=$('#id_weightPerBag').val();
            weightPerCone=$('#id_weightPerCone').val();
            totalWeight=(noOfBags*weightPerBag)+(noOfAddCones*weightPerCone);
             totalWeightInput='<div class="form-row field-totalWeight">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="id_totalWeight">Total Weight:</label>\n' +
                   '                        \n' +
                   '                            <input type="text" name="totalWeight" value="'+totalWeight+'" class="vTextField" disabled maxlength="100"  id="id_totalWeight">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
             $(totalWeightInput).insertAfter('#contractdetails_set-group');

        });
        $('#id_ratePerUnit').focusout(function () {
           ratePerUnit=this.value;
           totalUnits=$('#id_totalWeight').val();
           ammountWithOutTax=ratePerUnit*totalUnits;
           ammountWithOutTaxInput='<div class="form-row field-ammountWithOutTax">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="id_ammountWithOutTax">Total Ammount Without Tax:</label>\n' +
                   '                        \n' +
                   '                            <input type="text" name="ammountWithOutTax" value="'+ammountWithOutTax+'" class="vTextField" disabled maxlength="100"  id="id_ammountWithOutTax">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
           saleTax=$('#id_saleTax').val();
           incomeTax=$('#id_incomeTax').val();
           ammountWithTax=ammountWithOutTax+(ammountWithOutTax*saleTax/100)-(ammountWithOutTax*incomeTax/100);
           ammountWithTaxInput='<div class="form-row field-ammountWithTax">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="id_ammountWithTax">Total Amount  Tax:</label>\n' +
                   '                        \n' +
                   '                            <input type="text" name="ammountWithTax" value="'+ammountWithTax+'" class="vTextField" disabled maxlength="100"  id="id_ammountWithTax">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
           $(ammountWithOutTaxInput).insertAfter('.field-remarks');
           $(ammountWithTaxInput).insertAfter('.field-remarks');

        });

    });
})(django.jQuery);

