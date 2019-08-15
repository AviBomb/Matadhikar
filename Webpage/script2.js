var server_addr="http://localhost:5000"
var route="/api/v1/login"
function sendact() {
    var data_file = server_addr+route;
    // alert(data_file);
    var http_request = new XMLHttpRequest();
    
    var voter_id= document.getElementById("voter_id").value;
    var ph_no= document.getElementById("ph_no").value;
    var temp_password= document.getElementById("temp_password").value;
    var time= Math.floor(Date.now()/1000)
    var params =JSON.stringify({'voter_id': voter_id,'ph_no': ph_no,'temp_password': temp_password,'time': time});

    http_request.onreadystatechange = function() {//Call a function when the state changes.
        if(http_request.readyState == 4) {
            var jsonObj = JSON.parse(http_request.responseText);
            // console.log(jsonObj.status);
            if(jsonObj.status === "User Doesn't exist or Wrong password")
            {
                // console.log(jsonObj.status);
                document.getElementById("status").innerHTML="Incorrect Credentials Please Re-enter the data";
                document.getElementById("voter_id").value = '';
                document.getElementById("ph_no").value= '';
            }
            else
            {
                document.getElementById("status").innerHTML='';
                // console.log(jsonObj.status);
                location.replace('Reset_Password.html')
            }    
        }
    }
    http_request.open('POST', data_file, true);
    http_request.send(params);
}



