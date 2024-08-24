fn is_prime(num: u64) -> bool {
    if num < 2 {
        return false;
    }
    for i in 2..=num / 2 {
        if num % i == 0 {
            return false;
        }
    }
    return true;
}
