use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let n: i32 = lines.next().unwrap().parse().unwrap();
    let mut line = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap());
    let y: i32 = line.next().unwrap();
    let r: i32 = line.next().unwrap();

    let ans = n.min(r + y / 2);
    println!("{ans}");
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
