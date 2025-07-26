# Hierarchical Data

## Question

**Sha** asked on 22 Oct 2020

Hi, My data model looks like this, but I'm not sure how to map it to the grid. It gives an error saying it isn't enumerable, which is true. How do I map complex fields as a sub-grid row? public class MainModel { public DetailsModel Order { get; set; } public DetailsModel2 Stuff { get; set; } } public class DetailsModel { public string OrderId { get; set; } public string DealSize { get; set; } } public class DetailsModel2 { public string StuffId { get; set; } public string StuffSize { get; set; } } private List<MainModel> GenerateData() { List<MainModel> data=new List<MainModel>(); for (int i=0; i <5; i++) { MainModel mdl=new MainModel() { Order=new DetailsModel() { OrderId=i.ToString(), DealSize=i.ToString() } , Stuff=new DetailsModel2() { StuffId=i.ToString(), StuffSize=i.ToString() } }; data.Add(mdl); } return data; } <TelerikGrid Data="salesTeamMembers"> <DetailTemplate Context="TemplateItem"> @{ var Item=TemplateItem as MainModel; <TelerikGrid Data="Item.Order" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"></GridColumn> <GridColumn Field="DealSize"></GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Order">Order</GridColumn> <GridColumn Field="Stuff">Stuff</GridColumn> </GridColumns> </TelerikGrid> Thanks!

## Answer

**Marin Bratanov** answered on 23 Oct 2020

Hi Shawn, I suggest you start by reviewing the notes on data binding the grid as they provide a few key aspects: the Field that you point columns to must not be a collection if you want to show data from nested fields, you should point the grid to a particular field in the complex object as explained in the Bind to navigation properties in complex objects article the data of the grid itself must be an IEnumerable collection. This also applies to a grid put in some template, like the DetailTemplate. With the current models, the detail template cannot be a grid, its just one instance of a model. You could, of course, create a collection for that and have a grid with one row. the columns have a field, and templates, but you can't just write text between their tags Another thing to consider is that if you have hierarchical data, perhaps the TreeList component will be more suitable. That said, here's an example that shows the provided models in a grid, I highlighted the changes: <TelerikGrid Data="salesTeamMembers">
<DetailTemplate Context="TemplateItem">
@{ var Item=TemplateItem as MainModel; var GridData=new List<DetailsModel>() { Item.Order }; <TelerikGrid Data=" GridData " Pageable="true" PageSize="5">
<GridColumns>
<GridColumn Field="OrderId"></GridColumn>
<GridColumn Field="DealSize"></GridColumn>
</GridColumns>
</TelerikGrid>
}
</DetailTemplate>
<GridColumns>
<GridColumn Field="Order. OrderId "></GridColumn>
<GridColumn Field="Order.DealSize "></GridColumn>
<GridColumn Field="Stuff.StuffId "></GridColumn>
<GridColumn Field="Stuff.StuffSize "></GridColumn>
</GridColumns>
</TelerikGrid>
@code{
List<MainModel> salesTeamMembers { get; set; } protected override async Task OnInitializedAsync ( ) {
salesTeamMembers=GenerateData();
} public class MainModel { public DetailsModel Order { get; set; } public DetailsModel2 Stuff { get; set; }
} public class DetailsModel { public string OrderId { get; set; } public string DealSize { get; set; }
} public class DetailsModel2 { public string StuffId { get; set; } public string StuffSize { get; set; }
} private List<MainModel> GenerateData ( ) {
List<MainModel> data=new List<MainModel>(); for ( int i=0; i <5; i++)
{
MainModel mdl=new MainModel()
{
Order=new DetailsModel() { OrderId=i.ToString(), DealSize=i.ToString() }
,
Stuff=new DetailsModel2() { StuffId=i.ToString(), StuffSize=i.ToString() }
};
data.Add(mdl);
} return data;
}
} Regards, Marin Bratanov
