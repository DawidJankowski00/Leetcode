impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut result = 0;
        for i in (0..bytes.len().saturating_sub(1)).step_by(2){
            if bytes[i] != bytes[i+1]{
                result +=1;
            }
        }
        result
    }
}
