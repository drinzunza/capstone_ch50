
function init() {
    console.log("List Posts Page");
}

function showModal() {
    const mdl = $("#modalCreate");              // find the template
    const myModal = new bootstrap.Modal(mdl);    // create a modal
    myModal.show();                             // show the modal
}

window.onload = init;