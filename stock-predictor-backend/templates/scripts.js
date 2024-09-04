document.addEventListener("DOMContentLoaded", function() {
    console.log("Page is ready.");
});

// Function to fetch and display live stock data
async function fetchStockData(ticker) {
    try {
        // Fetch stock data from Flask backend
        const response = await fetch('/details', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({ ticker: ticker })
        });

        const data = await response.json();
        
        // Handle stock data
        updateChart(data);
        updateStockDetails(data);
    } catch (error) {
        console.error("Error fetching stock data:", error);
    }
}

function updateChart(data) {
    const labels = data.history.map(entry => new Date(entry.Date).toLocaleDateString());
    const prices = data.history.map(entry => entry.Close);

    const ctx = document.getElementById('stockChart').getContext('2d');
    const config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Stock Price',
                backgroundColor: 'rgba(52, 152, 219, 0.2)',
                borderColor: '#3498db',
                data: prices
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Stock Price Over Time'
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price (USD)'
                    }
                }
            }
        }
    };

    new Chart(ctx, config);
}

function updateStockDetails(data) {
    const detailsBody = document.getElementById('stock-details-body');
    const attributes = [
        { label: "Current Price", value: data.currentPrice },
        { label: "Previous Close", value: data.previousClose },
        { label: "Open", value: data.open },
        { label: "Day's Low", value: data.dayLow },
        { label: "Day's High", value: data.dayHigh },
        { label: "Volume", value: data.volume },
        { label: "Market Cap", value: data.marketCap },
        { label: "Beta", value: data.beta },
        { label: "PE Ratio", value: data.peRatio },
        { label: "EPS", value: data.eps },
        { label: "Earnings Date", value: data.earningsDate },
        { label: "Dividend Yield", value: data.dividendYield },
        { label: "Website", value: `<a href="${data.website}" target="_blank">${data.website}</a>` },
        { label: "Sector", value: data.sector },
        { label: "Industry", value: data.industry }
    ];

    detailsBody.innerHTML = attributes.map(attr => `
        <tr>
            <td>${attr.label}</td>
            <td>${attr.value}</td>
        </tr>
    `).join('');
}
