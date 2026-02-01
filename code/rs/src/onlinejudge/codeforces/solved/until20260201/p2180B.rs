use std::io::{self, Read};
use std::str::Lines;

fn solve(lines: &mut Lines) {
    let mut ans: String = String::new();
    let _: usize = lines.next().unwrap().parse().unwrap();
    let a = lines.next().unwrap().split_whitespace();
    for ai in a {
        if format!("{}{}", ai, ans) < format!("{}{}", ans, ai) {
            ans.insert_str(0, ai);
        } else {
            ans.push_str(ai);
        }
    }
    println!("{}", ans);
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let mut lines = buf.lines();
    let t: usize = lines.next().unwrap().parse().unwrap();
    for _ in 0..t {
        solve(&mut lines);
    }
}
