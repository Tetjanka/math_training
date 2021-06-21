/*window.onclick = function(event) {
    let target = event.target;
    if (target.id == "add"
        || target.id == "subtr"
        || target.id == "divis"
        || target.id == "multi"){

            send_action('http://127.0.0.1:8000/start/', {"target": target.id})
                .then((data) => {
                    concole.log(data);
                });
    }
}

async function send_action((url = '', data = {})){
    console.log(target);
    let res = await fetch (url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data),

    });

    return await res.json();
}
*/

window.onclick = function(event) {
    let target = event.target;
    if (target.id == "add"
        || target.id == "subtr"
        || target.id == "divis"
        || target.id == "multi"){

            send_action(target.id);
    }
};

async function send_action(target){
    console.log(target);
    try{
        let res = await fetch ('http://127.0.0.1:8000/start/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(target),

        });

        let result = await res.json();

        console.log("JSON.stringify(result)");
        console.log(JSON.stringify(result));
    } catch (error){
        console.error('Ошибка:', error);
    }

    if (target.id == "add"){
        add (result);
        console.log("add");
    }
    else {
        console.log("not add");
    }
};









/*
window.onclick = function(event) {
    let target = event.target;
    if (target.id == "add"
        || target.id == "subtr"
        || target.id == "divis"
        || target.id == "multi"){

            send_action(target.id);
    }
}

async function send_action(target){
    console.log(target);
    let res = await fetch ('http://127.0.0.1:8000/start/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(target),

    });

    let result = await res.json();

    concole.log(JSON.stringify(result));
}
*/
