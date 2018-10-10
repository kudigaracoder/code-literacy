var img;
function preload() {
    img = loadImage('./images/image-5.jpg');
}
function setup() {
    createCanvas(windowWidth,windowHeight);
    image(img, 10,10,500,500);
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
