use std::io::{self, Read};
use std::mem::swap;
use std::str::Lines;

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while 0 != b {
        a %= b;
        swap(&mut a, &mut b);
    }
    a
}

fn solve(lines: &mut Lines) {
    let n: usize = lines.next().unwrap().parse().unwrap();
    let a = lines.next().unwrap().split_whitespace();

    let mut ans: i32 = -1;
    let a = a.map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();
    let mut g = a[0];
    for i in 1..n {
        g = gcd(g, a[i]);
    }
    for x in vec![
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51, 53,
    ] {
        if 0 != g % x {
            ans = x as i32;
            break;
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
