'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var first_large = nums[0];
    var second_large = nums[0];
    // console.log("initially ",first_large,second_large);
    for (var i in nums) {
        // console.log(nums[i]);
        if (nums[i] > first_large) {
            second_large = first_large;
            first_large = nums[i];
        }
        else if (nums[i] < first_large && nums[i] > second_large) {
            second_large = nums[i];
        }
    }
    return second_large;
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}
