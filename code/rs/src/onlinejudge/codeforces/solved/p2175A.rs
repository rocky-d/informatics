use std::collections::HashSet;
use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: usize = lines.next().unwrap().parse().unwrap();
    let mut colors: HashSet<usize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let mut ci = colors.len();
    while !colors.contains(&ci) {
        colors.insert(ci);
        ci = colors.len();
    }
    println!("{}", ci);
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut lines = buf.lines();
    let t: usize = lines.next().unwrap().parse().unwrap();
    for _ in 0..t {
        solve(&mut lines);
    }
}
