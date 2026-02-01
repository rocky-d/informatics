use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let n: u32 = lines.next().unwrap().parse().unwrap();

    let ans = if 1 == n {
        1
    } else if 2 == n {
        9
    } else if 3 == n {
        29
    } else if 4 == n {
        56
    } else {
        5 * (n * n - n - 1)
    };
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
