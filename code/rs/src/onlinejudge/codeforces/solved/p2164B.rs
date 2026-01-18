use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let n: usize = lines.next().unwrap().parse().unwrap();
    let a = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap());

    let a: Vec<i32> = a.collect();
    let mut even1 = 0;
    for ai in &a {
        if 0b0 == 0b1 & ai {
            even1 = *ai;
            break;
        }
    }
    let mut even2 = 0;
    for ai in a.iter().rev() {
        if 0b0 == 0b1 & ai {
            even2 = *ai;
            break;
        }
    }
    if even1 != even2 {
        println!("{even1} {even2}");
        return;
    }
    for i in 0..n {
        for j in (i + 1)..n.min(i + 32) {
            if 0b0 == 0b1 & a[j] % a[i] {
                println!("{} {}", a[i], a[j]);
                return;
            }
        }
    }
    println!("-1");
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
