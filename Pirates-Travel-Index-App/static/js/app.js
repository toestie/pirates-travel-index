(async function init() {

  const tourist_url = "/gdci-tourists";
  const expenses_url = "/gdci-expenses";
  const ratio_url = "/tourism-ratio";

  let data = await d3.json(tourist_url);
  console.table(data);
  
  let chart = new d3plus.BumpChart()
    .data(data)
    .select("#viz1")
    .groupBy("City")
    // .label(d => d.City)
    .label(function(d) {
      if (d.id == "circle"){
        return String(d.Rank)
      }
      else {
          return d.City;
      }
    })
    .x("Year")
    .y("Rank")
    .shape(function(d) {
      if (d.id === "line") {
        return "Line";
      }
      else {
        return "Circle";
      }
    });

  chart
    .xConfig({
      title: "Years"
    })
    .yConfig({
      title: "Ranking",
      ticks: []
    })
    .y2Config({
      ticks: []
    })
    .shapeConfig({
      Line: {
        strokeWidth: 5
      }
    })
    .sizeMin(20)
    .title("Top Number of Tourists Ranking")
    .render()
  ;


    // let expenses_data = await d3.json(expenses_url);
    // console.table(expenses_data);
    
    // new d3plus.BumpChart()
    //   .data(expenses_data)
    //   .select("#viz2")
    //   .groupBy("City")
    //   .label(function(d) {
    //       return d.City;
    //     })
    //   .x("Year")
    //   .y("Rank")
    //   .xConfig({
    //     title: "Years"
    //   })
    //   .yConfig({
    //     title: "Ranking"
    //   })
    //   .title("Top Expenses Ranking")
    //   .render();

    // let ratio_data = await d3.json(ratio_url);
    // console.table(ratio_data);
    
    // new d3plus.BumpChart()
    //   .data(ratio_data)
    //   .select("#viz3")
    //   .groupBy("City")
    //   .label(function(d) {
    //       return d.City.toString();
    //     })
    //   .x("Year")
    //   .y("Rank")
    //   .xConfig({
    //     title: "Years"
    //   })
    //   .yConfig({
    //     title: "Ranking"
    //   })
    //   .title("Tourism Density Ranking")
    //   .render();

})()
