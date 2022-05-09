# 124. Binary Tree Maximum Path Sum

`Hard`

## Description

<p>A <strong>path</strong> in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence <strong>at most once</strong>. Note that the path does not need to pass through the root.</p>

<p>The <strong>path sum</strong> of a path is the sum of the node&#39;s values in the path.</p>

<p>Given the <code>root</code> of a binary tree, return <em>the maximum <strong>path sum</strong> of any <strong>non-empty</strong> path</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The optimal path is 2 -&gt; 1 -&gt; 3 with a path sum of 2 + 1 + 3 = 6.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" />
<pre>
<strong>Input:</strong> root = [-10,9,20,null,null,15,7]
<strong>Output:</strong> 42
<strong>Explanation:</strong> The optimal path is 15 -&gt; 20 -&gt; 7 with a path sum of 15 + 20 + 7 = 42.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


---

### Topic Tags

[dynamic-programming]: https://img.shields.io/badge/-Dynamic%20Programming-EF9A9A
[tree]: https://img.shields.io/badge/-Tree-B39DDB
[depth-first-search]: https://img.shields.io/badge/-Depth%20First%20Search-81D4FA
[binary-tree]: https://img.shields.io/badge/-Binary%20Tree-A5D6A7

![Dynamic Programming][dynamic-programming]

![Tree][tree]

![Depth-First Search][depth-first-search]

![Binary Tree][binary-tree]

---

##### [original question](https://leetcode.com/problems/binary-tree-maximum-path-sum)
