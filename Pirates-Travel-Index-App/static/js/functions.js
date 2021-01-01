function getColor(city) {
  // returns color for each bump chart line
  // depending on city name to have it be fixed
  if (city == "Amsterdam") {
    return "#000000";
  } else if (city == "Antalya") {
    return "#A6C599";
  } else if (city == "Bangkok") {
    return "#E9CD4D";
  } else if (city == "Barcelona") {
    return "#E79C8B";
  } else if (city == "Dubai") {
    return "#5E497B";
  } else if (city == "Hong Kong") {
    return "#449390";
  } else if (city == "Istanbul") {
    return "#983F87";
  } else if (city == "Kuala Lumpur") {
    return "#769047";
  } else if (city == "London") {
    return "#B0230F";
  } else if (city == "Makkah") {
    return "#F6B97C";
  } else if (city == "Miami") {
    return "#D1D295";
  } else if (city == "New York") {
    return "#234E22";
  } else if (city == "Palma de Mallorca") {
    return "#BDEFD1";
  } else if (city == "Paris") {
    return "#283069";
  } else if (city == "Phuket") {
    return "#DF9BCE";
  } else if (city == "Seoul") {
    return "#F4E38D";
  } else if (city == "Shanghai") {
    return "#FF69B4";
  } else if (city == "Singapore") {
    return "#B15C27";
  } else if (city == "Taipei") {
    return "#C5B6E4";
  } else if (city == "Tokyo") {
    return "#A9CCDE";
  } else
  return "grey";
}

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
      // if (d.id === "circle"){
        // return String(d.Rank)
      // }
      // else {
        return d.City.concat("-").concat(d.Rank/2);
      // }
    })
    .x("Year")
    .y("Rank")
    .shape(function(d) {
      // if (d.id === "line") {
        return "Line";
      // }
      // else {
      //   return "Circle";
      // }
    })
    .shapeConfig({
      Line: {
        strokeWidth: 5,
        stroke: function(d) {
          return getColor(d.City);
        }
      },
      // Circle: {
      //   r: 17,
      //   fill: function(d) {
      //     return getColor(d.City);
      //   }
      // },
      labelConfig: {
        fontMin: 11,
        fontColor: "white"
      }
    })
  ;

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
      // tickSize: 35,
      // ticks: []
    })
    // .y2Config({
    //   tickSize: 35,
    //   ticks: []
    // })
    .title(title)
    .titleConfig({
      fontSize: 20
    })
    .legendPosition("top")
    .legendConfig({
      padding: 15
    })
    .render()
  ;

}

