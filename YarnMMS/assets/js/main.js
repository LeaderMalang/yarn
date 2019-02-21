(function ($) {


    $(document).ready(function () {
        //add starting inventory Function
        $('#id_addInventory').click(function () {
            startinginventory='<div class="form-row field-startinginventory">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="startinginventory">Starting Inventory:</label>\n' +
                   '                        \n' +
                   '                            <input type="number" name="startinginventory" class="vTextField" maxlength="100" required="" id="startinginventory">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
               startingprice='<div class="form-row field-startingprice">\n' +
                   '            \n' +
                   '            \n' +
                   '                <div>\n' +
                   '                    \n' +
                   '                    \n' +
                   '                        <label class="required" for="startingprice">Starting Price:</label>\n' +
                   '                        \n' +
                   '                            <input type="number" name="startingprice" class="vTextField" maxlength="100" required="" id="startingprice">\n' +
                   '                        \n' +
                   '                    \n' +
                   '                    \n' +
                   '                </div>\n' +
                   '            \n' +
                   '        </div>';
           if($(this).is(':checked')){

               $('.aligned').append(startinginventory,startingprice)
           }else {
               $('.field-startinginventory').remove()
               $('.field-startingprice').remove()
           }
        });

    });


})(django.jQuery);