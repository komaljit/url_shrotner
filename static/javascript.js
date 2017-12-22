function shortenUrl(){
var value = $('.input1').val();
if(value==""){
   return ""
}
$.ajax({
  type: 'POST',
  url: "http://34.230.73.181:6100/get_short_url",
  data: JSON.stringify(value),
  contentType: 'application/json',
  success: function(data){
    // do something with the received data
    document.getElementById("kom").value = data;
    document.getElementById("cbtn").style.display="block";
  }
});
}


function copy_st_url(){
     var short_Url  = document.getElementById("kom");
     short_Url.select();
     alert(short_Url.value)
     document.getElementById("cbtn").innerHTML="Copied"
     document.execCommand("copy");
}
