use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: usize = lines.next().unwrap().parse().unwrap();
    let s = lines.next().unwrap();

    let mut ans = 0;
    let mut zeros = 0;
    for _ in 0..2 {
        for c in s.chars() {
            if '0' == c {
                zeros += 1;
            } else if '1' == c {
                ans = ans.max(zeros);
                zeros = 0;
            }
        }
    }
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
