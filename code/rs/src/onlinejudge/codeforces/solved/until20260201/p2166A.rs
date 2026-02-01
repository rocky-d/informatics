use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: i32 = lines.next().unwrap().parse().unwrap();
    let s = lines.next().unwrap();

    let mut cnt = 0;
    let mut chars = s.chars().rev();
    let first = chars.next().unwrap();
    for c in chars {
        if first != c {
            cnt += 1;
        }
    }
    println!("{}", cnt);
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
