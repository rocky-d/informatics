/**
 * @param {number[]} nums
 * @return {void}
 */
var moveZeroes = function (nums) {
    let n = nums.length;
    let i = 0;
    while (i < n) {
        if (0 === nums[i]) {
            nums.splice(i, 1);
            nums.push(0);
            n -= 1;
        } else {
            i += 1
        }
    }
};
