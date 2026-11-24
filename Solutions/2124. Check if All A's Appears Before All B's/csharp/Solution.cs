public class Solution {
    public bool CheckString(string s) {
        bool b = false;
        foreach(char v in s)
        {
            if (v == 'b') b = true;
            else if(b == true) return false;
        }
        return true;
    }
}
