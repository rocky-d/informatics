use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let m = tokens.next().unwrap().parse::<i32>().unwrap();
    let mut ab = tokens.take(n + n).map(|x| x.parse::<i32>().unwrap());

    let mut ans = m;
    let mut switch = 0b1;
    let mut a;
    let mut b;
    for _ in 0..n {
        a = 0b1 & ab.next().unwrap();
        b = 0b1 & ab.next().unwrap();
        if 0b0 == switch ^ a ^ b {
            switch = 1 - switch;
            ans -= 1;
        }
    }
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
