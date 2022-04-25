const origin = document.querySelector('#origin');
const airportName = document.querySelector('#airport_name');
const destination = document.querySelector('#destination');
const destAirportName = document.querySelector('#dest_airport_name');
const showFlights = document.querySelector('#show_flights');

window.addEventListener('load', ()=>{
    airportName.style.display = 'none';
    destAirportName.style.display = 'none';
})

origin.addEventListener('focusout', async()=>{
    airportName.innerHTML = 'Locating Closest Airport';
    let originCity = origin.value;
    let response = await fetch(`/origin?origin=${originCity}`)
    let raw = await response.json()
    airportName.style.display = 'block';
    if (raw.name == 'Please Enter A City'){
        airportName.textContent = "Please Enter A City";
    }
    else{
        airportName.textContent = `${raw.name} Airport 🛫`;
    }
});

destination.addEventListener('focusout', async()=>{
    destAirportName.innerHTML = 'Locating Closest Airport';
    let destinationCity = destination.value;
    let response = await fetch(`/destination?destination=${destinationCity}`)
    let raw = await response.json()
    destAirportName.style.display = 'block';
    if (raw.name == 'Please Enter A City'){
        destAirportName.textContent = "Please Enter A City";
    }
    else{
        destAirportName.textContent = `${raw.name} Airport 🛬`;
    }
});

showFlights.addEventListener('click', (event)=>{
    event.preventDefault();
    originAirport = airportName.value;
    destinationAirport = destAirportName.value;
    console.log(originAirport, destinationAirport)
})