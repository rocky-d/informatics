use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let s = tokens.next().unwrap();

    let mut ans = 0;
    let s = s.as_bytes();
    for i in 0..s.len() {
        if s[i] == b'i' || s[i] == b'j' {
            ans += 1;
        }
    }
    println!("{ans}");
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    // for _ in 0..tokens.next().unwrap().parse().unwrap() {
    //     solve(&mut tokens);
    // }
    solve(&mut tokens);
}
