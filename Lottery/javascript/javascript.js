

// Luodaan globaali taulukko palkintoja varten
let palkinnot = []

// Funktio lisäämään palkinto [palkinnot] taulukkoon
function lisaaPalkinto() {
    let palkinto = document.getElementById("palkinto").value

    // Virhe
    const palkintoError = "Kenttä ei voi olla tyhjä"
    document.getElementById("error1").innerHTML = ""
    // Tarkistetaan onko palkinto-kenttä tyhjä
    if (palkinto === "") {
        document.getElementById("error1").innerHTML = palkintoError
        return
    }
    // Jos ei, lisätään palkinto taulukkoon
    palkinnot.push(palkinto)
    let kaikkiPalkinnot = "<ul class='two'>"
    for (let i = 0; i < palkinnot.length; i++) {
        kaikkiPalkinnot += "<li>" + palkinnot[i] + " €" + "</li>" // [i] lisää sillä iteraatiolla käsiteltävän i:n arrayhin
    }
    kaikkiPalkinnot += "</ul>"
    document.getElementById("palkintosumma").innerHTML = kaikkiPalkinnot
}

// Luodaan globaali taulukko henkilöitä varten
let henkilot = []

// Funktio lisäämään henkilö [henkilot] taulukkoon
function lisaaHenkilo() {
    let nimi = document.getElementById("nimi").value
    // Virhe
    const nimiError = "Kenttä ei voi olla tyhjä"
    document.getElementById("error2").innerHTML = ""
    // Tarkistetaan onko nimi-kenttä tyhjä
    if (nimi === "") {
        document.getElementById("error2").innerHTML = nimiError
        return
    }
    // Jos ei, lisätään nimi taulukkoon
    henkilot.push(nimi)
    let kaikkiNimet = "<ul class='three'>"
    for (let i = 0; i < henkilot.length; i++) {
        kaikkiNimet += "<li>" + henkilot[i] + "</li>"
    }
    kaikkiNimet += "</ul>"  // liittää tablen sulkukomennon kaikkiNimet muuttujaan
    document.getElementById("henkilot").innerHTML = kaikkiNimet
}

// Luodaan globaali taulukko henkilöille ja palkinnoille
let henkilotJaPalkinnot = []

// Luodaan funktio yhdistämään henkilöt ja palkinnot
function palkinto() {
    // Virhe-ilmoitus mikäli taulukot ovat tyhjiä
    document.getElementById("error3").innerHTML = ""
    if ((henkilot.length === 0) && (palkinnot.length === 0)){
        document.getElementById("error3").innerHTML = "Molemmat taulukot ovat tyhjiä"
        return
    }
    if (henkilot.length === 0) {
        document.getElementById("error3").innerHTML = "Henkilöt-taulukko on tyhjä"
        return
    }
    if (palkinnot.length === 0) {
        document.getElementById("error3").innerHTML = "Palkinnot-taulukko on tyhjä"
        return
    }

    /*if (henkilot.length === 0 || palkinnot.length === 0) {
        document.getElementById("error3").innerHTML += "Toinen tai molemmat taulukoista ovat tyhjiä" + "<br>"
        return
    }*/
    // Haetaan splice-metodilla ja Math-funktioilla satunnainen elementti taulukoista [palkinnot] ja [henkilot] ja lisätään muuttujiin
    const randName = henkilot.splice(Math.floor(Math.random()*henkilot.length), 1)
    const randPalk = palkinnot.splice(Math.floor(Math.random()*palkinnot.length), 1)

    // Lisätään taulukkoon [henkilotJaPalkinnot] satunnaiset henkilö- ja palkinto-yhdistelmät
    henkilotJaPalkinnot.push(randPalk + " € : " + randName)
    let henkjapalk = "<ul class='one'>"
    for (let i = 0; i < henkilotJaPalkinnot.length; i++) {
        henkjapalk += "<li>" + henkilotJaPalkinnot[i] + "</li>"
    }
    henkjapalk += "</ul>"
    document.getElementById("namee").innerHTML = henkjapalk
}
