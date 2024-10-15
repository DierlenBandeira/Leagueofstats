document.getElementById("upButton").addEventListener("click", function() {
    // Adiciona a classe de animação ao botão de seta para movê-lo para cima
    this.classList.add("animate-up");

    // Espera a animação do botão de seta terminar para mostrar a descrição e o botão "Iniciar"
    setTimeout(function() {
        const descriptionElement = document.getElementById("description");
        const startButton = document.getElementById("startButton");
        const backgroundElement = document.querySelector('.background'); // Seleciona o fundo

        
        // Exibe a descrição alterando diretamente a opacidade
        descriptionElement.style.opacity = "1";
        
        // Exibe o botão Iniciar alterando diretamente a opacidade
        startButton.style.opacity = "1";

        // Diminuir o brilho do fundo da tela
        backgroundElement.style.filter = "brightness(0.2)";

    }, 1000); // Tempo para a animação do botão de seta terminar
});
