impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (i, &num1) in nums.iter().enumerate() {
            for (j, &num2) in nums.iter().enumerate() {
                if i == j {
                    continue;
                }
                if target == num1 + num2 {
                    return vec![i as i32, j as i32];
                }
            }
        }
        return vec![];
    }
}
