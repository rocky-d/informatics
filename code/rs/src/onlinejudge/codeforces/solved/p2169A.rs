use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let mut it = lines.next().unwrap().split_whitespace();
    let _n: i32 = it.next().unwrap().parse().unwrap();
    let a: i32 = it.next().unwrap().parse().unwrap();
    let v = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap());

    let mut l = 0;
    let mut r = 0;
    for vi in v {
        if vi < a {
            l += 1;
        } else if a < vi {
            r += 1;
        }
    }
    if l < r {
        println!("{}", a + 1);
    } else {
        println!("{}", a - 1);
    }
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
