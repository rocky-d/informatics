use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let n: u16 = {
        let mut it = lines
            .next()
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap());
        it.next().unwrap()
    };
    let a = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap());

    let mut ans = 0;
    let mut max = 0;
    for ai in a {
        if max <= ai {
            max = ai;
            ans += 1;
        }
    }
    println!("{}", n - ans);
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
