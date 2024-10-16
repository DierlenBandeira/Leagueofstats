document.getElementById("upButton").addEventListener("click", function() {
    // Adiciona a classe de animação ao botão de seta para movê-lo para cima
    this.classList.add("animate-up");

    // Espera a animação do botão de seta terminar para mostrar a descrição e o botão "Iniciar"
    setTimeout(function() {
        const descriptionElement = document.getElementById("description");
        const startButton = document.getElementById("startButton");

        // Exibe a descrição alterando diretamente a opacidade
        descriptionElement.style.opacity = "1";
        
        // Exibe o botão Iniciar alterando diretamente a opacidade
        startButton.style.opacity = "1";

    }, 1000); // Tempo para a animação do botão de seta terminar
});

document.getElementById("startButton").addEventListener("click", function() {
    // Redireciona para a rota /register
    window.location.href = "/login";
});

document.getElementById("registerButton").addEventListener("click", function() {
    window.location.href = "/login";
    document.addEventListener("DOMContentLoaded", function () {
        // Animação para o botão de registro
        var registerButton = document.getElementById("registerButton");
        if (registerButton) {
            registerButton.addEventListener("click", function (event) {
                event.preventDefault(); // Impede o envio do formulário imediatamente
                var button = this;
                button.classList.add("loading");

                // Simula um tempo de carregamento antes de continuar
                setTimeout(function () {
                    button.form.submit(); // Submete o formulário após o "loading"
                }, 2000); // 2 segundos de "loading"
            });
        }
    });
});

