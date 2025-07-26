# Iconfield in ItemTemplate

## Question

**Rob** asked on 03 Apr 2020

Based on this thread: [https://www.telerik.com/forums/bind-style-based-on-selected-node](https://www.telerik.com/forums/bind-style-based-on-selected-node) I am able to get a selected node. Demos shown treeview bindings without ItemTemplate. I use: <TreeViewBinding IdField="Id" ParentIdField="ParentIdValue" ExpandedField="Expanded" TextField="Text" HasChildrenField="HasChildren" IconField="Icon" UrlField="Url" /> This results in a treeview with icons. How can I have the same result using an ItemTemplate?

## Answer

**Svetoslav Dimitrov** answered on 03 Apr 2020

Hello Robby, It is possible to achieve similar behavior and styling by using ItemTemplate for the Treeview. What you can do is use the img tag inside the ItemTemplate and provide the src and alt (if needed). Or, you could use the font icons we provide as a separate component: [https://docs.telerik.com/blazor-ui/common-features/font-icons](https://docs.telerik.com/blazor-ui/common-features/font-icons) A working demo that showcases the things described above can be seen in our docs for the Treeview component under the Templates article, link here: [https://docs.telerik.com/blazor-ui/components/treeview/templates.](https://docs.telerik.com/blazor-ui/components/treeview/templates.) The example that will suit your usecase is the last one in the article, titled Different templates for different node levels. Regards, Svetoslav Dimitrov
