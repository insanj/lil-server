function debugLog(message) {
	$("body").append(message + "<br/>");
}


function talkToServer(data) {
	debugLog("Starting to talk...");
	$.ajax({
		url: "/json/?q=" + data,
		dataType: "json",
		success: function (response) {
			debugLog("Success: " + JSON.stringify(response));
		},
		error: function (response) {
			debugLog("Error: " + response.responseText);
		},
		always: function (response) {
			debugLog("Finished connection..." + response.responseText);
		}
	});
}

document.addEventListener("keypress", function () {
	debugLog("Talking...");
	talkToServer(new Date().toLocaleString("en-US"));
});

debugLog("Alive!");
