(function density_ranking() {

  // endpoint to get data from
  const ratio_url = "/tourism-ratio";

  // bump chart to plot
  plotBump(ratio_url, "#densityRankings", "Tourism Density Ranking");

  // Tableau chart
  let tableauContainer = document.getElementById("tableauDensity");
  let tableauurl = "https://public.tableau.com/views/PiratesTravelIndex-Density/DetailedTourismDensity";

  let options = {
      hideTabs: true
  };

  new tableau.Viz(tableauContainer, tableauurl, options);

})()
