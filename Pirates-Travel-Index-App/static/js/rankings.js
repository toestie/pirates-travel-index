async function plotBump(url, html_id, title){
  // url: Flask endpoint to get data from
  // html_id: HTML element to put chart in (tagged by id attribute)
  // title: title for the chart

  let data = await d3.json(url);

  //////////////////////////////////
  // build the bump chart
  /////////////////////////////////
  
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

  //////////////////////////////////
  // format the bump chart
  //////////////////////////////////

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

(function rankings() {

  // endpoints to get data from
  const tourist_url   = "/gdci-tourists";
  const expenses_url  = "/gdci-expenses";
  const ratio_url     = "/tourism-ratio";

  // bump charts to plot
  plotBump(tourist_url, "#tourismRankings", "Top Number of Tourists Ranking");
  plotBump(expenses_url, "#expensesRankings", "Top Number of Tourist Expenses Ranking");
  // plotBump(ratio_url, "#viz3", "Tourism Density Ranking");

})()
