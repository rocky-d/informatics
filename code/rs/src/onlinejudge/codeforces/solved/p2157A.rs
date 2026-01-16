use std::collections::HashMap;
use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: usize = lines.next().unwrap().parse().unwrap();
    let a = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap());

    let ans: i32;
    let mut map: HashMap<i32, i32> = HashMap::new();
    for ai in a {
        *map.entry(ai).or_insert(0) += 1;
    }
    ans = map
        .into_iter()
        .map(|(k, v)| if v < k { v } else { v - k })
        .sum();
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
