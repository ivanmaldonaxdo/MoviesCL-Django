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
document.getElementById("pelicula").value = ""
document.getElementById("buscar").addEventListener("click",function (e) {
    e.preventDefault();
    peli = document.getElementById("pelicula").value
    console.log(peli);
    pasarIdCli(1);
}


)