use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let mut line = lines.next().unwrap().split_whitespace();
    let mut r: i32 = line.next().unwrap().parse().unwrap();
    let x: i32 = line.next().unwrap().parse().unwrap();
    let d: i32 = line.next().unwrap().parse().unwrap();
    let n: i32 = line.next().unwrap().parse().unwrap();
    let s = lines.next().unwrap();

    let mut ans: i32 = n;
    for c in s.chars() {
        if '1' == c {
            r = 0.max(r - d);
        } else if '2' == c {
            if r < x {
                r = 0.max(r - d);
            } else if x <= r {
                ans -= 1;
            }
        }
    }
    println!("{}", ans);
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
