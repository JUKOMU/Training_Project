function Judge2() {
    var user = document.getElementById("uname").value;
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    if ((user == null || user === "")&&(password1 == null || password1 === "")&&(password2 == null || password2 === "")){
        document.getElementById("p1").innerHTML = "请输入用户名和密码";
        return false;
    }
    if (user == null || user === "") {
        document.getElementById("p1").innerHTML = "请输入用户名";
        return false;
    }
    if (password1 == null || password1 === "") {
        document.getElementById("p1").innerHTML = "请输入密码";
        return false;
    }
    if (password2 == null || password2 === "") {
        document.getElementById("p1").innerHTML = "请输入确认密码";
        return false;
    }
    if (password1 !== password2) {
        document.getElementById("p1").innerHTML = "两次输入的密码不同";
        return false;
    }
    return true;
}