struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut dp0 = 0;
        let mut dp1 = -prices[0];
        for i in 1..prices.len() {
            dp0 = dp0.max(dp1 + prices[i]);
            dp1 = dp1.max(-prices[i]);
        }
        dp0
    }
}

fn main() {
    let result = Solution::max_profit([7, 1, 5, 3, 6, 4].to_vec());
    println!("{:?}", result);
}
