impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x % 10 == 0 && x != 0) {
            return false;
        }
        
        let x_str = x.to_string();
        let mid_index = x_str.len() / 2;
        let (left, right) = x_str.split_at(mid_index);

        let reversed_right: String = right.chars().rev().collect();
        left == reversed_right
    }
}
