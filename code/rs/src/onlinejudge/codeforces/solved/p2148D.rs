use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens.take(n).map(|x| x.parse::<u64>().unwrap());

    let mut ans = 0;
    let mut eves = Vec::with_capacity(n);
    let mut odds = Vec::with_capacity(n);
    for ai in a {
        if 0b0 == 0b1 & ai {
            eves.push(ai);
        } else {
            odds.push(ai);
        }
    }
    if 0 == odds.len() {
        println!("{}", ans);
        return;
    }
    ans += eves.iter().sum::<u64>();
    odds.sort_unstable();
    let mut state = false;
    let mut i = odds.len();
    for _ in 0..odds.len() {
        state = !state;
        if state {
            i -= 1;
            ans += odds[i];
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
