use std::collections::HashMap;
use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: i32 = lines.next().unwrap().parse().unwrap();
    let mut a = lines.next().unwrap().split_whitespace();

    let s = a.next().unwrap();
    let t = a.next().unwrap();
    let mut map = HashMap::new();
    for c in s.chars() {
        *map.entry(c).or_insert(0) += 1;
    }
    for c in t.chars() {
        *map.entry(c).or_insert(0) -= 1;
    }
    println!(
        "{}",
        if map.values().all(|x| &0 == x) {
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
