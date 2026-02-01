use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let mut abn = lines.next().unwrap().split_whitespace();

    let a: u64 = abn.next().unwrap().parse().unwrap();
    let b: u64 = abn.next().unwrap().parse().unwrap();
    let n: u64 = abn.next().unwrap().parse().unwrap();
    println!("{}", if a == b || b * n <= a { 1 } else { 2 });
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
