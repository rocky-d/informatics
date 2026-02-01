use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let s = tokens.next().unwrap();

    let s = [b" ", s.as_bytes()].concat();
    let mut indices = Vec::with_capacity(n);
    let mut l = 1;
    let mut r = n;
    let mut flag = true;
    while l < r {
        if b'1' == s[l] && b'0' == s[r] {
            indices.push(l);
            l += 1;
            flag = false;
        } else if b'0' == s[l] && b'1' == s[r] {
            if flag {
                indices.push(l);
                l += 1;
            }
            indices.push(r);
            r -= 1;
        } else {
            l += 1;
            r -= 1;
        }
    }
    indices.sort();
    println!("{}", indices.len());
    println!(
        "{}",
        indices
            .iter()
            .map(ToString::to_string)
            .collect::<Vec<_>>()
            .join(" "),
    );
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    for _ in 0..tokens.next().unwrap().parse().unwrap() {
        solve(&mut tokens);
    }
}
