use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let r = tokens.next().unwrap();

    let mut ans = 0;
    let mut r = r.bytes().collect::<Vec<_>>();
    let n = r.len();
    if b'u' == r[0] {
        r[0] = b's';
        ans += 1;
    }
    if b'u' == r[n - 1] {
        r[n - 1] = b's';
        ans += 1;
    }
    let mut i = 0;
    while i < r.len() {
        let c = r[i];
        let mut cnt = 0;
        while i < r.len() && c == r[i] {
            cnt += 1;
            i += 1;
        }
        if b'u' == c {
            ans += cnt / 2;
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
