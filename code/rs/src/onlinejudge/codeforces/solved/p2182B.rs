use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let a = tokens.next().unwrap().parse::<i32>().unwrap();
    let b = tokens.next().unwrap().parse::<i32>().unwrap();

    let mut ans = 0;
    let mut mut_a = a;
    let mut mut_b = b;
    let mut level = 0;
    loop {
        if 0b0 == 0b1 & level {
            mut_a -= 2i32.pow(level);
            if mut_a < 0 {
                break;
            }
        } else {
            mut_b -= 2i32.pow(level);
            if mut_b < 0 {
                break;
            }
        }
        level += 1;
    }
    ans = ans.max(level);
    let mut mut_a = a;
    let mut mut_b = b;
    let mut level = 0;
    loop {
        if 0b1 == 0b1 & level {
            mut_a -= 2i32.pow(level);
            if mut_a < 0 {
                break;
            }
        } else {
            mut_b -= 2i32.pow(level);
            if mut_b < 0 {
                break;
            }
        }
        level += 1;
    }
    ans = ans.max(level);
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
