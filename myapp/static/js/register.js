function validateForm() {
    var empid = document.forms["regForm"]["empid"].value;
    var empname = document.forms["regForm"]["name"].value;
    var email = document.forms["regForm"]["email"].value;
    var phone = document.forms["regForm"]["phone"].value;
    var gender = document.forms["regForm"]["gender"].value;
    var job = document.forms["regForm"]["job"].value;



    if (empid == "") {
        alert("Employee Id must be filled out");
        return false;
    } else if (empname == "") {
        alert("Name must be fill out")
        return false;
    } else if (email == "") {
        alert("Email must be fill out")
        return false;
    } else if (phone == "") {
        alert("Phone number must be fill out")
        return false;
    } else if (gender == "") {
        alert("Gender must be fill out")
        return false;
    } else if (job == "") {
        alert("Job position must be fill out")
        return false;
    }
}







function validate() {
    var empid = document.getElementById("empid").value;
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var gender = document.getElementById("gender").value;
    var job = document.getElementById("job").value;
    var error_message = document.getElementById("error_message");

    error_message.style.padding = "10px";

    var text;
    if (empid.length < 5) {
        text = "Please Enter valid Employee Id";
        error_message.innerHTML = text;
        return false;
    }
    if (name.length < 3) {
        text = "Please Enter valid Name";
        error_message.innerHTML = text;
        return false;
    }
    if (email.indexOf("@") == -1 || email.length < 5) {
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
    }
    if (isNaN(phone) || phone.length != 10) {
        text = "Please Enter valid Phone Number";
        error_message.innerHTML = text;
        return false;
    }
    if (gender == "") {
        text = "Select a gender";
        error_message.innerHTML = text;
        return false;
    }
    if (job.length < 5) {
        text = "Please Enter valid Job position";
        error_message.innerHTML = text;
        return false;
    }
    alert("Form Submitted Successfully!");
    return true;
}