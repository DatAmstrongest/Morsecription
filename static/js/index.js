const SLEEP_TIME = 500

// sleep time expects milliseconds
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }

$(document).ready(function() {
    $('#encryptButton').click(function(){
        $("#gear").removeClass("rotate-img-left")
        $("#gear").addClass("rotate-img-right")
        sleep(SLEEP_TIME).then(() =>{
            $.ajax({
                type: "POST",
                url: "http://localhost:5002/encrypt",
                headers:{ 'Content-Type': 'application/json'},
                dataType: "json",
                data: JSON.stringify(
                {
                    plaintext: $("#PlaintextTextArea").val()
                }),
                cache: false,
                success: function(html){
                    $("#gear").removeClass("rotate-img-right")
                    $("#CiphertextTextArea").val(html.ciphertext)

                }
            });
        });
        
    })
    $("#decryptButton").click(() => {
        $("#gear").removeClass("rotate-img-right")
        $("#gear").addClass("rotate-img-left")
        sleep(SLEEP_TIME).then(() =>{
            $.ajax({
                type: "POST",
                url: "http://localhost:5002/decrypt",
                headers:{ 'Content-Type': 'application/json'},
                dataType: "json",
                data: JSON.stringify(
                {
                    ciphertext: $("#CiphertextTextArea").val()
                }),
                success: function(html){
                    $("#gear").removeClass("rotate-img-left")
                    $("#PlaintextTextArea").val(html.plaintext)
                }
            });
        })
    })
    
    $("#audioButton").click(function(){
        sleep(SLEEP_TIME).then(() =>{
            $.ajax({
                type: "POST",
                url: "http://localhost:5002/toSound",
                headers:{ 'Content-Type': 'application/json'},
                dataType: "json",
                data: JSON.stringify(
                {
                    ciphertext: $("#CiphertextTextArea").val()
                }),
                success: function(result){
                    $("#mp3Download").click()
                }
            });
        })
    })
    
});
