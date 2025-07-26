# Get list of partially checked items from treeview???

## Question

**EdEd** asked on 11 Apr 2022

Hi, I have a need to be able to get partially checked root items. Basically, I want to tell by looking a given child node, who it's root parent is. Is there a way I can tell which are partially checked? Thanks ... Ed

## Answer

**Nadezhda Tacheva** answered on 14 Apr 2022

Hi Ed, The current behavior of the TreeView CheckBox selection if CheckParents is enabled is to mark the parents in indeterminate state when some (not all) of their children are selected. If all the children are checked, the parent will be checked, too. You may test that behavior in the live demo. As far as I can understand, you want to get a list of the parents that are in indeterminate state (partially checked). To do that, you should loop through the data collection and find the parents of the checked items. You may handle the CheckedItemsChanged event of the TreeView to perform that operation. To get only the partially checked items, you should also check if all their children are checked since in this case the parent will also be checked (not partially). It will be easier to achieve the result if you work with flat data collection as you can look for parent id match. I hope you will find the above information useful. Please let us know if any further questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Ed** commented on 14 Apr 2022

Understood. I was just trying to be lazy and see if someone had already written that kind of code. Thanks. Just remember, that in order to understand recursion, you must first understand recursion.
