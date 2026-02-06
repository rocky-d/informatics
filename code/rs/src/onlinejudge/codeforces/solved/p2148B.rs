use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let m = tokens.next().unwrap().parse::<usize>().unwrap();
    let _x = tokens.next().unwrap().parse::<usize>().unwrap();
    let _y = tokens.next().unwrap().parse::<usize>().unwrap();
    let _a = tokens.take(n).collect::<Vec<_>>();
    let _b = tokens.take(m).collect::<Vec<_>>();

    println!("{}", n + m);
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
