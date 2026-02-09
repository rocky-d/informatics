use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let q = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();
    let b = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();
    let mut lr = tokens.take(q + q).map(|x| x.parse::<usize>().unwrap());

    let mut ans = Vec::with_capacity(q);
    let mut a = a
        .iter()
        .zip(b)
        .map(|(&ai, bi)| ai.max(bi))
        .collect::<Vec<_>>();
    let mut max = 0;
    for i in (0..n).rev() {
        if max < a[i] {
            max = a[i];
        }
        a[i] = max;
    }
    a.insert(0, 0);
    for i in 1..1 + n {
        a[i] += a[i - 1];
    }
    let mut l;
    let mut r;
    for _ in 0..q {
        l = lr.next().unwrap();
        r = lr.next().unwrap();
        ans.push((a[r] - a[l - 1]).to_string());
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
