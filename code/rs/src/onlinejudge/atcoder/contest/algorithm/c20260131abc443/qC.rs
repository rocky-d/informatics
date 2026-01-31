use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let t = tokens.next().unwrap().parse::<i32>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let mut ans = 0;
    let mut last = 0;
    for ai in a {
        ans += 0.max(ai - last);
        if last < ai {
            last = ai + 100;
        }
    }
    let ai = t;
    ans += 0.max(ai - last);
    println!("{}", ans);
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
