# Treeview, Hierarchical Data: more than one ItemsField

## Question

**Hei** asked on 20 Jul 2022

I checked the following example: Treeview Data Binding to Hierarchical Data Let's say ProductCategoryItem has a second list, e. g. "Orders". public class ProductCategoryItem { public string Category { get; set; } public List<ProductItem> Products { get; set; } public List<OrderItem> Orders { get; set; }
} public class ProductItem { public string ProductName { get; set; }
} public class OrderItem { public string OrderName { get; set; }
} How can I display this second list "Orders" in TreeView? <TelerikTreeView Data="@HierarchicalData" @bind-ExpandedItems="@ExpandedItems"> <TreeViewBindings> <TreeViewBinding TextField="Category" ItemsField="Products" /> <TreeViewBinding Level="1" TextField="ProductName" />??? <TreeViewBinding TextField="Category" ItemsField="Orders" />??? </TreeViewBindings> </TelerikTreeView> Regards Heiko

## Answer

**Hristian Stefanov** answered on 25 Jul 2022

Hi Heiko, To preserve the structure hierarchy, the Orders list needs to go into the ProductItem model. Every new list needs a separate model and a different hierarchy level. I have prepared an example you can use as a starting point that shows a TreeView Hierarchy configuration in the attached project (see " treeview-hierarchy-configuration-sample.zip "). Please run and test it to see the result. Regards, Hristian Stefanov
