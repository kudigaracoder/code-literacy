var img = [];
var xPos = yPos = 0;
var imgHeight = imgWidth = 250;
var imgPadding = 10;

function preload() {
    for (var i=1; i<=5; i++)
    {
        img[i] = loadImage("./images/image-"+i+".jpg");
    }
}
function setup() {
    createCanvas(windowWidth,windowHeight);
    noLoop();
}

function draw() {
    for (var i=1; i<=5; i++)
    {
        image(img[i], xPos, yPos, imgWidth, imgHeight);
        xPos = xPos + imgWidth + imgPadding;
    }

}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
