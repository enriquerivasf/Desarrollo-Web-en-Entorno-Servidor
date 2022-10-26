document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("formulario")
        .addEventListener("submit", validarFormulario);
});

function validarFormulario(evento) {
    evento.preventDefault();

    let pass = document.getElementById("contrasena").value;
    let pass_repeat = document.getElementById("repetirContrasena").value;

    if (!(pass === pass_repeat)) {
        alert("Las contraseñas no son iguales");
    } else if (pass.length == 0) {
        alert("Escribe tu contraseña");
    } else {
        this.submit();
    }
}