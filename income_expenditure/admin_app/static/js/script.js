
// function showToast(message, type = 'success') {
//     const toast = document.createElement('div');
//     toast.className = `toast toast-${type}`;
//     toast.textContent = message;
//     document.body.appendChild(toast);

//     setTimeout(() => {
//         toast.classList.add('fade-out');
//         setTimeout(() => toast.remove(), 500);
//     }, 2000);
// }

// document.getElementById('export-csv').addEventListener('click', () => {
//     showToast('CSV Export Coming Soon!', 'info');
// });

// document.getElementById('print-page').addEventListener('click', () => {
//     window.print();
// });

// function addRow(tableId) {
//     const table = document.getElementById(tableId).getElementsByTagName('tbody')[0];
//     const newRow = table.insertRow();
//     for (let i = 0; i < 3; i++) {
//         const cell = newRow.insertCell(i);
//         cell.contentEditable = "true";
//         cell.innerText = "New Entry";
//         cell.className = "px-6 py-4";
//     }
//     showToast('New row added successfully!', 'success');
// }

// document.getElementById('add-income-row').addEventListener('click', () => addRow('income-table'));
// document.getElementById('add-expense-row').addEventListener('click', () => addRow('expense-table'));

// document.addEventListener("DOMContentLoaded", function () {
//     const incomeData = [20000, 30000, 40000, 35000, 50000, 45000];
//     const expenseData = [10000, 15000, 20000, 18000, 22000, 25000];
//     const profit = parseInt(document.getElementById('total-profit').innerText);
//     const totalIncome = parseInt(document.getElementById('total-income').innerText);
//     const totalExpense = parseInt(document.getElementById('total-expenditure').innerText);

//     const ctx1 = document.getElementById("income-expense-chart").getContext("2d");
//     new Chart(ctx1, {
//         type: "bar",
//         data: {
//             labels: ["Income", "Expenditure", "Profit"],
//             datasets: [{
//                 label: "Amount",
//                 data: [totalIncome, totalExpense, profit],
//                 backgroundColor: [
//                     "#86ef7d",
//                     "#fca5a5",
//                     "#6ee7b7"
//                 ],
//                 borderColor: [
//                     "#86ef7d",
//                     "#fca5a5",
//                     "#6ee7b7"
//                 ],
//                 borderWidth: 1
//             }]
//         },
//         options: {
//             responsive: true,
//             plugins: {
//                 title: {
//                     display: false,
//                     text: 'Income vs Expenses',
//                     font: {
//                         size: 18
//                     }
//                 },
//                 legend: {
//                     position: 'bottom'
//                 }
//             },
//             scales: {
//                 y: {
//                     beginAtZero: true,
//                     ticks: {
//                         callback: function (value) {
//                             return 'Rs ' + value;
//                         }
//                     }
//                 }
//             }
//         }
//     });

//     const ctx2 = document.getElementById("tracking-chart").getContext("2d");
//     new Chart(ctx2, {
//         type: "line",
//         data: {
//             labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
//             datasets: [{
//                 label: "Income",
//                 data: incomeData,
//                 borderColor: "#38bdf8",
//                 backgroundColor: "rgba(56, 189, 248, 0.2)",
//                 fill: true,
//                 borderWidth: 2,
//                 pointRadius: 5,
//                 pointBackgroundColor: "#38bdf8",
//                 pointBorderColor: "#fff",
//                 pointHoverRadius: 7,
//                 pointHoverBackgroundColor: "#38bdf8",
//                 pointHoverBorderColor: "#fff",
//             }, {
//                 label: "Expenditure",
//                 data: expenseData,
//                 borderColor: "#f87171",
//                 backgroundColor: "rgba(248, 113, 113, 0.2)",
//                 fill: true,
//                 borderWidth: 2,
//                 pointRadius: 5,
//                 pointBackgroundColor: "#f87171",
//                 pointBorderColor: "#fff",
//                 pointHoverRadius: 7,
//                 pointHoverBackgroundColor: "#f87171",
//                 pointHoverBorderColor: "#fff",
//             }]
//         },
//         options: {
//             responsive: true,
//             plugins: {
//                 title: {
//                     display: false,
//                     text: 'Monthly Tracking',
//                     font: {
//                         size: 18
//                     }
//                 },
//                 legend: {
//                     position: 'bottom'
//                 }
//             },
//             scales: {
//                 x: {
//                     grid: {
//                         display: false
//                     }
//                 },
//                 y: {
//                     beginAtZero: true,
//                     ticks: {
//                         callback: function (value) {
//                             return 'Rs ' + value;
//                         }
//                     },
//                     grid: {
//                         color: "rgba(0, 0, 0, 0.1)"
//                     }
//                 }
//             },
//             elements: {
//                 line: {
//                     tension: 0.4
//                 }
//             }
//         }
//     });
// });