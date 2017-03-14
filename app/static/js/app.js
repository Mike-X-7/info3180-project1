/* Validating form on submit */
function validateForm() {
    var a = document.forms["myForm"]["firstname"].value;
    var b = document.forms["myForm"]["lastname"].value;
    var c = document.forms["myForm"]["username"].value;
    var d = document.forms["myForm"]["age"].value;
    var e = document.forms["myForm"]["bio"].value;
    var f = document.forms["myForm"]["image"];
    
    if (a == "") {
        alert("PLEASE ENTER YOUR FISTNAME");
        return false;
    }
    if (b == "") {
        alert("PLEASE ENTER YOUR LASTNAME");
        return false;
    }
    if (c == "") {
        alert("PLEASE ENTER A UNIQUE USERNAME");
        return false;
    }
    if (d == "") {
        alert("PLEASE ENTER YOUR AGE");
        return false;
    }
    if (e == "") {
        alert("PLEASE WRITE SOMETHING ABOUT YOURSELF");
        return false;
    }
    if (f.files.length == 0) {
        alert("PLEASE SELECT AN IMAGE TO UPLOAD");
        return false;
    }
}





 /* Customized Alert Box */ 
var ALERT_TITLE = "Oops!";
var ALERT_BUTTON_TEXT = "Ok";

if(document.getElementById) {
    window.alert = function(txt) {
        createCustomAlert(txt);
    }
}

function createCustomAlert(txt) {
    var d = document;

    if(d.getElementById("modalContainer")) return;

    var mObj = d.getElementsByTagName("body")[0].appendChild(d.createElement("div"));
    mObj.id = "modalContainer";
    mObj.style.height = d.documentElement.scrollHeight + "px";

    var alertObj = mObj.appendChild(d.createElement("div"));
    alertObj.id = "alertBox";
    if(d.all && !window.opera) alertObj.style.top = document.documentElement.scrollTop + "px";
    alertObj.style.left = (d.documentElement.scrollWidth - alertObj.offsetWidth)/2 + "px";
    alertObj.style.visiblity="visible";

    var h1 = alertObj.appendChild(d.createElement("h1"));
    h1.appendChild(d.createTextNode(ALERT_TITLE));

    var msg = alertObj.appendChild(d.createElement("p"));
    //msg.appendChild(d.createTextNode(txt));
    msg.innerHTML = txt;

    var btn = alertObj.appendChild(d.createElement("a"));
    btn.id = "closeBtn";
    btn.appendChild(d.createTextNode(ALERT_BUTTON_TEXT));
    btn.href = "#";
    btn.focus();
    btn.onclick = function() { removeCustomAlert();return false; }

    alertObj.style.display = "block";

}

function removeCustomAlert() {
    document.getElementsByTagName("body")[0].removeChild(document.getElementById("modalContainer"));
}