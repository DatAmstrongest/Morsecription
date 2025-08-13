const SLEEP_TIME = 500

// sleep time expects milliseconds
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}
function showError(errorModal, message){
   document.getElementById("errorModalBody").innerHTML=message;
   errorModal.show();
}
//TODO: Refactoring in API calls is needed
$(document).ready(function() {   
    const errorModal = new bootstrap.Modal(document.getElementById('errorModal'));

    $('#Ciphertext_count_message').html('0 / ' + 1000);
    $('#Plaintext_count_message').html('0 / ' + 200);

    $('#PlaintextTextArea').keyup(function() {
      var text_length = $('#PlaintextTextArea').val().length;
      var text_remaining = text_max - text_length;

      $('#Plaintext_count_message').html(text_length + ' / ' + text_max);
    });

    $('#CiphertextTextArea').keyup(function() {
      var text_length = $('#CiphertextTextArea').val().length;
      var text_remaining = text_max - text_length;

      $('#Ciphertext_count_message').html(text_length + ' / ' + text_max);
    });

    $('#encryptButton').click(function(){
        $("#gear").removeClass("rotate-img-left")
        $("#gear").addClass("rotate-img-right")
        sleep(SLEEP_TIME).then(() =>{
            $.ajax({
                type: "POST",
                url: "/encrypt",
                headers:{ 'Content-Type': 'application/json'},
                dataType: "json",
                data: JSON.stringify(
                {
                    plaintext: $("#PlaintextTextArea").val()
                }),
                cache: false,
                success: function(html){
		    $("#gear").removeClass("rotate-img-right");
      		    $("#CiphertextTextArea").val(html.ciphertext);

		    if (html.error.length>0){
	            	showError(errorModal, html.error);
			return;
	            }

		    fetch("/sound", {
			method: "POST",
			headers: {
			    "Content-Type": "application/json"
			},
			body: JSON.stringify({
			    ciphertext: $("#CiphertextTextArea").val()
			})
		    })
		    .then(response => {
			const contentType = response.headers.get("Content-Type");
			if (!response.ok || !contentType.startsWith("audio")) {
			    throw new Error("Invalid response from /sound");
			}
			return response.blob();
		    })
		    .then(blob => {
			const audioUrl = URL.createObjectURL(blob);
			const audioEl = document.getElementById("audioButton");
			const download = document.getElementById("download");

			download.href = audioUrl;
			audioEl.src = audioUrl;
			audioEl.load();
			audioEl.style.display = "block";
			download.style.display = "block";
		    })
		    .catch(error => {
			console.error("Failed to fetch audio:", error);
		    });

                }
            });
        });
        
    })
    //TODO: Add audio api call also here
    //TODO: Refactor audio call
    $("#decryptButton").click(() => {
        $("#gear").removeClass("rotate-img-right")
        $("#gear").addClass("rotate-img-left")
        sleep(SLEEP_TIME).then(() =>{
            $.ajax({
                type: "POST",
                url: "/decrypt",
                headers:{ 'Content-Type': 'application/json'},
                dataType: "json",
                data: JSON.stringify(
                {
                    ciphertext: $("#CiphertextTextArea").val()
                }),
                success: function(html){
                    $("#gear").removeClass("rotate-img-left")
                    $("#PlaintextTextArea").val(html.plaintext)

		    if (html.error.length>0){
	            	showError(errorModal, html.error);
			return;
	            }
                }
            });
        })
    })
    
});
