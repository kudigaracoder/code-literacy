var capture;
var w = 800,
    h = 600;

function setup() {
    capture = createCapture(VIDEO);
    createCanvas(w, h);
    capture.size(w, h);
    capture.hide();

}

var targetColor = [255,255,255];

function draw() {
//    rect(20,20,50,50);
//    fill(255,0,0);

    capture.loadPixels();
    var sampling = false;
    var screenWidth = capture.width,
        screenHeight = capture.height;
    if (capture.pixels.length > 0) {
        if (mouseIsPressed &&
            mouseX > 0 && mouseX < width &&
            mouseY > 0 && mouseY < height) {
            targetColor = capture.get(mouseX, mouseY);
            background(targetColor);
            sampling = true;
        }
        var pixels = capture.pixels;
        if (!sampling) {
            capture.updatePixels();
        }
        image(capture, 0, 0, w, h);
    }
}

//function mousePressed() {
//    if ( mouseX > 0 && mouseX < width &&
//        mouseY > 0 && mouseY < height) {
//        fillColor = get(mouseX, mouseY);
//        background(fillColor);
//    }
//}
