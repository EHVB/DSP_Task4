
let crop1;
let crop2; 

var loadFile1 = function(event) {
	console.log(event.target.files.length);
 	var image = document.getElementById('img1');
	image.src = URL.createObjectURL(event.target.files[0]);
	var image4 = document.getElementById('img4');
	crop1= Jcrop.attach(image4);	
	var xhr=new XMLHttpRequest();
    var fd=new FormData();
	fd.append("image1",event.target.files[0],event.target.files[0].filename);
	fd.append("requestinfo","image1" );
	xhr.open("POST","/",true);
	xhr.send(fd);
	xhr.onload=function(e) {
		if(this.readyState === 4) {
			console.log("Server returned: ",e.target.responseText);
			var image4 = document.getElementById('img4');
			console.log(e.target.responseText.length);
			response=e.target.responseText;		  
			image4.src=response;
	


		}
	};

	};

var loadFile2 = function(event) {
	console.log(event.target.files.length);
 	var image = document.getElementById('img2');
	image.src = URL.createObjectURL(event.target.files[0]);
	var image3 = document.getElementById('img3');
	console.log(event.target.id)
	crop2= Jcrop.attach(image3);	
	var xhr=new XMLHttpRequest();
    var fd=new FormData();
	fd.append("image2",event.target.files[0],event.target.files[0].filename);
	fd.append("requestinfo","image2" );
	xhr.open("POST","/",true);
	xhr.send(fd);
	xhr.onload=function(e) {
		if(this.readyState === 4) {
			console.log("Server returned: ",e.target.responseText);
			var image3 = document.getElementById('img3');
			console.log(e.target.responseText.length);
			response=e.target.responseText;		  
			image3.src=response;
	


		}
	};


};
	

