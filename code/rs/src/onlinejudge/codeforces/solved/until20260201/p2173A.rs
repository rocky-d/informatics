use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let mut it = lines.next().unwrap().split_whitespace();
    let _n: u8 = it.next().unwrap().parse().unwrap();
    let k: u8 = it.next().unwrap().parse().unwrap();
    let s = lines.next().unwrap();

    let mut ans = 0;
    let mut cd = 0;
    for c in s.chars() {
        if '1' == c {
            cd = k;
        } else {
            if 0 < cd {
                cd -= 1
            } else {
                ans += 1;
            }
        }
    }
    println!("{}", ans)
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
