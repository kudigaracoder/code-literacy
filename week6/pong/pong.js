function setup() {
  createCanvas(800, 600);
  background(0);
  noStroke();
  fill(0, 255, 0);
}

var ballX = 100;
var ballY = 100;

var ballXV = -4;
var ballYV = 1;

var rectX = 10;
var rectY = 10;

//User defined
var plyr2X = 750;
var plyr2Y = 10;
var plyr2Speed = 50;
var plyr2Xdamp = 0;
var plyr2Ydamp = 0;
var keyValue;

var lives = 3;

function draw() {
    rect(300,30,50,50);
    background(0);
    setText();
    setShapes();
    bounceCheck();
    increment();
    scoreCheck();
}

function increment() {
  ballX += ballXV;
  ballY += ballYV;

  if(millis() % 1000 == 0) {
    ballXV = ballXV * 2;
  }
}

function mouseMoved() {
    rectY = mouseY;
}

function keyPressed() {
    if (keyCode === DOWN_ARROW) {
        plyr2Y += plyr2Speed;
    } else if (keyCode === UP_ARROW) {
        plyr2Y -= plyr2Speed;
    }

    this.update = function() {
    this.move();
    }

    this.move = function() {
    plyr2Y += plyr2Ydamp;
    }
    // dampenings
    plyr2Ydamp *= 0.9;

}

function ball(x, y) {
  ellipse(x - 2, y, 30, 30);
  ellipse(x, y, 15, 15);
}

function setShapes() {
    fill(255);
    rect(rectX, rectY, 20, 75);
    rect(plyr2X, plyr2Y, 20, 75);
    ball(ballX, ballY);
}

function sliderBounce() {
  if(rectY < ballY && rectY + 100 > ballY) {
    ballXV = ballXV * -1;
    lives += 1;
  }
}

function wallBounce() {
  ballXV = ballXV * -1;
}

function bounceCheck() {
  if(ballY < 0 || ballY > 600) {
    ballYV = ballYV * -1;
  }

  if(ballX < 40 && ballXV < 0) {
    sliderBounce();
  }

  if(ballX > 800 && ballXV > 0) {
    wallBounce();
  }

  if(ballX < 0) {
    ballX = 800;
    lives -= 1;
  }
}

function scoreCheck() {
  if(lives == 0) {
    noLoop();
    lives = "YOU LOSE";
  }

  if(lives == 10) {
    noLoop();
    lives = "YOU WIN";
  }
}

function setText() {
  textAlign(CENTER);
  textSize(22);
  text(lives, 10, 20);
}
