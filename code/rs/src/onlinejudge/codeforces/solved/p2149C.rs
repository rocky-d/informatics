use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n = tokens.next().unwrap().parse::<usize>().unwrap();
    let k = tokens.next().unwrap().parse::<i32>().unwrap();
    let a = tokens.take(n).map(|x| x.parse::<i32>().unwrap());

    let mut ans = 0;
    let mut map = std::collections::HashMap::new();
    for ai in a {
        *map.entry(ai).or_insert(0) += 1;
    }
    for x in 0..k {
        if !map.contains_key(&x) {
            ans += 1;
        }
    }
    ans = ans.max(*map.entry(k).or_insert(0));
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
