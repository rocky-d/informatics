use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let mut h = tokens.next().unwrap().parse::<i32>().unwrap();
    let mut l = tokens.next().unwrap().parse::<i32>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    if h > l {
        let tmp = h;
        h = l;
        l = tmp;
    }
    let mut x = 0;
    let mut y = 0;
    for ai in a {
        if ai <= h {
            x += 1;
        } else if ai <= l {
            y += 1;
        }
    }
    let ans = x.min(y) + 0.max(x - y) / 2;
    println!("{ans}");
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
