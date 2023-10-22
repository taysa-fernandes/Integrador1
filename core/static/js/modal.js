document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("myModal");
    const botaoDiarioAlimentar = document.getElementById("botao-diario-alimentar");
    const botaoFecharModal = document.getElementById("fecharModal");

    botaoDiarioAlimentar.addEventListener("click", function() {
        modal.showModal();
    });

    botaoFecharModal.addEventListener("click", function() {
        modal.close();
    });
});