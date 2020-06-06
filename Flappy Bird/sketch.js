var bird;
var pipes = [];
var score;
function setup(){
    createCanvas(400, 600);
    bird = new Bird();
    pipes.push(new Pipe());
}
function draw(){
    background(0);
    for(var i=pipes.length-1; i>=0; i--){
        pipes[i].show();
        pipes[i].update();
        if(pipes[i].hits(bird)){
            console.log("hit");
        }
        if(pipes[i].offscreen()) {
            pipes.splice(i, 1);
        }
    }
    bird.update();
    bird.show();
    if(frameCount%100==0){ //파이프 사이의 간격
        pipes.push(new Pipe());
    }
}
function keyPressed(){ //스페이스 누르면 올라가기
    if (key == ' '){
        bird.up();
    }
}