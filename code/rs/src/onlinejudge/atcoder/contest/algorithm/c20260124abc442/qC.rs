use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();

    let mut ans: Vec<i64> = Vec::with_capacity(n + 1);
    let mut a: usize;
    let mut b: usize;
    let mut cnt = vec![0; n + 1];
    for _ in 0..m {
        a = tokens.next().unwrap().parse().unwrap();
        b = tokens.next().unwrap().parse().unwrap();
        cnt[a] += 1;
        cnt[b] += 1;
    }
    for i in 1..=n {
        let x = n as i64 - cnt[i] as i64 - 1_i64;
        if x < 3 {
            ans.push(0);
            continue;
        }
        ans.push((x * (x - 1) * (x - 2)) / 6);
    }
    let ans_str = ans
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" ");
    println!("{}", ans_str);
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut tokens = buf.split_whitespace();
    solve(&mut tokens);
    // for _ in 0..tokens.next().unwrap().parse().unwrap() {
    //     solve(&mut tokens);
    // }
}
