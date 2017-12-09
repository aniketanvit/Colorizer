function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                return allText;
                // alert(allText);
            }
        }
    }
    rawFile.send(null);
}

function download(filename, text) {
    var pom = document.createElement('a');
    pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    pom.setAttribute('download', filename);

    if (document.createEvent) {
        var event = document.createEvent('MouseEvents');
        event.initEvent('click', true, true);
        pom.dispatchEvent(event);
    }
    else {
        pom.click();
    }
}

// var htmlObj = readTextFile("input.html"), parser = new DOMParser(), doc = parser.parseFromString(xmlString, "text/xml");
window.onload = function() {
		var fileInput = document.getElementById('fileInput');
		var fileDisplayArea = document.getElementById('fileDisplayArea');

		fileInput.addEventListener('change', function(e) {
			var file = fileInput.files[0];
      console.log(file);
			var textType = /text.*/;

			if (file.type.match(textType)) {
				var reader = new FileReader();

				reader.onload = function(e) {
          var s = '<div id="myDiv"></div>';
          var htmlObject = document.createElement('div');
          htmlObject.innerHTML = reader.result;
          // htmlObject.getElementById("myDiv").style.marginTop = reader.result;

          var htmlObj = $(reader.result);
          console.log(htmlObject);
          var rows = htmlObject.querySelector(".wikitable").querySelector("tbody").querySelectorAll("tr");
          var list = [];
          for (i = 0; i < rows.length; i++) {
            var val = rows[i].querySelector("td");
            list.push(val.innerText)
          }
          fileDisplayArea.innerText = list;
          download('test.txt', list);
				}
				reader.readAsText(file);
			} else {
				fileDisplayArea.innerText = "File not supported!"
			}
		});
}

/*
var htmlObj = $(readTextFile("input.html"));
console.log(readTextFile("input.html"));
var rows = htmlObj.querySelector("table").querySelector("tbody").querySelectorAll("tr");
var list = [];
for (i = 0; i < rows.length; i++) {
  var val = rows[i].querySelector("td");
  list.push(val.innerText)
}

var create = document.getElementById('create'),
    textbox = document.getElementById('textbox');

  create.addEventListener('click', function () {
    var link = document.createElement('a');
    link.setAttribute('download', 'info.txt');
    link.href = makeTextFile(list);
    document.body.appendChild(link);

    // wait for the link to be added to the document
    window.requestAnimationFrame(function () {
      var event = new MouseEvent('click');
      link.dispatchEvent(event);
      document.body.removeChild(link);
    });

  }, false);
*/
