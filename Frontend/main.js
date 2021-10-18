console.log("Hello from our JS")

function createSongPage(songList){
    
    document.getElementById("song").innerHTML = songList
    
}
function grabInput(){

    var lyric = document.getElementById("lyricID").value
    console.log(lyric)
    const lyricLink = new URL (`https://api.genius.com/search?q=${lyric}&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J`)
    grabSong(lyric)

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