function setup() {
    var canvas = createCanvas(800, 600);
    canvas.parent("canvas-parent");
}
var vertexes = [];

function draw() {

    fill(51)
    stroke(0);
    strokeWeight(4)
    beginShape()
    if (mouseIsPressed) {
        vertex(vertexes[0], vertexes[1]);
        vertex(mouseX, mouseY);
        vertexes = [mouseX, mouseY];
    }
    if (!mouseIsPressed) {
        vertexes = [];
    }
    endShape(CLOSE);
}