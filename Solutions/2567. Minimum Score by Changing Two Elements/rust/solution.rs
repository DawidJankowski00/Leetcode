impl Solution {
    pub fn minimize_sum(nums: Vec<i32>) -> i32 {
        if nums.len() == 3 {
            return 0;
        }

        let (mut min1, mut min2, mut min3) = (i32::MAX, i32::MAX, i32::MAX);
        let (mut max1, mut max2, mut max3) = (i32::MIN, i32::MIN, i32::MIN);

        for num in nums {
            if num <= min1 {
                min3 = min2;
                min2 = min1;
                min1 = num;
            } else if num <= min2 {
                min3 = min2;
                min2 = num;
            } else if num < min3 {
                min3 = num;
            }

            if num >= max1 {
                max3 = max2;
                max2 = max1;
                max1 = num;
            } else if num >= max2 {
                max3 = max2;
                max2 = num;
            } else if num > max3 {
                max3 = num;
            }
        }

        let a = max1 - min3;
        let b = max2 - min2;
        let c = max3 - min1;

        a.min(b).min(c)
    }
}
