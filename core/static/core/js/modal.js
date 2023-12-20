document.addEventListener("DOMContentLoaded", function() {
    const botoesAbrirModal = document.querySelectorAll(".abrirModal");

    botoesAbrirModal.forEach(botao => {
        botao.addEventListener("click", () => {
            modal.showModal();    
        });
        
    });

    const modal = document.getElementById("myModal");
    const botoesFecharModal = document.querySelectorAll(".fecharModal")

    botoesFecharModal.forEach((button) => {
        button.addEventListener("click", () => {
            modal.close();
        });
    })

});
document.addEventListener("DOMContentLoaded", function() {
    const openModal = document.getElementById("abrirModal2");
    const modal = document.getElementById("myModal2");
    const closeButton = document.getElementById("fecharModal2")
    openModal.addEventListener("click", () => {
        modal.showModal();
    });
    closeButton.addEventListener("click", () => {
        modal.close();
    });
});
document.addEventListener("DOMContentLoaded", function() {
    const openModal = document.getElementById("abrirModal3");
    const modal = document.getElementById("myModal3");
    const closeButton = document.getElementById("fecharModal3")
    openModal.addEventListener("click", () => {
        modal.showModal();
    });
    closeButton.addEventListener("click", () => {
        modal.close();
    });
});