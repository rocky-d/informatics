use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let n: i32 = lines.next().unwrap().parse().unwrap();
    let a = lines.next().unwrap().split_whitespace();

    let mut ans = "YES";
    let mut a: Vec<i32> = a.map(|x| x.parse().unwrap()).collect();
    a.sort();
    for i in (1..n - 1).step_by(2) {
        if a[i as usize] != a[(i + 1) as usize] {
            ans = "NO";
            break;
        }
    }
    println!("{}", ans)
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut lines = buf.lines();
    let t: u32 = lines.next().unwrap().parse().unwrap();
    for _ in 0..t {
        solve(&mut lines);
    }
}
