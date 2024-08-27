// Cargar el archivo JSON y generar gráficos
fetch("dataset/cleaned_data.json")
  .then((response) => response.json())
  .then((data) => {
    const categories = [
      "Acts intended to induce fear or emotional distress",
      "Acts intended to induce fear or emotional distress: Cyber-related",
      "Intimate partner or family member",
      "Kidnapping",
      "Other Perpetrator known to the victim",
      "Perpetrator unknown to the victim",
      "Relationship to perpetrator is not known",
      "Serious assault",
      "Sexual Exploitation",
      "Sexual violence",
      "Sexual violence: Other acts of sexual violence",
      "Sexual violence: Rape",
      "Sexual violence: Sexual assault",
    ];
    const values = categories.map((category) => {
      return data.filter((row) => row[`Category_${category}`] === true).length;
    });

    const yearCounts = data.reduce((acc, row) => {
      if (row.Year in acc) {
        acc[row.Year]++;
      } else {
        acc[row.Year] = 1;
      }
      return acc;
    }, {});

    const years = Object.keys(yearCounts);
    const valuesPerYear = Object.values(yearCounts);

    const ctxBar = document.getElementById("barChart").getContext("2d");
    new Chart(ctxBar, {
      type: "bar",
      data: {
        labels: categories,
        datasets: [
          {
            label: "# of Cases",
            data: values,
            borderWidth: 2.5,
          },
        ],
      },
    });

    const ctxPie = document.getElementById("pieChart").getContext("2d");
    new Chart(ctxPie, {
      type: "pie",
      data: {
        labels: categories,
        datasets: [
          {
            label: "# of Cases",
            data: values,

            borderWidth: 2.5,
          },
        ],
      },
    });

    const ctxLine = document.getElementById("lineChart").getContext("2d");
    new Chart(ctxLine, {
      type: "line",
      data: {
        labels: years,
        datasets: [
          {
            label: "Cases per year",
            data: valuesPerYear,
            borderWidth: 2.5,
            pointOverBorderWidth: 2,
            pointStyle: "triangle",
          },
        ],
      },
      options: {},
    });
  });
