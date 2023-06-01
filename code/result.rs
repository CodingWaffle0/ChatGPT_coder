impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x_str = x.to_string(); // Convert `x` to a string
        let mid_index = x_str.len() / 2; // Find the index of the middle character
        let (left, right) = x_str.split_at(mid_index); // Split `x_str` into two halves
        
        let reversed_right: String = right.chars().rev().collect(); // Reverse the right half
        left == reversed_right // Check if left half is equal to reversed right half
    }
}