Given an array of integers <code>nums</code> and an integer <code>target</code>, return <i>indices of the two numbers such that they add up</i> to <code><i>target</i></code>.

You may assume that each input would have <strong><i>exactly</i> one solution</strong>, and you may not use the <i>same</i> element twice.

You can return the answer in any order.


<b>Example 1:</b>

<pre>
<b>Input:</b> nums = [2,7,11,15], target = 9
<b>Output:</b> [0,1]
<b>Explanation:</b> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> nums = [3,2,4], target = 6
<b>Output:</b> [1,2]
</pre>

<b>Example 3:</b>

<pre>
<b>Input:</b> nums = [3,3], target = 6
<b>Output:</b> [0,1]
</pre>


<b>Constraints:</b>

- <code>2 <= nums.length <= 104</code>
- <code>-109 <= nums[i] <= 109</code>
- <code>-109 <= target <= 109</code>
- <b>Only one valid answer exists.</b>


<b>Follow-up:</b> Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code> time complexity?
