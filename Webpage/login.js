var server_addr="http://localhost:5000"
var route="/api/v1/login"
function sendact() {
    var data_file = server_addr+route;
    var http_request = new XMLHttpRequest();
    
    var voter_id= document.getElementById("voter_id").value;
    var password= document.getElementById("password").value;
    var params =JSON.stringify({'voter_id': voter_id,'password':password});

    http_request.onreadystatechange = function() {//Call a function when the state changes.
        if(http_request.readyState == 4) {
            var jsonObj = JSON.parse(http_request.responseText);
            // console.log(jsonObj.status);
            if(jsonObj.status === "User Doesn't exist or Wrong password")
            {
                document.getElementById("status").innerHTML="Incorrect Credentials Please Re-enter the data";
                document.getElementById("voter_id").value = '';
                document.getElementById("password").value= '';
            }
            else
            {
                document.getElementById("status").innerHTML='';
                // console.log(jsonObj.status);
                document.getElementById("voter_id").value = '';
                document.getElementById("password").value= '';   
                location.replace('candidates.html')
            }    
        }
    }
    http_request.open('POST', data_file, true);
    http_request.send(params);
}