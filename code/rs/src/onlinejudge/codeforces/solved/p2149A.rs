use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens.take(n).map(|x| x.parse::<i32>().unwrap());

    let mut minusones = 0;
    let mut zeros = 0;
    for ai in a {
        if -1 == ai {
            minusones += 1;
        } else if 0 == ai {
            zeros += 1;
        }
    }
    let ans = 2 * (0b1 & minusones) + zeros;
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
