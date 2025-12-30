use std::collections::HashSet;
use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let (l, a, b): (u16, u16, u16) = {
        let mut it = lines
            .next()
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap());
        (it.next().unwrap(), it.next().unwrap(), it.next().unwrap())
    };
    let mut a = a;
    let mut vis = HashSet::new();
    while !vis.contains(&a) {
        vis.insert(a);
        a = (a + b) % l;
    }
    println!("{}", vis.iter().max().unwrap());
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
