console.log("Hello from our JS")

async function start() { //async function needed because API requests take a long time. Other parts of the code should still run while we wait.
    const response = await fetch("https://api.genius.com/search?q=wildest&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J") //await to do the following code until promise is resolved / we have the API data
    const data = await response.json()

    var num = Object.keys(data.response.hits).length
    //alert(num)

   // alert(data.response.hits[0].result.full_title)
    let text = "";
    for (let counter = 0; counter < num; counter++) {
        text += data.response.hits[counter].result.full_title + "<br>" + "<br>";
    }
   // alert(text)
    createSongPage(text)
    // console.log(data.response.hits[0].result.full_title)
    // alert(data.response.hits[0].result.full_title)
    // createSongPage(data.response.hits[0].result.full_title)

}
// start()

function createSongPage(songList){
    
    document.getElementById("song").innerHTML = songList
    // document.getElementById("song").innerHTML = `
    // <button onclick="loadBySong(this.value)">Click me</button> 
    // <p>Song List</p>

    // ${Object.keys(songList).map(function (song) {
    //     return`<p>${songList}</p>`
    // }).join('')}
    
}

function loadBySong(song){
    
    //alert(song)

    // var nameValue = document.getElementById("lyricID").value;
    // console.log(nameValue);
    // myUrl = "https://lunarfy-server.florayfr1.repl.co/search/" + nameValue

    // alert(nameValue)
}
function grabInput(){

    var lyric = document.getElementById("lyricID").value
    console.log(lyric)
   // alert(lyric)
    const lyricLink = new URL (`https://api.genius.com/search?q=${lyric}&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J`)
    
    //alert("I'm goin in")
    grabSong(lyric)

}
async function grabSong(lyric) {

    // var nameValue = document.getElementById("lyricID").value
    // console.log(nameValue)
    // myUrl = "https://lunarfy-server.florayfr1.repl.co/search/" + nameValue
    // myUrl = "https://dog.ceo/api/breeds/image/" + nameValue
    // https://dog.ceo/api/breed/${lyric}/images
    //https://lunarfy-server.florayfr1.repl.co/search/${lyric}
    //https://api.genius.com/search?q=${lyric}&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J
    // alert(lyric)
    //alert(lyric)
    const response = await fetch(`https://api.genius.com/search?q=${lyric}&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J`) //await to do the following code until promise is resolved / we have the API data
    const data = await response.json()
    // console.log(data)
    // alert(lyric)
    

    //try {
    //const response = await fetch("https://api.genius.com/search?q=wildest&access_token=XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J") //await to do the following code until promise is resolved / we have the API data
   // const data = await response.json()
    //alert("Yo I made it here lol")
        // alert(data.response)

      /*} catch (e) {
        console.log("There was a problem fetching that")
        alert("There was a problem fetching that...")
    }*/


    // const response = await fetch(`https://lunarfy-server.florayfr1.repl.co/search/${lyric}`) //await to do the following code until promise is resolved / we have the API data
    // const data = await response.json()
    // console.log(data)
    // alert(lyric)
    // const response = await fetch(`https://dog.ceo/api/breed/${lyric}/images`)

    // const data = await response.json()


    // alert(data.response.hits)


    var num = Object.keys(data.response.hits).length
    //alert(num)

    //alert(data.response.hits[0].result.full_title)
    let text = "";
    for (let counter = 0; counter < num; counter++) {
        text += data.response.hits[counter].result.full_title + "<br>" + "<br>";
    }
    //alert(text)
    createSongPage(text)
}