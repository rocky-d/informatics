function moveZeroes(nums: number[]): void {
    let n: number = nums.length;
    let i: number = 0;
    while (i < n) {
        if (0 == nums[i]) {
            nums.splice(i, 1);
            nums.push(0);
            n -= 1;
        } else {
            i += 1
        }
    }
}