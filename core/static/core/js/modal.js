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
    const openModal2 = document.getElementById("abrirModal2");
    const modal2 = document.getElementById("myModal2");
    const closeButton2 = document.getElementById("fecharModal2")
    openModal2.addEventListener("click", () => {
        modal2.showModal();
    });
    closeButton2.addEventListener("click", () => {
        modal2.close();
    });
});