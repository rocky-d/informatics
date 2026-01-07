use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let abcd = lines.next().unwrap().split_whitespace();

    let abcd: Vec<&str> = abcd.collect();
    println!(
        "{}",
        if abcd.iter().all(|x| *x == abcd[0]) {
            "YES"
        } else {
            "NO"
        }
    );
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut lines = buf.lines();
    let t: u32 = lines.next().unwrap().parse().unwrap();
    for _ in 0..t {
        solve(&mut lines);
    }
}
