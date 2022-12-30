
var loadFile1 = function(event) {
	console.log(event.target.files.length);
 	var image = document.getElementById('img1');
	image.src = URL.createObjectURL(event.target.files[0]);

    
};

var loadFile2 = function(event) {
	console.log(event.target.files.length);
 	var image = document.getElementById('img2');
	image.src = URL.createObjectURL(event.target.files[0]);

    
};
	

