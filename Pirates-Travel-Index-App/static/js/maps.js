(function mapViz() {
  let cityMapcontainer = document.getElementById("cityMapStory");
  let cityMapurl = "https://public.tableau.com/views/VisitorsandExpensesScatter/StorySummary";

  let incomeContainer = document.getElementById("incomeMap");
  let incomeurl = "https://public.tableau.com/views/TourismandHappinessReportData/IncomeGroupbyCountry";

  let options = {
      hideTabs: true
  };

  new tableau.Viz(cityMapcontainer, cityMapurl, options);
  new tableau.Viz(incomeContainer, incomeurl, options);

})()