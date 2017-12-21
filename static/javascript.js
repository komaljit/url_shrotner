function activateShortner(){
    document.getElementById("asText").disabled = false;
    
}

function shortenUrl(){
    
var value = $('.input1').val();
console.log(value)
$.ajax({
  type: 'POST',
  url: "http://localhost:6100/get_short_url",
  data: JSON.stringify(value),
  contentType: 'application/json',
  success: function(data){
      console.log(data);
    // do something with the received data
    document.getElementById("kom").value = data;
  }
});
}