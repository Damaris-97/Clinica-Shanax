document.addEventListener('DOMContentLoaded', function() {
    var ctx1 = document.getElementById('myChart1').getContext('2d');
    var labels1 = JSON.parse(document.getElementById('labels1').textContent);
    var values1 = JSON.parse(document.getElementById('values1').textContent);

    var ctx2 = document.getElementById('myChart2').getContext('2d');
    var labels2 = JSON.parse(document.getElementById('labels2').textContent);
    var values2 = JSON.parse(document.getElementById('values2').textContent);

    var backgroundColors = [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(75, 192, 192, 0.2)'
    ];
    var borderColors = [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(75, 192, 192, 1)'
    ];

    // Chart 1
    var myChart1 = new Chart(ctx1, {
        type: 'pie',
        data: {
            labels: labels1,
            datasets: [{
                label: 'Cantidad de Pacientes por Tipo de Grupo',
                data: values1,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    enabled: true,
                }
            }
        }
    });

    // Chart 2
    var myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: labels2,
            datasets: [{
                label: 'Cantidad de Pacientes por Género',
                data: values2,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    enabled: true,
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
