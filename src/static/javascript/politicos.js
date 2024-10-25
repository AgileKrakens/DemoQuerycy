function ajustarTamanhoFonte() {
    const elementos = document.getElementsByClassName('name');
    
    for (let i = 0; i < elementos.length; i++) {
        const elemento = elementos[i];
        const comprimentoTexto = elemento.textContent.length;

        let tamanhoFonte = 18;
        const tamanhoMinimoFonte = 15;
        const tamanhoMaximoFonte = 18;

        if (comprimentoTexto > 15) {
            tamanhoFonte -= (comprimentoTexto - 15) * 0.5;
        }

        if (tamanhoFonte < tamanhoMinimoFonte) {
            tamanhoFonte = tamanhoMinimoFonte;
        } else if (tamanhoFonte > tamanhoMaximoFonte) {
            tamanhoFonte = tamanhoMaximoFonte;
        }

        elemento.style.fontSize = tamanhoFonte + 'px';
    }
}

window.addEventListener("resize", ajustarTamanhoFonte);
ajustarTamanhoFonte();
