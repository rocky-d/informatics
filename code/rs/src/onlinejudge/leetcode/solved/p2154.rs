use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let mut res = original;
        let set: HashSet<i32> = HashSet::from_iter(nums);
        while set.contains(&res) {
            res *= 2;
        }
        res
    }
}

fn main() {
    let result = Solution::find_final_value(vec![5, 3, 6, 1, 12], 3);
    println!("{}", result);
}
