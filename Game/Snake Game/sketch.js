var s;
var scl = 20;
var food;
//아직 꼬리가 왜 빨간색인지 모름 고치기

function setup(){
    createCanvas(600,600);
    s = new Snake();
    frameRate(10); //속도조절
    pickLocation();
}
function pickLocation(){
    var cols = floor(width/scl);
    var rows = floor(height/scl);
    food = createVector(floor(random(cols)), floor(random(rows)))
    food.mult(scl);
}
function mousePressed(){ //마우스를 누르면 꼬리가 늘어남
    s.total++;
}
function draw(){
    background(51);
    if(s.eat(food)){
        pickLocation();
    }
    s.death();
    s.update();
    s.show();

    if(s.eat(food)){
        pickLocation();
    }

    fill(255, 0, 100);
    rect(food.x, food.y, scl, scl);
}
function keyPressed(){
    if(keyCode==UP_ARROW){
        s.dir(0,-1);
    }
    else if(keyCode==DOWN_ARROW){
        s.dir(0,1);
    }
    else if(keyCode==RIGHT_ARROW){
        s.dir(1,0);
    }
    else if(keyCode==LEFT_ARROW){
        s.dir(-1,0);
    }
}
