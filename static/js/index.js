document.addEventListener('DOMContentLoaded', function() {
    // changing TODO lists
    todos = document.querySelectorAll('.TODO');
    for (let todo of todos) {
        todo.style.backgroundColor = 'lightgreen';
        todo.style.fontWeight = 'bold';
        todo.querySelector("button").innerHTML = 'DONE';
    };

    //changing DONE lists
    dones = document.querySelectorAll('.DONE');
    for (let done of dones) {
        done.style.backgroundColor = 'indianred';
        done.querySelector("button").innerHTML = 'CANCEL';
    };
});