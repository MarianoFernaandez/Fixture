document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("http://localhost:8000/vista-equipos/"); // Cambia la URL según tu backend
    const equipos = await response.json();
    const tableBody = document.querySelector("#tabla-equipos tbody");

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
});
