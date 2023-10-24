document.addEventListener("DOMContentLoaded", function() {
    const openModal = document.getElementById("abrirModal");
    const modal = document.getElementById("myModal");
    const closeButton = document.getElementById("fecharModal")
    openModal.addEventListener("click", () => {
        modal.showModal();
    });
    closeButton.addEventListener("click", () => {
        modal.close();
    });
});