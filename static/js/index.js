
let crop1;
let crop2; 

var loadFile1 = function(event) {
	console.log(event.target.files.length);
 	var image = document.getElementById('img1');
	image.src = URL.createObjectURL(event.target.files[0]);
	var image4 = document.getElementById('img4');
	console.log(typeof crop1);
	if (typeof crop1 !=="undefined" ) {
		crop1.destroy();
		crop1= Jcrop.attach(image4);

	} else {
		crop1= Jcrop.attach(image4);
	};
		
	console.log(typeof crop1);
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
crop1.listen('crop.change',(widget,e) => {
	console.log(widget.pos);
	console.log(widget.pos.x);
	var xhr=new XMLHttpRequest();
	var fd=new FormData();
	fd.append("requestinfo", 'crop1pos')
	fd.append("x",widget.pos.x)
	fd.append("y",widget.pos.y)
	fd.append("w",widget.pos.w)
	fd.append("h",widget.pos.h)
	
	xhr.open("POST","/",true);
	xhr.send(fd);
	xhr.onload=function(e) {
		if(this.readyState === 4) {
			console.log("Server returned: ",e.target.responseText);		

		}
	};

	});


	};

	};
var loadFile2 = function(event) {
	console.log(event.target.files.length);
 	var image = document.getElementById('img2');
	image.src = URL.createObjectURL(event.target.files[0]);
	var image3 = document.getElementById('img3');
	console.log(event.target.id)
	if (typeof crop2 !=="undefined" ) {
		crop2.destroy();
		crop2= Jcrop.attach(image3);

	} else {
		crop2= Jcrop.attach(image3);
	};	
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
	

