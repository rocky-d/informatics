use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n: i32 = tokens.next().unwrap().parse().unwrap();

    let ans = 2 * (n - 1);
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
