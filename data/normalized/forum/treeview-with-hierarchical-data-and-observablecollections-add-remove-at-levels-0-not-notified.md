# TreeView with hierarchical data and ObservableCollections: Add/Remove at Levels > 0 not notified

## Question

**Jen** asked on 31 Mar 2022

I have a TreeView with 2 Levels (I changed your RefreshData example to work with 2 levels and ObservableCollections): <h3> TreeView </h3> Hierarchical data hold collections of the child items <TelerikButton OnClick="@AddRoot"> Add root </TelerikButton> <TelerikButton OnClick="@AddItem"> Add child </TelerikButton> <TelerikButton OnClick="@RemoveItem"> Remove child </TelerikButton> <TelerikTreeView Data="@HierarchicalData" @bind-ExpandedItems="@ExpandedItems"> <TreeViewBindings> <TreeViewBinding TextField="Category" ItemsField="Products" /> <TreeViewBinding Level="1" TextField="ProductName" /> </TreeViewBindings> </TelerikTreeView> @code {
public IList <ProductCategoryItem> HierarchicalData { get; set; }
public IEnumerable <object> ExpandedItems { get; set; }=new List <object> ();

void AddItem()
{
var firstItem=HierarchicalData.First();
firstItem.Products.Add(
new ProductItem
{
ProductName="New Item"
});

StateHasChanged();
}

void AddRoot()
{
HierarchicalData.Add(new ProductCategoryItem { Category="New Category" });

StateHasChanged();
}

void RemoveItem()
{
var firstItem=HierarchicalData.First();
if (firstItem.Products.Count> 0)
{
firstItem.Products.RemoveAt(firstItem.Products
.IndexOf(firstItem.Products.Last()));

StateHasChanged();
}
}

public class ProductCategoryItem
{
public string Category { get; set; }
public IList <ProductItem> Products { get; set; }
}

public class ProductItem
{
public string ProductName { get; set; }
}

protected override void OnInitialized()
{
LoadHierarchical();
ExpandedItems=HierarchicalData.Where(x=> x.Products !=null && x.Products.Any()).ToList();
}

private void LoadHierarchical()
{
var roots=new ObservableCollection <ProductCategoryItem> ();

var firstCategoryProducts=new ObservableCollection <ProductItem> ()
{
new ProductItem { ProductName="Category 1 - Product 1" },
new ProductItem { ProductName="Category 1 - Product 2" }
};

roots.Add(new ProductCategoryItem
{
Category="Category 1",
Products=firstCategoryProducts // this is how child items are provided

});

roots.Add(new ProductCategoryItem
{
Category="Category 2" // we will set no other properties and it will not have children, nor will it be expanded
});

HierarchicalData=roots;
}
} If I "add child" then the TreeView is not updated, Even after collapsing and re-expanding the root node, the newly added child item is not shown. Notification works only on the first level ("add root") which also updates the child items.

## Answer

**Svetoslav Dimitrov** answered on 05 Apr 2022

Hello Jens, Changing an item in a nested collection would not pre-render the TreeView, in the AddItem method, I would suggest you change the reference of the collection bound to the TreeView: HierarchicalData=new ObservableCollection <ProductCategoryItem> (HierarchicalData); Here is the updated REPL link, where you can run the sample and experiment with it. Regards, Svetoslav Dimitrov
