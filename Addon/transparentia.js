var space = document.createElement("br");

var name = document.getElementsByClassName("ProfileHeaderCard-nameLink u-textInheritColor js-nav");
var RealName = name[0];
var salary;

$.ajax({
    url: '/GiveMeMoney',
    data:{ param: RealName.textContent},
    type: 'POST',
    success: function(response){
        console.log(response);
        salary = response.salary;
    },
    error: function(error){
        console.log(error);
    }
});

var sueldo = document.createElement("a");
sueldo.textContent = salary;
sueldo.href = "https://www.newtral.com/";

var name = document.getElementsByClassName("ProfileHeaderCard-name");
var RealName = name[0];

var DivName = document.getElementsByClassName("ProfileHeaderCard");
var RealDivname = DivName[0];

//document.insertBefore(RealName, sueldo);
RealName.appendChild(space);
RealName.appendChild(sueldo);