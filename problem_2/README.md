You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg">

<pre>
<b>Input:</b> l1 = [2,4,3], l2 = [5,6,4]
<b>Output:</b> [7,0,8]
<b>Explanation:</b> 342 + 465 = 807.
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> l1 = [0], l2 = [0]
<b>Output:</b> [0]
</pre>

<b>Example 3:</b>

<pre>
<b>Input:</b> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<b>Output:</b> [8,9,9,9,0,0,0,1]
</pre>


<b>Constraints:</b>

- The number of nodes in each linked list is in the range <code>[1, 100]</code>.
- <code>0 <= Node.val <= 9</code>
- It is guaranteed that the list represents a number that does not have leading zeros.
