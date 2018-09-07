$(document).ready(function(){
  // $("#id_username").addClass("form-control input-lg");
  // $("#id_username").attr("placeholder","Nombre de usuario");
  // $("#id_password").addClass("form-control input-lg");
  // $("#id_password").attr("placeholder","ContraseÃ±a");
  // $("#submit").click(function(){
  //   var campo= $("#id_username").val();
  //   if (!campo) {
  //     $("#content").addClass("has-error");
  //   }
    
  // })
  var url= String( window.location.href )
  var url2= String( window.location.href ).split('?')[0]
 
  if (url != url2) {
    function locationVars (vr)
    {

      var src = String( window.location.href ).split('?')[1];
      var vrs = src.split('&');
      for (var x = 0, c = vrs.length; x < c; x++)
      {
        if (vrs[x].indexOf(vr) != -1)
        {
          return decodeURI( vrs[x].split('=')[1] );
          break;

        };
      };
    };
    
    var param = String( window.location.href ).split('?')[1]; //--- para obtener el parametro
    var campo =param.split('=')[0]; //---- para obtener el nombre del parametro 
   
    var email = locationVars('email');
    var user = locationVars('user');

    if (campo=='user') { 
      $("#id_username").attr('value', user);
    };

    if (campo=='email') {
      $("#id_email").attr('value', email);
    };
 
  }; 
    
})