
    $(document).ready(function() {
        function block_form() {
            $("#loading").show();
            $('textarea').attr('disabled', 'disabled');
            $('input').attr('disabled', 'disabled');
        }

        function unblock_form() {
            $('#loading').hide();
            $('textarea').removeAttr('disabled');
            $('input').removeAttr('disabled');
            $('.errorlist').remove();
        }

        // prepare Options Object for plugin
        var options = {
            beforeSubmit: function(form, options) {
                // return false to cancel submit
                block_form();
            },
            success: function() {
                unblock_form();

                $('.modal-body').load('/render/62805',function(result){
                    $('#myModal').modal({show:true});
                });

                $("#form_ajax").show();
                setTimeout(function() {
                    $("#form_ajax").hide();
                }, 5000);
            },
            error:  function(resp) {
                unblock_form();
                $("#form_ajax_error").show();
                // render errors in form fields
                var errors = JSON.parse(resp.responseText);
                console.log(errors);
                for (error in errors) {
                    var id = '#id_' + error + '_span';
                    console.log(id);
                   

                    if(id=='#id___all___span'){
                       $('p').parent(".alerta").addClass('alert alert-danger').prepend(errors[error]);
                  
                    }else{
                        $('p').parent(".alerta").removeClass('alert alert-danger')
                    }

                    $(id).prepend(errors[error]);
                 
                }
                setTimeout(function() {
                    $("#form_ajax_error").hide();
                }, 5000);
            }
        };

        $('#ajaxform').ajaxForm(options);
    });
