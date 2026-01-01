use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let _n: u32 = lines.next().unwrap().parse().unwrap();
    let a = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap());

    let mut a: Vec<i32> = a.collect();
    if Some(&-1) == a.first() {
        if let [first, .., last] = &mut a[..] {
            *first = *last;
        }
    } else if Some(&-1) == a.last() {
        if let [first, .., last] = &mut a[..] {
            *last = *first;
        }
    }
    for i in 0..a.len() {
        if -1 == a[i] {
            a[i] = 0;
        }
    }
    let (Some(first), Some(last)) = (a.first(), a.last()) else {
        return;
    };
    println!("{}", (last - first).abs());
    let out: Vec<_> = a.iter().map(|x| x.to_string()).collect();
    println!("{}", out.join(" "));
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
