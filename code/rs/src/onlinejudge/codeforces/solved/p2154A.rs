use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    let s = tokens.next().unwrap();

    let mut ans = 0;
    let s = s.as_bytes();
    let mut x = k;
    for i in 0..n {
        x += 1;
        if b'1' == s[i] {
            if k <= x {
                ans += 1
            }
            x = 0;
        }
    }
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
