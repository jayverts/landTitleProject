
$(document).ready(function(){
  $("#updateModal").modal();
  $("#updateModal").modal("close");

  $("#updateButton").on('click', function(event) {
    console.log("button clicked");
    $("#updateModal").modal("open");
  });
 });

function zipFunction() {
var input = document.getElementById("zipInput").value;
window.location.href = 'http://production.shippingapis.com/ShippingAPITest.dll?API=CityStateLookup&XML=<CityStateLookupRequest USERID="307VERDO2690"><ZipCode ID= "0"><Zip5>'+input+'</Zip5></ZipCode></CityStateLookupRequest>';
}
