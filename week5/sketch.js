var img = [];
var xPos = yPos = 0;
var imgHeight = imgWidth = 250;
var imgPadding = 10;

var cv;

function preload() {
    for (var i=1; i<=5; i++)
    {
        img[i] = loadImage("./images/image-"+i+".jpg");
    }
}

function centerCanvas() {
    var canvasWidth = (windowWidth - width) / 2;
    var canvasHeight = (windowHeight - height) / 2;
    cv.position(canvasWidth, canvasHeight);
}

function setup() {
    cv = createCanvas(1290,500);
    centerCanvas();
    noLoop();
}

function draw() {
    for (var i=1; i<=5; i++)
    {
        image(img[i], xPos, yPos, imgWidth, imgHeight);
        xPos = xPos + imgWidth + imgPadding;
    }
}

function mousePressed() {
    for (var i=1; i<=5; i++)
    {
        EXIF.getData(img[i], function() {
            var allMetaData = EXIF.getAllTags(this);
            console.log(allMetaData);
        });
    }
}

function windowResized() {
  centerCanvas();
}
