# Markdown特殊字符

## Markdown表格数学公式中使用绝对值“| |”或竖杠"|"

一个\vert就能解决的问题。
1. 由于Markdown表格通过|来定义，因此不能直接用|写绝对值或竖杠；
2. 简单公式不用 KaTeX，可通过转义符\|或&#124;;来实现竖杠或绝对值；
3. KATEX会把\|显示为"∥"，而&#124;会报错，故不能直接用“2”中的方式写；
4. 网上的一种解决方案是把KaTeXX公式拆分，但是这种方案不仅复杂且仅适于简单公式；
5. 事实上，仅使用\vert就能完美解决Markdown表格数学公式中使用竖杠的问题；
6. \lvert，\rvert和\vert无显示差别，仅用于在表意上做区分。

多数博客系统Markdown写作中支持 KaTeX ($\KaTeX$)数学公式. （KaTeX的阉割Web版，有老前辈MathJax）。
[KaTeX](https://katex.org/docs/supported.html)的官方文档全面清晰适合速查。

## markdown 如何在代码块内输入 "<code>`</code>"

```
<code>`</code>
```

