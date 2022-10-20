(function () {

    const btnDelete = document.querySelectorAll(".btnDelete");

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Está seguro de borrar?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();