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
    if let [first, .., last] = &mut a[..] {
        if -1 == *first {
            *first = *last;
        } else if -1 == *last {
            *last = *first;
        }
    }
    a.iter_mut().for_each(|x| {
        if -1 == *x {
            *x = 0;
        }
    });
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
