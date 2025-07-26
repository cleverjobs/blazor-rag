# Avoid Collapse / Expand for specific items

## Question

**Chr** asked on 16 Mar 2022

Hello, is there a way to avoid collapsing and/or expanding tree items depending on the value of a property from the data model ? Additionally a feature request would be helpful: E.g. Model: class Node { public int Id { get; set;} public int ParentId { get; set;} public string Name { get; set;} public bool IsExpanded { get; set;} public bool IsCollapsed { get; set;} public bool CanExpanded { get; set;} public bool CanCollapsed { get; set;}
} Bind properties IsExpanded/IsCollapsed to the tree=> OnInitial render the node is expanded/collapsed Bind properites CanExpanded/CanCollapsed to the tree=> able to expand/collapse a tree node (and render the indicator differently)

## Answer

**Marin Bratanov** answered on 19 Mar 2022

Hello, The HasChildren field controls whether an item can be expanded/collapsed, if it is set to false there will be no expand arrow. You can read more about this (there are a few considerations about this) in this article: [https://docs.telerik.com/blazor-ui/components/treelist/data-binding/overview](https://docs.telerik.com/blazor-ui/components/treelist/data-binding/overview) You can use its state to also know when something happens: [https://docs.telerik.com/blazor-ui/components/treelist/state](https://docs.telerik.com/blazor-ui/components/treelist/state) - please go through the article as it opens up lots of possibilities - for example, see the StateChanged event and the "Get The User Action That Changes The TreeList" and "Set Default (Initial) State" sections. You can control which items are expanded/collapsed, you can set them on initial load and change what the user does by setting a new state based on the business logic you need to implement. Regards, Marin Bratanov
