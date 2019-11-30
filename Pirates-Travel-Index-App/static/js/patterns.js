(function patternsViz() {
  let popularPatternscontainer = document.getElementById("popularPatterns");
  let popularPatternsurl = "http://public.tableau.com/views/example_15743012921570/StoryMostpopulartouristcitiesyearoveryear";

  let happinessContainer = document.getElementById("happiness");
  let happinessurl = "http://public.tableau.com/views/HappinessFactors/HappinessFactors";

  let options = {
      hideTabs: true
  };

  new tableau.Viz(popularPatternscontainer, popularPatternsurl, options);
  new tableau.Viz(happinessContainer, happinessurl, options);

})()