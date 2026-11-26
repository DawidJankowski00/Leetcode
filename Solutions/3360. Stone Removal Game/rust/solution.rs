impl Solution {
    pub fn can_alice_win(mut n: i32) -> bool {
        let mut result = false;
        for i in (2..=10).rev().step_by(2) {
            n -= i;
            if n >= 0 {
                result = true;
            } else {
                result = false;
                break;
            }
            
            n -= i - 1;
            if n >= 0 {
                result = false;
            } else {
                break;
            }
        }
        result
    }
}