
function talkToServer() {
	console.log("Starting to talk...");
	$.ajax({
		url: "127.0.0.1:5000/json/?q=hello",
		success: function (response) {
			console.log("Done! " + response);
			$("body").append(response);
		},
		always: function () {
			console.log("Finished connection...");
		});
	});
}

document.onkeypress = function (e) {
	$("body").append("Talking...<br/>");
	talkToServer();
};
