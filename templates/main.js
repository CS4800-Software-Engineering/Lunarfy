console.log("Welcome to LunarVerse")


function passwordMatch(){
    var password1 = document.getElementById('pass').value;
    var password2 = document.getElementById('pass2').value;

    if (password1 != password2){
      alert("Passwords do not match!")
    }else{
      alert("yayyyy")
    }
}