use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();

    let mut p = vec![0; n];
    let mut x = 0;
    for i in (0..n).rev().step_by(2) {
        x += 1;
        p[i] = x;
    }
    for i in (0b1 & n..n).step_by(2) {
        x += 1;
        p[i] = x;
    }
    println!(
        "{}",
        p.iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
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
