let canvas;
let myMap;
let tripsCoordinates;
let allCoordinates = [];
let data;

let delta = 0;
let coordinate = 0;

let origin;
let originVector;
let destination;
let destinationVector;

let taxiPosition;

let visitedRoutes = []; // A new array to hold all visited positions

const options = {
  lat: 40.73447,
  lng: -74.00232,
  zoom: 13,
  style: 'http://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png'
}
const mappa = new Mappa('Leaflet');

function preload() {
  data = loadJSON('./data/taxiday1.geojson');
}

function setup() {
  canvas = createCanvas(800, 700);
  myMap = mappa.tileMap(options);
  myMap.overlay(canvas);
  tripsCoordinates = myMap.geoJSON(data, "LineString");

  tripsCoordinates.forEach(function (trip) {
    trip.forEach(function (coordinate) {
        allCoordinates.push(coordinate)
      })
  });
  //myMap.onChange(drawPoints);

  // Every time the map is zoomed or moved update the route
  myMap.onChange(drawRoute);
}

function draw(){
  // clear() can be commented since drawRoute() will handle clearing the canvas
  // clear();

  if(delta < 1){
    delta += 0.2;
  } else {
    // Once it has arrived at its destination, add the origin as a visited location
    visitedRoutes.push(allCoordinates[coordinate])
    delta = 0;
    coordinate ++;
    // Call the drawRoute to update the route
    drawRoute();
  }

  origin = myMap.latLngToPixel(allCoordinates[coordinate][1], allCoordinates[coordinate][0]);
  originVector = createVector(origin.x, origin.y);
  destination = myMap.latLngToPixel(allCoordinates[coordinate + 1][1], allCoordinates[coordinate + 1][0]);
  destinationVector = createVector(destination.x, destination.y);

  taxiPosition = originVector.lerp(destinationVector, delta);

  // remove the stroke from the route
  noStroke();
  fill(255,255,0);
  ellipse(taxiPosition.x, taxiPosition.y, 7, 7);
}

function drawPoints(){
  clear()
  noStroke();
  fill(255);
  for(var i = 0; i < allCoordinates.length; i++){
    var pos = myMap.latLngToPixel(allCoordinates[i][1], allCoordinates[i][0])
    ellipse(pos.x, pos.y, 5, 5);
  }
}

// This functions draws a line with n-vertices where n = visited routes;
function drawRoute(){
  clear();
  // stroke color and width to see the route line
  stroke(255,0,0, 40);
  strokeWeight(5);
  if(visitedRoutes.length > 0){
    noFill();
    beginShape();
    visitedRoutes.forEach(function (e) {
        var pos = myMap.latLngToPixel(e[1], e[0]);
        vertex(pos.x, pos.y);
    })
    endShape()
  }
}
