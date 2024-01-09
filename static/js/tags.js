document.addEventListener('DOMContentLoaded', function() {
    let editForms = document.querySelectorAll('.editForms');
    
    for (let editForm of editForms) {
        let form = editForm.querySelector('form');
        let editButton = editForm.querySelector('#edit_button');
        form.style.display = 'none';
        
        // edit button
        editButton.addEventListener('click', function() {
            if (form.style.display == 'none') { 
                form.style.display = 'block';
            } else {
                form.style.display = 'none';
            }

        });

        // confirm button
        let confirmButton = form.querySelector('button');
        confirmButton.addEventListener('click', function() {
            form.style.display = 'none';
        });
    };
});