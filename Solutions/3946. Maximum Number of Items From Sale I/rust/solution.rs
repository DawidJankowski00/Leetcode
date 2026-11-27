impl Solution {
    pub fn maximum_sale_items(items: Vec<Vec<i32>>, budget: i32) -> i32 {
        let n = items.len();
        let budget = budget as usize;
        let mut frees = vec![0i32; n];

        for i in 0..n {
            let fi = items[i][0];
            let mut cnt = 0;
            for j in 0..n {
                if i != j && items[j][0] % fi == 0 {
                    cnt += 1;
                }
            }
            frees[i] = cnt;
        }

        let mut dp = vec![0i32; budget + 1];

        for i in 0..n {
            let price = items[i][1] as usize;
            let free = frees[i];
            if price > budget {
                continue;
            }

            for b in (price..=budget).rev() {
                if dp[b - price] + 1 + free > dp[b] {
                    dp[b] = dp[b - price] + 1 + free;
                }
            }

            for b in price..=budget {
                if dp[b - price] + 1 > dp[b] {
                    dp[b] = dp[b - price] + 1;
                }
            }
        }

        dp[budget]
    }
}