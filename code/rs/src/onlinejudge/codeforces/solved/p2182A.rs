use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let _n = tokens.next().unwrap().parse::<usize>().unwrap();
    let s = tokens.next().unwrap();

    let ans = if s.contains("2026") || !s.contains("2025") {
        0
    } else {
        1
    };
    println!("{}", ans);
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    // let t = 1;
    let t = tokens.next().unwrap().parse().unwrap();
    for _ in 0..t {
        solve(&mut tokens);
    }
}
