function activateShortner(){
    document.getElementById("asText").disabled = false;
}

function shortenUrl(){
var value = $('.input1').val();
console.log(value)
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

function copy(){
     var short_Url  = document.getElementById("kom");
     short_Url.select();
     alert(short_Url.value)
     document.execCommand("Copy");

}
