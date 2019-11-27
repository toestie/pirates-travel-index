async function getData(input_url) {

  // Use `d3.json` to fetch the metadata for a sample
  let data = await d3.json(input_url);

  let year_2011 = []
  let year_2012 = [];
  let year_2013 = [];
  let year_2014 = [];
  let year_2015 = [];
  let year_2016 = [];
  let year_2017 = [];
  let year_2018 = [];

  data.forEach(function(d, i) {
    if (d.Year == 2011) {
      year_2011.push(d)
    } else if (d.Year == 2012) {
      year_2012.push(d)
    } else if (d.Year == 2013) {
      year_2013.push(d)
    } else if (d.Year == 2014) {
      year_2014.push(d)
    } else if (d.Year == 2015) {
      year_2015.push(d)
    } else if (d.Year == 2016) {
      year_2016.push(d)
    } else if (d.Year == 2017) {
      year_2017.push(d)
    } else if (d.Year == 2018) {
      year_2018.push(d)
    }
  });

  console.log(year_2018)
  
}


(function init() {

  const tourist_url = "/gdci-tourists";
  const expenses_url = "/gdci-expenses";
  const ratio_url = "/tourism-ratio";
  getData(tourist_url);
  getData(expenses_url);
  getData(ratio_url);
  
  // Use the first sample from the list to build the initial plots
  // const firstSample = sampleNames[0];
  // buildCharts(firstSample);
  // buildMetadata(firstSample);

})()
