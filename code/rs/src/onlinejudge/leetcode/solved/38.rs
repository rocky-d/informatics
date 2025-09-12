struct Solution;

impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut s0;
        let mut s1 = String::from("1");
        let mut c0;
        let mut cnt;
        for _ in 1..n {
            s0 = s1;
            s1 = String::new();
            c0 = s0.chars().nth(0).unwrap();
            cnt = 1;
            for c1 in (s0 + "_").chars().skip(1) {
                if c1 == c0 {
                    cnt += 1;
                    continue;
                }
                s1.push_str(&cnt.to_string());
                s1.push(c0);
                c0 = c1;
                cnt = 1;
            }
        }
        s1
    }
}

fn main() {
    let result = Solution::count_and_say(4);
    println!("{:?}", result);
}
