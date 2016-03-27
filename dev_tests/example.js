d3.json("map/region_un_Europe_subunits.json", function(geo_data) {
  "use strict";

  var svg = d3.select('body')
      .append('svg')
      .append('g')
      .attr('class', 'map');

  var projection = d3.geo.mercator();

  var path = d3.geo.path().projection(projection);

  var map = svg.selectAll('path')
        .data(geo_data.features)
        .enter()
        .append('path')
        .on("click", showDetails)

  ////
  ////
  //// SECOND PART OF THE ANIMATION, DATA-DRIVEN
  ////
  ////

  // nesting the data import into the showDetails function (which is where I'll use it)
  function showDetails(d) {

      // importing the json file
      d3.json('soil_sealing_cities.json', function(error, data) {

        data.forEach(function(d) {
            // some munging happens here
          });

        data.forEach(function(c) {
          if (c.country == d.properties.name) {

            // adding the images
            var country_vis =  d3.select('.modal-content').select('div');
            country_vis
              .data( function(c) {
                 return c.num_blocks
               })
              .enter()
              .append('img')
                  .attr('src', 'img/little_house2.png');
          }
        });
      };
  };

});



//////////////////////////anotherexample//////////////////////////


var data = [
    {'amount' : 80},
    {'amount' : 10},
    {'amount' : 20}
];

d3.select('body').append('span').attr('class', 'example');

d3.select('.example').selectAll('.block')
    .data(data, function(d) {
        // calling the function to generate the range for each row entry
        d.num_blocks = range(d.amount);
        d.num_squares = range(100 - d.amount)
        // debugger;
        return d.num_blocks, d.num_squares;
    })
    .enter()
    .append('span')
        // add nested data
        .selectAll('img')
        .data(function (d){return d.num_blocks})
        .enter()
        .append('img')
            .attr('class', 'block')
            .attr('src', 'img/block.png')
            .attr('alt', 'example block')
            .style('width', '40px')
            .style('height', '40px')
        .data(function (d){return d.num_squares})
        .enter()
        .append('img')
            .attr('class', 'square')
            .attr('src', 'img/square.png')
            .attr('alt', 'example square')
            .style('width', '40px')
            .style('height', '40px');