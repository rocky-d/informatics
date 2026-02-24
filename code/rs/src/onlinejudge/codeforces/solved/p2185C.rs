use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let mut ans = 0;
    let mut a = a;
    a.sort_unstable();
    let mut x = 1;
    let mut lst = a[0];
    for ai in a {
        if lst == ai {
            continue;
        }
        if lst + 1 == ai {
            x += 1;
        } else {
            ans = ans.max(x);
            x = 1;
        }
        lst = ai;
    }
    ans = ans.max(x);
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
