# How to Increase the width of telerik nested grid collapsible column?

## Question

**Noa** asked on 13 Nov 2024

I want to increase the width of the collapsible column in the telerik nested grid. I’ve tried to do it with CSS and JavaScript, but it hasn't worked. Could someone help me increase the width of this class k-hierarchy-cell? <TelerikGrid Data="categories" Pageable="true" PageSize="5" Class="custom-nested-grid"> <DetailTemplate Context="categoryItem"> @{
var category=categoryItem as CategoryModel; <TelerikGrid Data="category.SubItems" Pageable="true" PageSize="3" Class="nested-grid"> <DetailTemplate Context="subItem"> @{
var nestedItem=subItem as SubItemModel; <TelerikGrid Data="nestedItem.NestedItems" Pageable="true" PageSize="3" Class="nested-grid"> <DetailTemplate Context="nestedSubItem"> @{
// Add a fourth level of nesting here if needed
} </DetailTemplate> <GridColumns> <GridColumn Field="Code" Title="Code"> </GridColumn> <GridColumn Field="Name" Title="Name"> </GridColumn> <GridColumn Field="Description" Title="Description"> </GridColumn> <GridColumn Field="ItemType" Title="Item Type"> </GridColumn> <GridColumn Field="LinkedCategories" Title="Linked Categories"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Code" Title="Code"> </GridColumn> <GridColumn Field="Name" Title="Name"> </GridColumn> <GridColumn Field="Description" Title="Description"> </GridColumn> <GridColumn Field="ItemType" Title="Item Type"> </GridColumn> <GridColumn Field="LinkedCategories" Title="Linked Categories"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Code" Title="Code"> </GridColumn> <GridColumn Field="Name" Title="Name"> </GridColumn> <GridColumn Field="Description" Title="Description"> </GridColumn> <GridColumn Field="ItemType" Title="Item Type"> </GridColumn> <GridColumn Field="LinkedCategories" Title="Linked Categories"> </GridColumn> </GridColumns> </TelerikGrid> @code {
// Sample data model classes
public class CategoryModel
{
public string Code { get; set; }
public string Name { get; set; }
public string Description { get; set; }
public string ItemType { get; set; }
public string LinkedCategories { get; set; }
public List <SubItemModel> SubItems { get; set; }
}

public class SubItemModel
{
public string Code { get; set; }
public string Name { get; set; }
public string Description { get; set; }
public string ItemType { get; set; }
public string LinkedCategories { get; set; }
public List <NestedItemModel> NestedItems { get; set; }
}

public class NestedItemModel
{
public string Code { get; set; }
public string Name { get; set; }
public string Description { get; set; }
public string ItemType { get; set; }
public string LinkedCategories { get; set; }

// Add this property to support further nesting
public List <NestedItemModel> NestedItems { get; set; }=new List <NestedItemModel> ();
}

private List <CategoryModel> categories=new List <CategoryModel> {
new CategoryModel
{
Code="C-1", Name="Ram Pro Master 2500", Description="Ambulance parts for ram pro master 2500", ItemType="Parts", LinkedCategories="8 Linked categories",
SubItems=new List <SubItemModel> {
new SubItemModel
{
Code="C-134", Name="Electronic Control Unit", Description="Electric parts for ram pro master 3500", ItemType="-", LinkedCategories="4 Linked categories",
NestedItems=new List <NestedItemModel> {
new NestedItemModel
{
Code="N-1", Name="Subcomponent A", Description="Details for subcomponent A", ItemType="Electronic", LinkedCategories="2 Linked categories",
// Next level of data
NestedItems=new List <NestedItemModel> {
new NestedItemModel { Code="L-1", Name="Detail A1", Description="Details of A1", ItemType="Part", LinkedCategories="-",
NestedItems=new List <NestedItemModel> {
new NestedItemModel { Code="L-1", Name="Detail A1", Description="Details of A1", ItemType="Part", LinkedCategories="-" },
new NestedItemModel { Code="L-2", Name="Detail A2", Description="Details of A2", ItemType="Part", LinkedCategories="Linked" }
}
},
new NestedItemModel { Code="L-2", Name="Detail A2", Description="Details of A2", ItemType="Part", LinkedCategories="Linked" }
}
},
new NestedItemModel
{
Code="N-2", Name="Subcomponent B", Description="Details for subcomponent B", ItemType="Electronic", LinkedCategories="1 Linked category",
NestedItems=new List <NestedItemModel> {
new NestedItemModel { Code="L-3", Name="Detail B1", Description="Details of B1", ItemType="Part", LinkedCategories="-" }
}
}
}
}
}
},
new CategoryModel
{
Code="C-2", Name="Ram Pro Master 3500", Description="Electric parts for ram pro master 3500", ItemType="Parts", LinkedCategories="5 Linked categories",
SubItems=new List <SubItemModel> {
new SubItemModel
{
Code="C-672", Name="Engine Control Unit", Description="Engine module for control", ItemType="-", LinkedCategories="3 Linked categories",
NestedItems=new List <NestedItemModel> {
new NestedItemModel
{
Code="N-3", Name="Engine Subcomponent A", Description="Engine details A", ItemType="Engine Part", LinkedCategories="-",
NestedItems=new List <NestedItemModel> {
new NestedItemModel { Code="L-4", Name="Detail C1", Description="Details of C1", ItemType="Control Unit", LinkedCategories="-" },
new NestedItemModel { Code="L-5", Name="Detail C2", Description="Details of C2", ItemType="Control Unit", LinkedCategories="Linked" }
}
}
}
}
}
}
};

private void ApplyCategory(CategoryModel category)
{
Console.WriteLine($"Applying category: {category.Code}");
}

private void ApplySubItem(CategoryModel category, SubItemModel subItem)
{
Console.WriteLine($"Applying sub-item: {subItem.Code} under category: {category.Code}");
}
private TelerikGrid <CategoryModel> gridRef;

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
await JSRuntime.InvokeVoidAsync("setHierarchyCellWidth", 130); // Set the desired width here
}
}
} <script> window. setHierarchyCellWidth=function ( width ) { document. querySelectorAll ( ".k-hierarchy-cell" ). forEach ( cell=> {
cell. style. width=width + "px";
cell. style. minWidth=width + "px";
cell. style. maxWidth=width + "px";
});
} </script>

## Answer

**Dimo** answered on 14 Nov 2024

Hi Noam, Please target the <col> tags instead of the <td> tags. The Grid always applies column widths to the <col> s. <style>.k-grid col.k-hierarchy-col { width: 64px; /* default is 32px; */ } </style> <TelerikGrid Data="@GridData"> <GridColumns> <GridColumn Field="@nameof(SampleModel.Name)" /> </GridColumns> <DetailTemplate> Detail Template for item @context.Name </DetailTemplate> </TelerikGrid> @code {
private List<SampleModel> GridData { get; set; }=new ();

protected override void OnInitialized ( ) { for (int i=1; i <=7; i++)
{
GridData.Add( new SampleModel ( ) {
Id=i,
Name=$ "Name {i}",
});
}
}

public class SampleModel {
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
}
} Regards, Dimo Progress Telerik
