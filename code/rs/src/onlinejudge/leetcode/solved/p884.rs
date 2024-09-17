struct Solution;
use std::collections::HashMap;
impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let words1: Vec<String> = s1.split(' ').map(String::from).collect();
        let words2: Vec<String> = s2.split(' ').map(String::from).collect();
        let mut cnter = HashMap::new();
        for word in words1.iter() {
            if let Some(cnt) = cnter.get_mut(word) {
                *cnt += 1;
            } else {
                cnter.insert(word, 1);
            }
        }
        for word in words2.iter() {
            if let Some(cnt) = cnter.get_mut(word) {
                *cnt += 1;
            } else {
                cnter.insert(word, 1);
            }
        }
        let mut result = Vec::new();
        for (key, value) in cnter.iter() {
            if *value == 1 {
                result.push(key.to_string());
            }
        }
        return result;
    }
}
fn main() {
    let words: Vec<String> = Solution::uncommon_from_sentences(
        "this apple is sweet".to_string(),
        "this apple is sour".to_string(),
    );
    println!("{:?}", words);
}
