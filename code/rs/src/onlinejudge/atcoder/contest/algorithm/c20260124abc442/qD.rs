use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let a = tokens.take(n).map(|x| x.parse::<i32>().unwrap());

    let mut prefs: Vec<i32> = vec![0; n + 1];
    for (i, val) in a.enumerate() {
        prefs[i + 1] = prefs[i] + val;
    }
    for _ in 0..q {
        let o = tokens.next().unwrap();
        if "1" == o {
            let x = tokens.next().unwrap().parse::<usize>().unwrap();
            let a = prefs[x] - prefs[x - 1];
            let b = prefs[x + 1] - prefs[x];
            prefs[x] = prefs[x - 1] + b;
            prefs[x + 1] = prefs[x] + a;
        } else if "2" == o {
            let l = tokens.next().unwrap().parse::<usize>().unwrap();
            let r = tokens.next().unwrap().parse::<usize>().unwrap();
            let res = prefs[r] - prefs[l - 1];
            println!("{}", res);
        }
    }
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
