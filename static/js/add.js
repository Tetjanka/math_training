window.onclick = function(event)  {
    let target = event.target;
    if (target.id == "add_send_button"){
        add();
    }


};



function add () {


    console.log("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr");


    fetch('http://127.0.0.1:8000/add/')
        .then(res => res.text())          // convert to plain text
        .then(text => console.log(text))

/*
        .then(function (response) {
            return response.json(); // But parse it as JSON this time
        })
        .then(function (json) {
            console.log('GET response as JSON:');
            //console.log(json); // Here’s our JSON object
            console.log(JSON.stringify(json));
        })*/
};
