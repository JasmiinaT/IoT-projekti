document.addEventListener("DOMContentLoaded", function () {
  google.charts.load("current", { packages: ["corechart", "gauge"] });
  google.charts.setOnLoadCallback(drawChart);
  google.charts.setOnLoadCallback(drawInitialGauges);

  function drawInitialGauges() {
    drawGauges(0, 0);
    drawChart(); // calling read api data
  }

  function drawChart() {
    fetch(
      "https://api.thingspeak.com/channels/2713341/feeds.json?api_key=KDMM5EO6LEIEJXGH&results=2"
    )
      .then((response) => response.json())
      .then((APIdata) => {
        const feeds = APIdata.feeds;
        const data = [["Time", "Temperature", "Reference temperature"]];
        let latestTemperature = null;
        let latestReference = null;

        feeds.forEach((feed) => {
          const time = new Date(feed.created_at);
          const temperature = parseFloat(feed.field1);
          const referenceTemperature = parseFloat(feed.field2);
          data.push([time, temperature, referenceTemperature]);

          latestTemperature = temperature;
          latestReference = referenceTemperature;
        });

        const dataTable = google.visualization.arrayToDataTable(data);
        const options = {
          title: "Temperature Data Comparison",
          hAxis: { title: "Time", format: "HH:mm" },
          vAxis: { title: "Temperature" },
          legend: { position: "bottom" },
          colors: ["#1b9e77", "#d95f02"],
          width: 900,
          height: 500,
        };
        const chart = new google.visualization.LineChart(
          document.getElementById("curve_chart")
        );
        chart.draw(dataTable, options);
        if (latestHandmade !== null && latestReference !== null) {
          drawGauges(latestHandmade, latestReference);
        }
      })
      .catch((error) => console.error("Error fetching data:", error));
  }

  function drawGauges(temperatureValue, referenceValue) {
    // Data for temperature sensor gauge
    const temperatureData = google.visualization.arrayToDataTable([
      ["Label", "Value"],
      ["", temperatureValue],
    ]);

    const temperatureOptions = {
      width: 600,
      height: 300,
      redFrom: 40,
      redTo: 50,
      yellowFrom: 30,
      yellowTo: 50,
      minorTicks: 5,
      max: 50, // Set this according to your sensor range
    };

    const temperatureChart = new google.visualization.Gauge(
      document.getElementById("temperature_gauge")
    );
    temperatureChart.draw(temperatureData, temperatureOptions);

    // Data for reference sensor gauge
    const referenceData = google.visualization.arrayToDataTable([
      ["Label", "Value"],
      ["", referenceValue],
    ]);

    const referenceOptions = {
      width: 600,
      height: 300,
      redFrom: 40,
      redTo: 50,
      yellowFrom: 30,
      yellowTo: 50,
      minorTicks: 5,
      max: 50, // Set this according to your sensor range
    };

    const referenceChart = new google.visualization.Gauge(
      document.getElementById("reference_gauge")
    );
    referenceChart.draw(referenceData, referenceOptions);
  }
});
