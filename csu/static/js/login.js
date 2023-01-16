function Judge() {
    var user = document.getElementById("uname").value;
    var password = document.getElementById("password").value;
    if ((user == null || user === "")&&(password == null || password === "")){
        document.getElementById("errMsg").innerHTML = "请输入用户名和密码";
        return false;
    }
    if (user == null || user === "") {
        document.getElementById("errMsg").innerHTML = "请输入用户名";
        return false;
    }
    if (password == null || password === "") {
        document.getElementById("errMsg").innerHTML = "请输入密码";
        return false;
    }
    return true;
}