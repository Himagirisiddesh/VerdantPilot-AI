function predict() {
    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "⏳ Analyzing conditions...";

    const data = {
        N: parseFloat(document.getElementById("N").value),
        P: parseFloat(document.getElementById("P").value),
        K: parseFloat(document.getElementById("K").value),
        temp: parseFloat(document.getElementById("temp").value),
        humidity: parseFloat(document.getElementById("humidity").value),
        ph: parseFloat(document.getElementById("ph").value),
        rainfall: parseFloat(document.getElementById("rainfall").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        resultDiv.innerHTML = `🌾 ${data.result.toUpperCase()} is recommended`;
    })
    .catch(() => {
        resultDiv.innerHTML = "❌ Something went wrong!";
    });
}