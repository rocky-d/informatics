use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: i32 = lines.next().unwrap().parse().unwrap();
    let a = lines.next().unwrap().split_whitespace();
    let x: i32 = lines.next().unwrap().parse().unwrap();

    let a: Vec<i32> = a.map(|x| x.parse().unwrap()).collect();
    println!(
        "{}",
        if a.iter().min().unwrap() <= &x && &x <= a.iter().max().unwrap() {
            "YES"
        } else {
            "NO"
        }
    )
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
