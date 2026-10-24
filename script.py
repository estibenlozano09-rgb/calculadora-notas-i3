
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Notas Instituto i3</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f2f2f2;
        }

        form {
            background-color: white;
            padding: 20px;
            max-width: 350px;
            border-radius: 10px;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            box-sizing: border-box;
        }

        button {
            padding: 10px 20px;
            background-color: #1976d2;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>

</head>
<body>

    <h1>Calculadora de Notas Instituto i3</h1>

    <form id="formulario">
        <label for="nombre">Nombre del estudiante:</label>
        <input type="text" id="nombre" required>
        <br><br>

        <label for="nota1">Primera nota:</label>
        <input type="number" id="nota1" min="0" max="5" step="0.1" required>
        <br><br>

        <label for="nota2">Segunda nota:</label>
        <input type="number" id="nota2" min="0" max="5" step="0.1" required>
        <br><br>

        <label for="nota3">Tercera nota:</label>
        <input type="number" id="nota3" min="0" max="5" step="0.1" required>
        <br><br>

        <button type="submit">Calcular</button>
    </form>

    <h2 id="resultado"></h2>

    <script>
        document.getElementById("formulario").addEventListener("submit", function(event) {
            event.preventDefault();

            let nombre = document.getElementById("nombre").value;
            let nota1 = Number(document.getElementById("nota1").value);
            let nota2 = Number(document.getElementById("nota2").value);
            let nota3 = Number(document.getElementById("nota3").value);

            let promedio = (nota1 + nota2 + nota3) / 3;
            let estado = promedio >= 3.0 ? "Aprobado" : "Reprobado";

            document.getElementById("resultado").textContent =
                "Estudiante: " + nombre +
                " | Promedio: " + promedio.toFixed(2) +
                " | Estado: " + estado;
        });
    </script>

</body>
</html>
