window.onload = function(){
    addClass();
    let answers = [];
    window.onclick = function(event)  {
        let target = event.target;
        if (target.id.includes( "add_send_button")){
            let result = toggleClass(target);
            if (result != undefined){
                answers.push (result);
                console.log (result);
            }

            console.log (answers);
        }





    }


};

function addClass(){
    let hidden_elem = document.getElementsByClassName("cont_train_2_1");
    let hidden_title = document.getElementsByClassName("cont_train_1");
    //console.log(hidden_elem);
    for (i = 0; i < hidden_elem.length; i++)
        if (hidden_elem[i].id != 1){
            //console.log(hidden_elem[i].id);
            //console.log(hidden_elem[i]);
            hidden_elem[i].classList.add ("hidden");
            //console.log("done");
    }
    for (i = 0; i < hidden_title.length; i++)
        if (hidden_title[i].id != 1){
            //console.log(hidden_title[i].id);
            //console.log(hidden_title[i]);
            hidden_title[i].classList.add ("hidden");
            //console.log("done");
    }
}

function toggleClass(target){
    get_number_task = target.id.replace(/[^0-9]/g,'');

    let answer = document.getElementById("answer " + get_number_task).value;

    if (answer == ""){
        alert ("It needs to write your answer");

        return;
    }
    else{
        answer = Number (answer);
        let active_task_title = document.getElementsByClassName("cont_train_1");
        let active_task = document.getElementsByClassName("cont_train_2_1");


        counter_title = 0;
        for (let item of active_task_title) {
            if (counter_title == 0){
                if (item.classList.contains("hidden") == false){
                    item.classList.add("hidden");
                    counter_title = 1;
                }
            }
            else if (counter_title ==1 ){
                item.classList.remove("hidden");

                break;
            }

        }
        counter = 0;
        for (let item of active_task) {
            if (counter == 0){
                if (item.classList.contains("hidden") == false){
                    item.classList.add("hidden");
                    counter = 1;
                }
            }
            else if (counter ==1 ){
                item.classList.remove("hidden");

                break;
            }

        }


        return answer;
    }





}

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
