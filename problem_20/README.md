Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


<b>Example 1:</b>

<pre>
<b>Input:</b> s = "()"
<b>Output:</b> true
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> s = "()[]{}"
<b>Output:</b> true
</pre>

<b>Example 3:</b>

<pre>
<b>Input:</b> s = "(]"
<b>Output:</b> false
</pre>


<b>Constraints:</b>

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.
