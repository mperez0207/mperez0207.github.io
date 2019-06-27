var tbody = d3.select("tbody");

function populate_table()
{
    d3.csv("/final_dataset.csv", function(data) {
        data.forEach(function(row) {
            tbody.append("tr").attr("class", "data_row");
            Object.entries(row).forEach(function(datum) {
                 tbody.append("td").text(datum[1]);
            });
        });
    });
}

function results_bar_graph()
{
    d3.csv("/Prediction Results.csv", function(data) {

        var precision = {
            x: [],
            y: [],
            text: [],
            name: "",
            type: "bar"
        };

        var recall = {
            x: [],
            y: [],
            text: [],
            name: "",
            type: "bar"
        };

        data.forEach(function(row) {
            var rent_category = row["Rent Category"];

            precision["x"].push(rent_category);
            recall["x"].push(rent_category);

            precision["y"].push(row["precision"]);
            recall["y"].push(row["recall"]);

            precision["name"] = "Precision"
            recall["name"] = "Recall"

            var support = row["support"];

            var hover_text = support + " neighborhoods were " + rent_category;
            precision["text"].push(hover_text);
            recall["text"].push(hover_text);
        });

        var data = [precision, recall];
            
        var layout = {
            barmode: 'group',
            title: {
                text:'Precision and Recall For Each Rent Category',
                font: {
                  family: 'Courier New, monospace',
                  size: 24
                },
                xref: 'paper',
                x: 0.05,
              },
              xaxis: {
                title: {
                  text: 'Rent Category',
                  font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                  }
                },
              },
              yaxis: {
                title: {
                  text: 'Percentage',
                  font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                  }
                }
              }
        };
    
        Plotly.newPlot('results_graph', data, layout);
    });
}

// When webpage is first loaded, populate the table and display the results bar graph
populate_table();
results_bar_graph();