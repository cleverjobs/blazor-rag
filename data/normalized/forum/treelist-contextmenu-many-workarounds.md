# TreeList + ContextMenu = many workarounds

## Question

**Bla** asked on 22 Apr 2022

I am adding a context menu to the treelist. The issue is that I have not achieved a good integration between them. Especially for display issues I had to do a lot of workarounds. I attach a code snipet as an example: Examples As you can see in the Example 1, inside the green area you can right click and it shows the context menu, but outside this (the largest area) it doesn't. If we replace the <span> with a <div> now the green area will be larger but the button to expand is not on the same line. So we have to apply styles (for example: display: flex;) to the element that wraps our template (Example 2). Now the new issue is that the treelist loader (the one that is seen when we expand a parent node) looks stretched (Example 3). I find it hard to believe that the integration is so complicated. I am doing something wrong?? Regards. Ludwig.

### Response

**Blazorist** commented on 09 May 2022

The example was updated in order to clarify the problem.
