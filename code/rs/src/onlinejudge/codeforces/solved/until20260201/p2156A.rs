use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let n: usize = lines.next().unwrap().parse().unwrap();

    let mut ans = 0;
    let mut m = n as i32;
    while 2 < m {
        let m1 = m / 3;
        m -= m1 + m1;
        ans += m1;
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
