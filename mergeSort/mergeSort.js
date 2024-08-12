function splitTheList(listToSplit) {
    if (listToSplit.length > 1) {
        const middle = Math.floor(listToSplit.length / 2);
        return [listToSplit.slice(0, middle), listToSplit.slice(middle)];
    } else {
        console.log("One Item List");
        return [listToSplit, []];
    }
}

function merge(left, right) {
    const merged = [];
    let leftIndexTracker = 0;
    let rightIndexTracker = 0;

    while (leftIndexTracker < left.length && rightIndexTracker < right.length) {
        if (left[leftIndexTracker].height < right[rightIndexTracker].height) {
            merged.push(left[leftIndexTracker]);
            leftIndexTracker++;
        } else {
            merged.push(right[rightIndexTracker]);
            rightIndexTracker++;
        }
    }

    while (leftIndexTracker < left.length) {
        merged.push(left[leftIndexTracker]);
        leftIndexTracker++;
    }

    while (rightIndexTracker < right.length) {
        merged.push(right[rightIndexTracker]);
        rightIndexTracker++;
    }

    return merged;
}

function mergeSort(listToSort) {
    if (listToSort.length <= 1) {
        return listToSort;
    }

    const [left, right] = splitTheList(listToSort);
    return merge(mergeSort(left), mergeSort(right));
}

document.addEventListener('DOMContentLoaded', function() {
    var generateButton = document.getElementById('generateButton');
    var barContainer = document.getElementById('barContainer');
    var originalBar = document.createElement('div');
    var mergeSortButton = document.getElementById('mergeSort');

    originalBar.className = 'bar';

    function getRandomHeight(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function generateBars(count) {
        barContainer.innerHTML = '';

        for (var i = 0; i < count; i++) {
            var clonedBar = originalBar.cloneNode();
            var randomHeight = getRandomHeight(50, 420);
            clonedBar.style.height = randomHeight + 'px';
            barContainer.appendChild(clonedBar);
        }
    }



// Function to introduce a delay
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Async function to loop and wait
async function loopWithDelay() {
    for (let i = 1; i <= 42; i++) {
        console.log(i); // Your code here to execute on each iteration
        await sleep(2000); // Wait for 2 seconds (2000 milliseconds)
    }
}

// Start the loop



    generateButton.addEventListener('click', function() {
        var numberOfClones = 1; // Change this number as needed
        generateBars(numberOfClones);
        async function loopWithDelay() {
            for (let i = 1; i <= 42; i++) {
                console.log(i); // Your code here to execute on each iteration
                generateBars(i);

                await sleep(400); // Wait for 2 seconds (2000 milliseconds)
                var bars = Array.from(barContainer.getElementsByClassName("bar"));

                // Create an array of objects with the element and its height
                var barsWithHeights = bars.map(function(item) {
                    return {
                        element: item,
                        height: parseInt(item.style.height, 10)
                    };
                });
        
                // Sort the array of objects by height
                var sortedBars = mergeSort(barsWithHeights);
        
                // Clear the container and append bars in sorted order
                barContainer.innerHTML = '';
                sortedBars.forEach(function(bar) {
                    barContainer.appendChild(bar.element);
                });     
                
                await sleep(400); // Wait for 2 seconds (2000 milliseconds)

            }
        }
        loopWithDelay()
    });

    mergeSortButton.addEventListener('click', function() {
        console.log("sorting");
        var bars = Array.from(barContainer.getElementsByClassName("bar"));

        // Create an array of objects with the element and its height
        var barsWithHeights = bars.map(function(item) {
            return {
                element: item,
                height: parseInt(item.style.height, 10)
            };
        });

        // Sort the array of objects by height
        var sortedBars = mergeSort(barsWithHeights);

        // Clear the container and append bars in sorted order
        barContainer.innerHTML = '';
        sortedBars.forEach(function(bar) {
            barContainer.appendChild(bar.element);
        });
    });
});

// Function to introduce a delay
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
