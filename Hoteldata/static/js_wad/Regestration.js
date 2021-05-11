function matchPassword() {
  var pw1 = document.getElementById("pswd");
  var pw2 = document.getElementById("confirm-pswd");
  if (pw1 != pw2) {
    alert("Passwords did not match");
  } else {
    alert("Password created successfully");
  }
}
