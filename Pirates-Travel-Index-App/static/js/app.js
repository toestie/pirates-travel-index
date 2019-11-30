async function plotBump(url, html_id, title){
  let data = await d3.json(url);

  // build the chart
  let chart = new d3plus.BumpChart()
    .data(data)
    .select(html_id)
    .groupBy("City")
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

  // format the chart
  chart
    .xConfig({
      title: "Years",
      tickSize: 15
    })
    .yConfig({
      title: "Ranking",
      tickSize: 35,
      ticks: []
    })
    .y2Config({
      tickSize: 35,
      ticks: []
    })
    .shapeConfig({
      Line: {
        strokeWidth: 5
      },
      Circle: {
        r: 17,
      },
      labelConfig: {
        fontMin: 11
      }
    })
    .title(title)
    .titleConfig({
      fontSize: 20
    })
    .legendPosition("top")
    .render()
  ;

}

(function init() {

  const tourist_url   = "/gdci-tourists";
  const expenses_url  = "/gdci-expenses";
  const ratio_url     = "/tourism-ratio";

  plotBump(tourist_url, "#viz1", "Top Number of Tourists Ranking");
  plotBump(expenses_url, "#viz2", "Top Number of Tourist Expenses Ranking");
  // plotBump(ratio_url, "#viz3", "Tourism Density Ranking");
  // let data = await d3.json(tourist_url);
  
  // let chart = new d3plus.BumpChart()
  //   .data(data)
  //   .select("#viz1")
  //   .groupBy("City")
  //   .label(function(d) {
  //     if (d.id == "circle"){
  //       return String(d.Rank)
  //     }
  //     else {
  //       return d.City;
  //     }
  //   })
  //   .x("Year")
  //   .y("Rank")
  //   .shape(function(d) {
  //     if (d.id === "line") {
  //       return "Line";
  //     }
  //     else {
  //       return "Circle";
  //     }
  //   });

  // chart
  //   .xConfig({
  //     title: "Years",
  //     tickSize: 15
  //   })
  //   .yConfig({
  //     title: "Ranking",
  //     tickSize: 35,
  //     ticks: []
  //   })
  //   .y2Config({
  //     tickSize: 35,
  //     ticks: []
  //   })
  //   .shapeConfig({
  //     Line: {
  //       strokeWidth: 5
  //     },
  //     Circle: {
  //       r: 17,
  //     },
  //     labelConfig: {
  //       fontMin: 11
  //     }
  //   })
  //   .title("Top Number of Tourists Ranking")
  //   .titleConfig({
  //     fontSize: 20
  //   })
  //   .legendPosition("top")
  //   .render()
  // ;


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
