# Two way Binding to TreeNode properties

## Question

**And** asked on 26 Feb 2022

Depending if my folder is expanded or not I may want to display a different icon. Or I might want one of my leaf tree nodes should show a different look because of an external state change (e.g. IsDirty so add an asterisk to the text and make it red.) Changing the bound IconClass property of the tree node doesn't update the tree. If I update the property, I can't find a way to tell the tree to re-render that node. My only working example is to reset the tree data with a new copy of the tree data list. However this looks very awkward in the example of a tree node expand/collapse. The node expands and then about a second later the icon changes to an open folder. Any other options available? -Andy

## Answer

**Dimo** answered on 02 Mar 2022

Hi Andrew, Your observation is correct and refreshing the data instance is the current way to go. There is a feature request to track TreeView item property changes, which can provide different options in such scenarios, depending on how exactly we implement it. Regards, Dimo Progress Telerik
