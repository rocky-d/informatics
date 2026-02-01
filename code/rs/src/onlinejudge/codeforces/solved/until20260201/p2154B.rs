use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let a = (0..n).map(|_| tokens.next().unwrap().parse().unwrap());

    let mut ans = 0;
    let mut a: Vec<i32> = a.collect();
    let mut max = 0;
    for i in 0..n {
        if max < a[i] {
            max = a[i];
        }
        if 0b1 == 0b1 & i {
            a[i] = max;
        }
    }
    let mut x;
    for i in (0..n).step_by(2) {
        if 0 == i {
            x = 0.max(a[i] - (a[i + 1] - 1));
            a[i] -= x;
            ans += x
        } else {
            x = 0.max(a[i] - (a[i - 1] - 1));
            a[i] -= x;
            ans += x
        }
    }
    println!("{ans}");
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    for _ in 0..tokens.next().unwrap().parse().unwrap() {
        solve(&mut tokens);
    }
}
