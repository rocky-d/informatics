use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let p = tokens.take(n).map(|x| x.parse::<usize>().unwrap());

    let mut ans = Vec::with_capacity(n);
    let p = p.collect::<Vec<_>>();
    let mut x = 0;
    for (i, &pi) in (1..=n).rev().zip(&p) {
        if i != pi {
            x = i;
            break;
        }
        ans.push(pi.to_string());
    }
    if 0 == x {
        println!("{}", ans.join(" "));
        return;
    }
    for i in (0..n).rev() {
        if x == p[i] {
            for j in (n - x..=i).rev() {
                ans.push(p[j].to_string());
            }
            for j in i + 1..n {
                ans.push(p[j].to_string());
            }
            break;
        }
    }
    println!("{}", ans.join(" "));
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
