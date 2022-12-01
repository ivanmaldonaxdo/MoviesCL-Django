function pasarIdCli(idCli) {
    $.ajax({
        type: "GET",
        url: '/get_genres',
        // data: {
        //     "id_cli": idCli,
        // },
        dataType: "json",
        success: function (data) {
            console.log(data);
            // any process in data
            // alert("successfull")
        },
        failure: function () {
            console.log("fallo");
            // alert("failure");
        }
    });
    
}

function getMovies(query) {

    // let data_movies = [] 
    $.ajax({
        type: "GET",
        url: '/get_movies',
        data: {
            "query": query,
        },
        dataType: "json",
        success: function (data) {
            document.querySelector("#grid_artics").innerHTML = ""
            let  data_array =  Object.create(data);
            console.table(data_array.results);

            
            data_movies = data_array.results;
            Array.from(data_movies).map(p => createPeli(p));

            // any process in data
            // alert("successfull")
        },
        failure: function () {
            console.log("fallo");
            // alert("failure");
        }
    });
}

document.getElementById("pelicula").value = "scarface"
document.getElementById("buscar").addEventListener("click",function (e) {
    e.preventDefault();
    peli = document.getElementById("pelicula").value
    // console.log(peli);
    getMovies(peli);
    // console.log(movies);
    // pasarIdCli(1);
}



)
function getUrlmage(path) {
    let secure_base_url = "https://image.tmdb.org/t/p/",
        size = "original";
    let url = secure_base_url+size+path;
    // console.log(url);
    return url;
}   
function createPeli(peli) 
{
    const grid = document.querySelector("#grid_artics");

    let article= `<article class="item">
                    <img src="${getUrlmage(peli.poster_path)}" alt="" srcset="" class="box">
                    <h3>${peli.title}</h3>   
                </article>`
    if (peli.poster_path != null){
        grid.innerHTML += article
    }
    
}