(function rankings() {

  // endpoints to get data from
  const tourist_url   = "/gdci-tourists";
  const expenses_url  = "/gdci-expenses";

  // bump charts to plot
  plotBump(tourist_url, "#tourismRankings", "Top 10 Number of Tourists Ranking");
  plotBump(expenses_url, "#expensesRankings", "Top 10 Tourism Expenses Ranking");

})()
