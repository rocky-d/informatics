use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let a = tokens
        .take(n)
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let sum = (0..n - 1).map(|i| a[i].abs_diff(a[i + 1])).sum::<u32>();
    let mut ans = sum;
    for i in 0 + 1..n - 1 {
        ans = ans.min(
            sum + a[i - 1].abs_diff(a[i + 1]) - a[i].abs_diff(a[i - 1]) - a[i].abs_diff(a[i + 1]),
        );
    }
    ans = ans.min(sum - a[0].abs_diff(a[1]));
    ans = ans.min(sum - a[n - 1].abs_diff(a[n - 2]));
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
