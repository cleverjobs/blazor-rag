# Hide TreeView CheckBoxes on parent nodes

## Question

**Ila** asked on 08 Jun 2022

Is there a way to show the checkboxes (on TreeViewCheckBoxMode.Multiple) only on child nodes?

## Answer

**Dimo** answered on 13 Jun 2022

Hi Ilan, The easiest approach is to hide checkboxes in root items with CSS: <TelerikTreeView Class="root-checkboxes" /> <style>.root-checkboxes> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox { display: none;
} </style> The above approach is not suitable if: You want only the innermost (leaf) TreeView nodes to render checkboxes. Each root TreeView node has unknown number of nested levels. In this case you will have to use custom checkboxes inside an ItemTemplate, instead of the built-in checkboxes. If you need checkboxes for the leaf nodes only, and the number of levels is known, then the above CSS rule can be tweaked to hide the checkboxes at several levels: For version 3.6.0 and later: /* root items */.root-checkboxes> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox, /* first level children */.root-checkboxes> ul> li> div> div> div> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox, /* second level children */.root-checkboxes> ul> li> div> div> div> ul> li> div> div> div> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox { display: none;
} For version 3.5.0 and earlier, use one <div> less: /* root items */.root-checkboxes> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox, /* first level children */.root-checkboxes> ul> li> div> div> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox, /* second level children */.root-checkboxes> ul> li> div> div> ul> li> div> div> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox { display: none;
} Regards, Dimo Progress Telerik

### Response

**Ilan** commented on 14 Jun 2022

Can you please provide a sample for custom checkboxes? the other options won't work for me

### Response

**Dimo** commented on 15 Jun 2022

@Ilan - the implementation of custom checkboxes inside a TreeView ItemTemplate is independent of the TreeView API - it depends entirely on the business logic and your coding preferences. We can assist with tailor-made development in such scenarios as part of our separate offering - Professional Services. Let me know if you are interested.

### Response

**Doug** commented on 03 Nov 2022

In the first level children example (and I imagine in the second level as well) I needed a third div but otherwise it worked:.root-checkboxes> ul> li> div> div> div> ul> li> div:first -child.k-checkbox-wrapper>.k-checkbox,

### Response

**Dimo** commented on 04 Nov 2022

Yes, Doug, you are right - the additional "div" is necessary for version 3.6.0 and later. I updated my post.

### Response

**Doug** commented on 04 Nov 2022

I think this illustrates the downside of a solution like this. It effectively creates a breaking change from one version to the next.

### Response

**Ilan** commented on 04 Nov 2022

Telerik should had a property that does that on rendering

### Response

**Dimo** commented on 04 Nov 2022

We have a public feature request for disabled checkboxes for parent nodes. If this alternative will work for you, please vote for it. Otherwise, you can submit another one and describe your use case, so that other developers can vote too.

### Response

**Ilan** commented on 04 Nov 2022

Would like ShowParentNodesCheck="false"

### Response

**Dustin** commented on 13 Jun 2024

I wasn't able to get the above approach to work. But this worked for me. I set "display: none" for the whole treeview, and then dig into the level I want and set "display: block"..Dustins-treeview .k-checkbox-wrap { display: none; } .Dustins-treeview .k-treeview-lines .k-treeview-group .k-treeview-item .k-animation-container .k-checkbox-wrap { display: block; }
