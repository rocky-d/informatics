use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();

    let mut ans = Vec::with_capacity(n + n);
    for i in (1..=n).rev() {
        ans.push(i.to_string());
    }
    ans.push(n.to_string());
    for i in 1..n {
        ans.push(i.to_string());
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
