Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is palindrome integer.

An integer is a <strong>palindrome</strong> when it reads the same backward as forward.
- For example, 121 is a palindrome while 123 is not.


<b>Example 1:</b>

<pre>
<b>Input:</b> x = 121
<b>Output:</b> true
<b>Explanation:</b> 121 reads as 121 from left to right and from right to left.
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> x = -121
<b>Output:</b> false
<b>Explanation:</b> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<b>Example 3:</b>

<pre>
<b>Input:</b> x = 10
<b>Output:</b> false
<b>Explanation:</b> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>


<b>Constraints:</b>

- <code>-231 <= x <= 231 - 1</code>


<b>Follow up:</b> Could you solve it without converting the integer to a string?
