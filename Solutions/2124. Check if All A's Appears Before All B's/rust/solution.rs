impl Solution {
    pub fn check_string(s: String) -> bool {
        let mut b = false;
        for v in s.chars(){
            if v == 'b'{
                b = true;
            } else if b{
                return false;
            }
        }
        true
    }
}
