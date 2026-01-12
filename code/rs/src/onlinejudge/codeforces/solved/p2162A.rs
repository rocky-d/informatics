use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: i32 = lines.next().unwrap().parse().unwrap();
    let a = lines.next().unwrap().split_whitespace();

    println!("{}", a.map(|x| x.parse::<i32>().unwrap()).max().unwrap());
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
