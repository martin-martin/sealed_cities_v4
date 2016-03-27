////
//// PART 1 - BUILDING THE MAP
////

// importing the geoJSON file for drawing the map
// Resource: http://grokbase.com/t/gg/d3-js/1372gq18j9/geojson-maps - Thanks :)
d3.json("map/region_un_Europe_subunits.json", function(geo_data) {
  "use strict";
  var margin = 75,
      width = 1920 - margin,
      height = 1080 - margin;

  var svg = d3.select('body')
      .append('svg')
      .attr('width', width + margin)
      .attr('height', height + margin)
      .append('g')
      .attr('class', 'map');

  var projection = d3.geo.mercator()
        .scale(700)
        .translate([width / 2 - 600, height + 250]);

  var path = d3.geo.path().projection(projection);

  var map = svg.selectAll('path')
        .data(geo_data.features)
        .enter()
        .append('path')
        .attr('d', path)
        .attr('id', function(d) {
          return d.properties.brk_a3;
        })
        .attr('class', function(d) {
          var country_id = d.properties.brk_a3;
          if (country_id == "SCT" || country_id == "ENG" || country_id == "WLS" || country_id == "NIR") {
            return "UK";
          } else {
            return "entity";
          };
        })
        .on("mouseover", mapMouseOver)
        .on("mouseout", mapMouseOut)
        .on("click", showDetails)
        .style('fill', 'gray')
        .style("stroke", "white");

  function mapMouseOver(d) {
    // highlights the country on mouseover
    var country_id = d.properties.brk_a3;
    console.log(country_id, "is", d.properties.name)
    // in this map, the U.K. is represented in the different countries
    // however my dataset has data for "United Kingdom".
    // therefore I assigned a class "UK" to the countries and here I
    // am chaining them to color at the same time.
    var country = d3.selectAll($("#" + country_id));
    if (country.attr('class') == 'UK') {
      var selected = d3.selectAll('.UK');
    } else {
      var selected = country;
    }
    selected
        .style("fill", "red")
        .style("stroke", "white");
  };

  function mapMouseOut(d) {
    // returns the country to it's original state
    // when the cursor leaves the area
    var country_id = d.properties.brk_a3;
    var country = d3.selectAll($("#" + country_id));
    if (country.attr('class') == 'UK') {
      var selected = d3.selectAll('.UK');
    } else {
      var selected = country;
    }
    selected
        .style("fill", "gray")
        .style("stroke", "white");
  };

  ////
  ////
  //// SECOND PART OF THE ANIMATION, DATA-DRIVEN
  ////
  ////

  // nesting the data import into the showDetails function (which is where I'll use it)
  function showDetails(d) {
    console.log("you just clicked!");
    console.log(d.properties.brk_a3);


debugger;


  // importing the csv file
  d3.json('soil_sealing_cities.json', function(error, data) {
    ////
    //// PART 2 - DATA CLEANING
    ////
    // perform the data wrangling for each row
    data.forEach(function(d) {
      d.country = d.country;
      // transform string to integer
      d.cat_below_25_percent = +d.cat_below_25_percent;
      d.cat_25_to_49_percent = +d.cat_25_to_49_percent;
      d.cat_50_to_74_percent = +d.cat_50_to_74_percent;
      d.cat_75_and_above_percent = +d.cat_75_and_above_percent;
      d.sum_of_cities = +d.sum_of_cities;
      d.percentage_cities_50_and_above_percent = +d.percentage_cities_50_and_above_percent;
      });

debugger;

    d3.select('#country-info')
      .selectAll('p')
      .data(d)
      .enter()
      .append('p')
      .style('fill', 'green')
      .text(d.properties.brk_a3);








    ////
    //// PART 3 - DRAWING HOUSES AND TREES
    ////
    d3.select('body').append('span').attr('class', 'example');

    // modify the initial data
    data.forEach(function(d){
            // calling the function to generate the range for each row entry
            d.num_blocks = d3.range(0,d.total_sealed_in_percent,1);
            d.num_squares = d3.range(0,100 - d.total_sealed_in_percent,1);
    })

    // insert a div for each row
    var rows = d3.select('.example').selectAll('div')
        .data(data, function(d, i) {
            // binding a key to each row. It is not really necessary on this example
            // but I will leave it here to make the use of key functions clear
            return "row_" + i;
        })
        .enter()
        .append('div');

    // insert imgs with class block in each row
    var blocks = rows.selectAll('.block')
            .data(function (d){
                return d.num_blocks
            })
            .enter()
            .append('img')
                .attr('class', 'block')
                .attr('src', 'img/little_house2.png')
                .attr('alt', 'example block')
                .style('width', '40px')
                .style('height', '40px')

    // insert imgs with class squares in each row
    var squares = rows.selectAll('.square')
            .data(function (d){
                return d.num_squares
            })
            .enter()
            .append('img')
                .attr('class', 'square')
                .attr('src', 'img/tree.svg')
                .attr('alt', 'example square')
                .style('width', '40px')
                .style('height', '40px');

  // HERE THE PART OF THE JSON DATA ENDS
  });



  };
  // when i click I get d as the element holding the country's data.
  // however I will need the corresponding data from the OTHER data file
  // - so I need to link it into here


//// AND HERE IT ALL ENDS
});




