// Define constants and variables
const canvas = document.getElementById('mazeCanvas');
const ctx = canvas.getContext('2d');
const graphSize = 20;  // Size of the maze
const numberOfBlockedNodes = 100;  // Number of blocked nodes
const animationSpeed = 100;  // Animation speed in milliseconds

let maze = new Array(graphSize).fill().map(() => new Array(graphSize).fill(0));
let blockedNodes = new Array(graphSize).fill().map(() => new Array(graphSize).fill(0));
let marked = new Array(graphSize).fill().map(() => new Array(graphSize).fill(false));

// Generate blocked nodes
generateBlockedNodes(numberOfBlockedNodes);

// Generate graph adjacency list
let Graph = generateGraph();

// Perform DFS to generate maze
let stack = [];
let animationInterval;

function startDFS() {
    // Initialize DFS from a random starting point
    let startX = Math.floor(Math.random() * graphSize);
    let startY = Math.floor(Math.random() * graphSize);
    stack.push([startX, startY]);
    animateDFS();
}

function animateDFS() {
    if (stack.length === 0) {
        clearInterval(animationInterval);
        console.log("DFS complete");
        return;
    }

    let node = stack.pop();
    let x = node[0], y = node[1];
    
    if (blockedNodes[x][y] === 1 || marked[x][y]) {
        animateDFS();  // Skip blocked nodes or already visited nodes
        return;
    }

    visit(node);
    showMaze();
    marked[x][y] = true;
    shuffleArray(Graph[node]);

    Graph[node].forEach(neighbor => {
        if (!marked[neighbor[0]][neighbor[1]]) {
            stack.push(neighbor);
        }
    });

    animationInterval = setTimeout(animateDFS, animationSpeed);
}

// Function to generate blocked nodes randomly
function generateBlockedNodes(numberOfBlockedNodes) {
    while (numberOfBlockedNodes > 0) {
        let x = Math.floor(Math.random() * graphSize);
        let y = Math.floor(Math.random() * graphSize);
        if (blockedNodes[x][y] === 0) {
            blockedNodes[x][y] = 1;
            numberOfBlockedNodes--;
        }
    }
}

// Function to generate graph adjacency list
function generateGraph() {
    let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let Graph = {};

    for (let x = 0; x < graphSize; x++) {
        for (let y = 0; y < graphSize; y++) {
            Graph[[x, y]] = [];
            directions.forEach(neighbor => {
                let newX = x + neighbor[0];
                let newY = y + neighbor[1];
                if (newX >= 0 && newX < graphSize && newY >= 0 && newY < graphSize) {
                    Graph[[x, y]].push([newX, newY]);
                }
            });
        }
    }

    return Graph;
}

// Function to perform DFS
function dfs(startNode) {
    stack.push(startNode);
    animateDFS();
}

// Function to visit a node
function visit(node) {
    let x = node[0], y = node[1];
    maze[x][y] = 1;
}

// Function to shuffle an array (Fisher-Yates shuffle)
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Function to draw the maze on canvas
function showMaze() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let cellWidth = canvas.width / graphSize;
    let cellHeight = canvas.height / graphSize;

    for (let i = 0; i < graphSize; i++) {
        for (let j = 0; j < graphSize; j++) {
            if (maze[i][j] === 1) {
                ctx.fillStyle = '#8B0000';
            } else if (blockedNodes[i][j] === 1) {
                ctx.fillStyle = '#000';  // Blocked nodes color
            } else {
                ctx.fillStyle = '#fff';
            }
            ctx.fillRect(j * cellWidth, i * cellHeight, cellWidth, cellHeight);
            ctx.strokeStyle = '#ccc';
            ctx.strokeRect(j * cellWidth, i * cellHeight, cellWidth, cellHeight);
        }
    }
}

// Start DFS process
startDFS();
