Roman numerals are represented by seven different symbols: <code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.

<pre>
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</pre>

For example, <code>2</code> is written as <code>II</code> in Roman numeral, just two ones added together. <code>12</code> is written as <code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:

- <code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.
- <code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.
- <code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.


<b>Example 1:</b>

<pre>
<b>Input:</b> s = "III"
<b>Output:</b> 3
<b>Explanation:</b> III = 3.
</pre>

<b>Example 2:</b>

<pre>
<b>Input:</b> s = "LVIII"
<b>Output:</b> 58
<b>Explanation:</b> L = 50, V= 5, III = 3.
</pre>

<b>Example 3:</b>

<pre>
<b>Input:</b> s = "MCMXCIV"
<b>Output:</b> 1994
<b>Explanation:</b> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>


<b>Constraints:</b>

- <code>1 <= s.length <= 15</code>
- <code>s</code> contains only the characters <code>('I', 'V', 'X', 'L', 'C', 'D', 'M')</code>.
- It is <strong>guaranteed</strong> that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.
