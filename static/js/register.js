function validate()
{
    var pwd1 = document.getElementById("pwd").value;
    var pwd2 = document.getElementById("pwd_2").value;
    if (pwd1 == pwd2)
    {
        document.getElementById("warning").innerHTML = "<font color = 'red'>√</font>"
    }
    else
    {
        document.getElementById("warning").innerHTML = "<font color = 'red'>×</font>"    
    }
}
