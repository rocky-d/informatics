use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<i128>().unwrap();
    let k = tokens.next().unwrap().parse::<i128>().unwrap();

    let mut lo = 0 - 1;
    let mut hi = k + 1;
    while 1 < hi - lo {
        let mid = lo + hi >> 1;
        if mid * (mid + 1) / 2 + n * (mid + 1) < k {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    println!("{}", hi);
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    let t = 1;
    // let t = tokens.next().unwrap().parse().unwrap();
    for _ in 0..t {
        solve(&mut tokens);
    }
}
