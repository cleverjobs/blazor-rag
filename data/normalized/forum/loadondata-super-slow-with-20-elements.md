# LoadOnData super slow with 20 elements

## Question

**Nic** asked on 22 Oct 2019

Hi, I copy paste the code on your example of Treeview and I add 20 nodes with 20 nodes each and when I try to open up one it takes few seconds. My necessity is to have at least 50-100 elements per node and but actually it takes an "eternity" to visualize everything. Both on open and close operations. What can I do to improve the performance? Im using Chrome

## Answer

**Marin Bratanov** answered on 22 Oct 2019

Hello Nicola, This seems to work fine for me. I am attaching at the end of this post a video that shows how this works very quickly for me (and my machine is quite weak). Here's the code I used. If comparing against it does not help, can you modify it to showcase the issue? <TelerikTreeView Data="@HierarchicalData">
<TreeViewBindings>
<TreeViewBinding TextField="Category" ItemsField="Products" />
<TreeViewBinding Level="1" TextField="ProductName" />
</TreeViewBindings>
</TelerikTreeView>

@code { public IEnumerable<ProductCategoryItem> HierarchicalData { get; set; } public class ProductCategoryItem { public string Category { get; set; } public List<ProductItem> Products { get; set; } public bool Expanded { get; set; }
} public class ProductItem { public string ProductName { get; set; } public bool Expanded { get; set; }
} protected override void OnInitialized ( ) {
LoadHierarchical();
} private void LoadHierarchical ( ) {
List<ProductCategoryItem> roots=new List<ProductCategoryItem>(); for ( int i=0; i <20; i++)
{
roots.Add( new ProductCategoryItem
{
Category=$"Category {i} ",
Expanded=false,
Products=new List<ProductItem>()
}); for ( int j=0; j <20; j++)
{
roots[i].Products.Add( new ProductItem { ProductName=$"Category {i} - Product {j} " });
}
}

HierarchicalData=roots;
}
} Regards, Marin Bratanov

### Response

**Nicola** answered on 22 Oct 2019

Hey, thanks for reply. I also try this piece of code but I need more than one subfolder and Im unable to insert more than one subfolder because the TelerikTreeView component has the method OnExpand and then once expand I cant add into it another one with another method OnExpand that call another function! I test it with 100 elements and it works pretty well but as I dont not mentioned before I need more sublevel, like 5 and each five has other 5 and go on. Probably Im not so good but Im sure there is a way to accomplish that, if you can help, I really appreciate it! Right now Im trying to create inside the @code { } block the element TelerikTreeView with no success.

### Response

**Marin Bratanov** answered on 22 Oct 2019

Hi Nicola, The OnExpand event fires every time a node is collapsed or expanded. This allows you to uniquely identify the node based on metadata in the model you use, so you can fetch its children and set them to the child items collection of the item that was just expanded. This can work for more than one level and it is up to the application to distinguish one node from the other. You don't have to use different binding logic and models for the different levels. You must, however, ensure, that you have not disabled the expand arrow by setting the HasChildren field to false (false is the default value for a boolean field). On generating a treeview in the @code section - this is impossible. Blazor does not have a provision for creating components programmatically (we asked a few times). The way to add components in Blazor is to use markup and the Razor tricks it offers - conditional rendering in if-blocks and foreach loops, for example. Regards, Marin Bratanov
