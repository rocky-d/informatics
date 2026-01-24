use std::io::{self, Read};

fn solve<'a>(tokens: &mut impl Iterator<Item = &'a str>) {
    let q: i32 = tokens.next().unwrap().parse().unwrap();
    let a = (0..q).map(|_| tokens.next().unwrap().parse().unwrap());

    let mut ans = 0;
    let a: Vec<i32> = a.collect();
    let mut stopped = true;
    for ai in a {
        if 1 == ai {
            ans +=1;
        } else if 2 == ai {
            if 0 < ans {
                ans -= 1;
            }
        } else if 3 == ai {
            stopped = !stopped;
        }
        if !stopped && 3 <= ans {
            println!("Yes");
        }
        else {
            println!("No");
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
