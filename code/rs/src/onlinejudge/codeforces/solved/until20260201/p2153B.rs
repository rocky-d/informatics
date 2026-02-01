use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let xyz = tokens.take(3).map(|x| x.parse::<i32>().unwrap());

    let mut ans = "YES";
    let xyz = xyz
        .map(|x| format!("{:032b}", x).into_bytes())
        .collect::<Vec<_>>();
    let mut cnt;
    for i in 0..32 {
        cnt = 0;
        for j in 0..3 {
            if b'1' == xyz[j][i] {
                cnt += 1;
            }
        }
        if 2 == cnt {
            ans = "NO";
            break;
        }
    }
    println!("{ans}");
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
