use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: i32 = lines.next().unwrap().parse().unwrap();
    let a = lines.next().unwrap().split_whitespace();

    let mut a: Vec<i32> = a.map(|x| x.parse().unwrap()).collect();
    if !a.iter().all(|x| 0 == x % 2) && !a.iter().all(|x| 1 == x % 2) {
        a.sort();
    }
    let out: Vec<_> = a.iter().map(|x| x.to_string()).collect();
    println!("{}", out.join(" "));
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
