# Checkboxes pain

## Question

**EdEd** asked on 08 Apr 2021

Hi. For the life of me, I can't figure out how to programmatically check checkboxes on a treeview loaded with hiearchical data. I've even tried setting the CheckedItems=StoreageItems, using your example. I must be missing some magic sauce. The treeview comes up just fine. I just can't precheck items. Help!!!! <TelerikTreeView Data="@tvData" CheckBoxMode="TreeViewCheckBoxMode.Multiple" @bind-CheckedItems="@CheckedItems" CheckParents="true" CheckChildren="true" OnExpand="@OnExpand"> <TreeViewBindings> <TreeViewBinding IdField="CategoryId" ParentIdField="ParentItemId" ItemsField="Items" HasChildrenField="HasChildren" TextField="CategoryName" IconField="Icon"> </TreeViewBinding> <TreeViewBinding Level="1" TextField="CategoryName" /> </TreeViewBindings> </TelerikTreeView> public IEnumerable<object> CheckedItems { get; set; } public TreeViewCheckBoxMode CheckBoxMode { get; set; }=TreeViewCheckBoxMode.Multiple; public void LoadtvRootData() { List<CategoryItem> lst=new List<CategoryItem>(); // data requested and received for a certain node var q=from a in db.Categories where a.IsActive==true && a.SubscriberId==appData.AppUser.Id && a.ParentCategoryId==null orderby a.CategoryName select a; var lst1=q.ToList(); foreach(var item in lst1) { CategoryItem ci=new CategoryItem(item); var q1=from a in db.Categories where a.ParentCategoryId==item.Id select new CategoryItem(a) { Category=a, HasChildren=ATDBContext.udfCategoryHasChildren(a.Id), }; ci.Items=q1.ToList(); ci.HasChildren=ci.Items.Count> 0; ci.Category=item; lst.Add(ci); } tvData=new List<CategoryItem>(lst); CheckedItems=tvData; }

## Answer

**Svetoslav Dimitrov** answered on 13 Apr 2021

Hello Ed, In order to select not only the parent nodes in the TreeView but also the child items, you would need to traverse through the collection of child items and check the desired child by a certain condition. Below, I have made an example that you can use as a base in your own application: <TelerikTreeView Data="@HierarchicalData" CheckBoxMode="@TreeViewCheckBoxMode.Multiple" CheckedItems="@CheckedItems">
<TreeViewBindings>
<TreeViewBinding TextField="Category" ItemsField="Products" />
<TreeViewBinding Level="1" TextField="ProductName" />
</TreeViewBindings>
</TelerikTreeView>

@code { public IEnumerable<ProductCategoryItem> HierarchicalData { get; set; } public IEnumerable <object> CheckedItems { get; set; }=new List<object>(); public class ProductCategoryItem { public string Category { get; set; } public List<ProductItem> Products { get; set; } public bool Expanded { get; set; }
} public class ProductItem { public string ProductName { get; set; } // the following fields are to denote you can keep having hierarchy further down. They are not required // they are not really used in this example and you would have a collection of child items too // see the information about multiple data bindings earlier in this article on using them public bool Expanded { get; set; }
} private List<object> CheckItems ( IEnumerable<ProductCategoryItem> collection, string productName ) {
List<object> checkedItems=new List<object>(); foreach ( var item in collection)
{
checkedItems.Add(item); if (item.Products?.Count> 0 )
{ foreach ( var child in item.Products)
{ if (child.ProductName.Equals(productName))
{
checkedItems.Add(child);
}
}
}

} return checkedItems;
} protected override void OnInitialized ( ) {
LoadHierarchical(); CheckedItems=CheckItems(HierarchicalData, "Category 1 - Product 2" ); } private void LoadHierarchical ( ) {
List<ProductCategoryItem> roots=new List<ProductCategoryItem>();

List<ProductItem> firstCategoryProducts=new List<ProductItem>()
{ new ProductItem { ProductName="Category 1 - Product 1" }, new ProductItem { ProductName="Category 1 - Product 2" }
};

roots.Add( new ProductCategoryItem
{
Category="Category 1",
Expanded=true,
Products=firstCategoryProducts // this is how child items are provided });

roots.Add( new ProductCategoryItem
{
Category="Category 2" // we will set no other properties and it will not have children, nor will it be expanded });

HierarchicalData=roots;
}
} Regards, Svetoslav Dimitrov Progress Telerik
