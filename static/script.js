document.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch("http://localhost:8000/vista-equipos/");
        const equipos = await response.json();
        const tableBody = document.querySelector("#tabla-equipos tbody");

        // Insertar los datos en la tabla
        equipos.forEach(equipo => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${equipo.NombreEquipo}</td>
                <td>${equipo.Puntos}</td>
                <td>${equipo.PartidosJugados}</td>
                <td>${equipo.PartidosGanados}</td>
                <td>${equipo.PartidosEmpatados}</td>
                <td>${equipo.PartidosPerdidos}</td>
                <td>${equipo.GolesAFavor}</td>
                <td>${equipo.GolesEnContra}</td>
                <td>${equipo.DiferenciaDeGoles}</td>
            `;
            tableBody.appendChild(row);
        });

        // Actualizar los bloques de estadísticas
        document.getElementById("equipos-registrados").textContent = equipos.length;
        document.getElementById("partidos-jugados").textContent = equipos.reduce((acc, equipo) => acc + equipo.PartidosJugados, 0);
        document.getElementById("goles-totales").textContent = equipos.reduce((acc, equipo) => acc + equipo.GolesAFavor, 0);

        const totalGoles = equipos.reduce((acc, equipo) => acc + equipo.GolesAFavor, 0);
        const totalPartidos = equipos.reduce((acc, equipo) => acc + equipo.PartidosJugados, 0);
        const promedioGoles = (totalGoles / totalPartidos).toFixed(2);
        document.getElementById("promedio-goles").textContent = promedioGoles;

    } catch (error) {
        console.error("Error al cargar los datos:", error);
    }
});
