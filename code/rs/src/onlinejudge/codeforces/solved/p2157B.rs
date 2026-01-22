use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n: i32 = tokens.next().unwrap().parse().unwrap();
    let mut x: i32 = tokens.next().unwrap().parse().unwrap();
    let mut y: i32 = tokens.next().unwrap().parse().unwrap();
    let s: &str = tokens.next().unwrap();

    x = n - x.abs();
    y = n - y.abs();
    if x < 0 || y < 0 {
        println!("NO");
        return;
    }
    let f = s.chars().filter(|&c| '4' == c).count() as i32;
    let ans = if f <= x + y { "YES" } else { "NO" };
    println!("{ans}");
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    for _ in 0..tokens.next().unwrap().parse().unwrap() {
        solve(&mut tokens);
    }
}
