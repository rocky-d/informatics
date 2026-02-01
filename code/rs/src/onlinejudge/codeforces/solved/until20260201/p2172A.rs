use std::io;

fn main() {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer).unwrap();
    let mut nums: Vec<i8> = buffer
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    nums.sort();
    if 10 <= nums[2] - nums[0] {
        println!("check again");
    } else {
        println!("final {}", nums[1]);
    }
}
