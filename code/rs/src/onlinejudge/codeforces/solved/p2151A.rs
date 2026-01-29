use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<i32>().unwrap();
    let m = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens.take(m).map(|x| x.parse::<i32>().unwrap());

    let a = a.collect::<Vec<_>>();
    let ans = if (1..m).all(|i| 1 == a[i] - a[i - 1]) {
        1 + n - a.iter().max().unwrap()
    } else {
        1
    };
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
