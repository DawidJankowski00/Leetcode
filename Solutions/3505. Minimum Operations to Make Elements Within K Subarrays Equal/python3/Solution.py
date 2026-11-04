def compute_window_costs(elements: List[int], span: int) -> List[int]:
    half_len = span // 2
    is_odd = span & 1
    
    ordered_elements = SortedList(elements[:span])
    lower_half_sum = sum(ordered_elements[:half_len])
    window_sum = sum(elements[:span])

    def get_current_cost() -> int:
        return window_sum - 2 * lower_half_sum - is_odd * ordered_elements[half_len]

    all_costs = [get_current_cost()]

    for leaving_val, entering_val in zip(elements, elements[span:]):
        if entering_val < ordered_elements[half_len - 1]:
            lower_half_sum += entering_val - ordered_elements[half_len - 1]
        ordered_elements.add(entering_val)

        if leaving_val <= ordered_elements[half_len - 1]:
            lower_half_sum += ordered_elements[half_len] - leaving_val
        ordered_elements.remove(leaving_val)

        window_sum += entering_val - leaving_val
        all_costs.append(get_current_cost())

    return all_costs


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        window_penalties = compute_window_costs(nums, x)
        dp_state = [0] * (len(nums) + 1)
        
        for _ in range(k):
            dp_state = list(
                accumulate(
                    [inf] * x + [prev_dp + penalty for prev_dp, penalty in zip(dp_state, window_penalties)],
                    min
                )
            )
            
        return dp_state[-1]