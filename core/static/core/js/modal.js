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
    const botoesAbrirModal = document.querySelectorAll(".abrirModal");
    const modal = document.getElementById("myModal2");
    const botoesFecharModal = document.querySelectorAll(".fecharModal")

    botoesAbrirModal.forEach(botao => {
        botao.addEventListener("click", () => {
            modal.showModal();    
        });
        
    });

    botoesFecharModal.forEach((button) => {
        button.addEventListener("click", () => {
            modal.close();
        });
    })
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