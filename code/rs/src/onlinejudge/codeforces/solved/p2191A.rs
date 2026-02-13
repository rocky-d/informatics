use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let mut idxes = (0..n).collect::<Vec<_>>();
    idxes.sort_by_cached_key(|&i| a[i]);
    let x = 0b1 & idxes[0];
    println!(
        "{}",
        if idxes.iter().step_by(2).all(|i| x == 0b1 & i) {
            "YES"
        } else {
            "NO"
        }
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
