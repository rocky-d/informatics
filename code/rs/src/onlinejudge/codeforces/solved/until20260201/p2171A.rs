use std::io;

fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf).unwrap();

    let t: i8 = buf.trim().parse().unwrap();
    let mut n: i8;
    for _ in 0..t {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        n = buf.trim().parse().unwrap();
        if 1 == 0b1 & n {
            println!("0");
            continue;
        }
        println!("{}", 1 + n / 4);
    }
}
