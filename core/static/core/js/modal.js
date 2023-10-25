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