var space = document.createElement("br");

var name = document.getElementsByClassName("ProfileHeaderCard-nameLink u-textInheritColor js-nav");
var RealName = name[0];

http://localhost:5000/get_name_parsed


var sueldo = document.createElement("a");
sueldo.textContent = parse_name;
sueldo.href = "https://www.newtral.com/";

var name = document.getElementsByClassName("ProfileHeaderCard-name");
var RealName = name[0];

var DivName = document.getElementsByClassName("ProfileHeaderCard");
var RealDivname = DivName[0];

//document.insertBefore(RealName, sueldo);
RealName.appendChild(space);
RealName.appendChild(sueldo);

