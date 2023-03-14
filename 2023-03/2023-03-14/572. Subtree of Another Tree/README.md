# 572. Subtree of Another Tree

`Easy`

## Description

<p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values of<code> subRoot</code> and <code>false</code> otherwise.</p>

<p>A subtree of a binary tree <code>tree</code> is a tree that consists of a node in <code>tree</code> and all of this node&#39;s descendants. The tree <code>tree</code> could also be considered as a subtree of itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>root</code> tree is in the range <code>[1, 2000]</code>.</li>
	<li>The number of nodes in the <code>subRoot</code> tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code></li>
</ul>


---

### Topic Tags

[tree]: https://img.shields.io/badge/-Tree-EF9A9A
[depth-first-search]: https://img.shields.io/badge/-Depth%20First%20Search-B39DDB
[string-matching]: https://img.shields.io/badge/-String%20Matching-81D4FA
[binary-tree]: https://img.shields.io/badge/-Binary%20Tree-A5D6A7
[hash-function]: https://img.shields.io/badge/-Hash%20Function-FFF59D

![Tree][tree]

![Depth-First Search][depth-first-search]

![String Matching][string-matching]

![Binary Tree][binary-tree]

![Hash Function][hash-function]

---

##### [original question](https://leetcode.com/problems/subtree-of-another-tree)
