use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let s = tokens.next().unwrap().parse::<i32>().unwrap();
    let x = tokens.next().unwrap().parse::<i32>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let diff = s - a.iter().sum::<i32>();
    println!(
        "{}",
        if 0 <= diff && 0 == diff % x {
            "YES"
        } else {
            "NO"
        }
    );
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
