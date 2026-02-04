use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let x = tokens.next().unwrap().parse::<u8>().unwrap();
    let n = tokens.next().unwrap().parse::<u8>().unwrap();

    let ans = if 0b0 == 0b1 & n { 0 } else { x };
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
