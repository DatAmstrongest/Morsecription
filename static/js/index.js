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
			$("#gear").removeClass("rotate-img-right");
      		    $("#CiphertextTextArea").val(html.ciphertext);

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
    
});
