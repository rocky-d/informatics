use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let q = tokens.next().unwrap().parse::<usize>().unwrap();
    let s = tokens.next().unwrap().as_bytes();
    let a = tokens.take(q).map(|x| x.parse::<usize>().unwrap());

    if !s.contains(&b'B') {
        for ai in a {
            println!("{}", ai);
        }
        return;
    }
    let mut res;
    let mut i;
    for mut ai in a {
        res = 0;
        i = 0;
        while 0 < ai {
            res += 1;
            if b'A' == s[i] {
                ai -= 1;
            } else {
                ai /= 2;
            }
            i = (i + 1) % n;
        }
        println!("{}", res);
    }
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
