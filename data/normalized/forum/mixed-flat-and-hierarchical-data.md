# Mixed flat and hierarchical data

## Question

**Tam** asked on 16 Dec 2020

I have a list of items that I can display in a TreeView as flat data source. Each of these items has a list of other items, more like a hierarchical data source. Is it possible to have a TreeView with mixed flat and hierarchical data in it? I've tried adding another TreeViewBinding, but that didn't work. public class TreeItem { public int Id { get; set; } public string Text { get; set; } public int? Parent { get; set; } public bool HasChildren { get; set; } public bool IsExpanded { get; set; } public List<SubItem> SubItems { get; set; } }

## Answer

**Nadezhda Tacheva** answered on 17 Dec 2020

Hello Tamas, Generally speaking, if a collection of child items is provided in a field of its parent's model that would make the whole data model hierarchical. As it is in your case, a list of Subitems is provided in the last field of the model. If you wish to display the first level not expanded when the page first renders (that will make it look like flat data), you can do the following: Set an "Expanded" bool flag in the model Define its value to "false" when adding the root level element I've created the following example to better illustrate the described scenario: <TelerikTreeView Data="@HierarchicalData">
<TreeViewBindings>
<TreeViewBinding TextField="Category" ItemsField="Products" />
<TreeViewBinding Level="1" TextField="ProductName" />
</TreeViewBindings>
</TelerikTreeView>

@code { public IEnumerable<ProductCategoryItem> HierarchicalData { get; set; } public class ProductCategoryItem { public string Category { get; set; } public List<ProductItem> Products { get; set; } public bool Expanded { get; set; } } public class ProductItem { public string ProductName { get; set; } // the following fields are to denote you can keep having hierarchy further down. They are not required // they are not really used in this example and you would have a collection of child items too // see the information about multiple data bindings earlier in this article on using them public bool Expanded { get; set; }
} protected override void OnInitialized ( ) {
LoadHierarchical();
} private void LoadHierarchical ( ) {
List<ProductCategoryItem> roots=new List<ProductCategoryItem>();

List<ProductItem> firstCategoryProducts=new List<ProductItem>()
{ new ProductItem { ProductName="Category 1 - Product 1" }, new ProductItem { ProductName="Category 1 - Product 2" }, new ProductItem { ProductName="Category 1 - Product 3" }, new ProductItem { ProductName="Category 1 - Product 4" }
};

roots.Add( new ProductCategoryItem
{
Category="Category 1", Expanded=false,
Products=firstCategoryProducts // this is how child items are provided });

roots.Add( new ProductCategoryItem
{
Category="Category 2" // we will set no other properties and it will not have children, nor will it be expanded });

HierarchicalData=roots;
}
} Regards, Nadezhda

### Response

**Tamas** answered on 17 Dec 2020

Hi Nadezhda, Thanks for your response. I might have not expressed myself clearly. Your example shows hierarchical data with the top items not expanded. However, I don't want to make it "look" like I have flat data. I have tree data with parents and children, but in a flat data model ( [https://docs.telerik.com/blazor-ui/components/treelist/data-binding/flat-data](https://docs.telerik.com/blazor-ui/components/treelist/data-binding/flat-data) ). At the leaf nodes of this data model, I would like to add the above mentioned SubItems in a list, just like it would be in a hierarchical data model ( [https://docs.telerik.com/blazor-ui/components/treelist/data-binding/hierarchical-data](https://docs.telerik.com/blazor-ui/components/treelist/data-binding/hierarchical-data) ). So, in fact, I would have a mixed or hybrid of flat and hierarchical data models in my TreeView. Based on your response, it doesn't seem to be possible. In that case, I will just have to convert my data into pure flat or pure hierarchical. Thanks, Tamas

### Response

**Nadezhda Tacheva** answered on 21 Dec 2020

Hi Tamas, Initially, the discussion was regarding the TreeView but I see that you've linked the data binding documentation for the TreeList, so I want to make sure we are on the same page. Generally speaking, both the TreeView and the TreeList behave likewise when it comes to data binding. However, as you have correctly stated, the two types of binding models (flat and hierarchical) cannot be applied simultaneously. When dealing with hierarchical data, a collection of child items is provided in a field of the parent's model and given to the ItemsField parameter. When using flat data, a collection of all items is provided at one level. The displayed hierarchical structure is simulated by checking the Id and ParentId fields and thus defining which are parent and which are child items. Having in mind all of the above, indeed the solution here will be to convert your data into pure flat or pure hierarchical (whichever suits your application better). Regards, Nadezhda
