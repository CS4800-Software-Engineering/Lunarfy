console.log("Welcome to LunarVerse")

function createSongPage(songList){

    document.getElementById("song").innerHTML = songList

}
function grabInput(){

    var lyric = document.getElementById("lyricID").value
    console.log(lyric)
    //text = url_for('search', term=lyric)
    //const lyricLink = new URL (`https://api.genius.com/search?q=${lyric}&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J`)
    grabSong(lyric)
    //createSongPage(text)
}
async function grabSong(lyric) {


    const response = await fetch(`https://api.genius.com/search?q=${lyric}&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J`) //await to do the following code until promise is resolved / we have the API data
    const data = await response.json()

    var num = Object.keys(data.response.hits).length

    let text = "";
    for (let counter = 0; counter < num; counter++) {
        text += data.response.hits[counter].result.full_title + "<br>" + "<br>";
    }
    createSongPage(text)
}
function passwordMatch(){
    var password1 = document.getElementById('pass').value;
    var password2 = document.getElementById('pass2').value;

    if (password1 != password2){
      alert("Passwords do not match!")
    }else{
      alert("yayyyy")
    }
}