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
    const botoesAbrirModal = document.querySelectorAll(".abrirModal2");
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
    const botoesAbrirModal = document.querySelectorAll(".abrirModal3");
    const modal = document.getElementById("myModal3");
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