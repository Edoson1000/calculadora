let display = document.getElementById("display");

function adicionarNumero(numero) {
    display.value += numero;
}

function adicionarOperador(operador) {
    display.value += operador;
}

function adicionarPonto() {
    if (!display.value.includes(".")) {
        display.value += ".";
    }
}

function limpar() {
    display.value = "";
}

function apagar() {
    display.value = display.value.slice(0, -1);
}

function calcular() {
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = "Erro";
    }
}
