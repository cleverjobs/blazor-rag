# Blazor TreeView ExpandedItems with Hierarchical data source

## Question

**Bri** asked on 14 Feb 2022

As of 3.01, the ExpandedField property of TreeViewBinding no longer exists and we're meant to bind the ExpandedItems property of the tree view instead. However, this is fine for a flat data source but doesn't really work for a hierarchical data source. I'm loading my hierarchical data source to include all expanded nodes and child nodes so that I can reselect the previously selected node, and this can go down 5 levels or more. So how can I create an expanded items local variable to bind to tree view control from that? The ExpandedField approach worked fine in this scenario, but I don't see how the ExpandedItems approach can. The only way I can see to resolve is to change my hierarchical data source to be flat which would be a lot of work and wouldn't really be ideal. On another matter, the class applied to the selected tree node span element seems to have changed from k-state-selected to k-selected, although I don't see this documented anywhere. Any advice on how I can get round the expanded items problem without drastically rewriting my code would be appreciated.

### Response

**Brian** commented on 15 Feb 2022

Managed to get round this by creating a recursive routine that traverses the hierarchical data source creating a list that contains all of the expanded nodes. Not ideal but it works.

### Response

**Hristian Stefanov** commented on 17 Feb 2022

Hi Brian, I'm glad to hear you've managed to find a working approach for the scenario. Thank you for sharing with us how things turned out. On a side note, there are changes in the rendering of many of our components. You can see the TreeView changes as of 3.0.1 here - " TreeView rendering changes (3.0.1) ".
