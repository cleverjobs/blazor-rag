# Is there a grid setting to not show the expander column completely?

## Question

**joh** asked on 14 May 2021

I figured out a way to hide the expander icon during the onRowRender. I've tried different css routes using style which does no consistently hide the column .k-grid k-hierarchy-col (etc.). Is there a setting / way to onRowRender hide this column completely? I am using a context menu to expand and feel it is taking up space on screen.

## Answer

**Marin Bratanov** answered on 18 May 2021

Hello John, You can use CSS to hide those elements from the grid, like so: <style>.no-expand-column.k-grid-content colgroup col:first-of-type,.no-expand-column.k-grid-header thead th:first-of-type,.no-expand-column.k-grid-header colgroup col:first-of-type { width: 0px;
}.no-expand-column.k-grid-content td.k-hierarchy-cell * { display: none;
} </style> <TelerikGrid Class="no-expand-column" Data="salesTeamMembers"> <DetailTemplate> @{
var employee=context as MainModel; <TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"> </GridColumn> <GridColumn Field="Name"> </GridColumn> </GridColumns> </TelerikGrid> @code {
List <MainModel> salesTeamMembers { get; set; }

protected override void OnInitialized()
{
salesTeamMembers=GenerateData();
}

private List <MainModel> GenerateData()
{
List <MainModel> data=new List <MainModel> ();
for (int i=0; i <5; i ++)
{ MainModel mdl=new MainModel { Id=i, Name=$ " Name { i }" }; mdl.Orders=Enumerable.Range(1, 15 ).Select ( x=> new DetailsModel { OrderId=x, DealSize=x ^ i }).ToList();
data.Add(mdl);
}
return data;
}

public class MainModel
{
public int Id { get; set; }
public string Name { get; set; }
public List <DetailsModel> Orders { get; set; }
}

public class DetailsModel
{
public int OrderId { get; set; }
public double DealSize { get; set; }
}
} Regards, Marin Bratanov

### Response

**johnbolt** commented on 18 May 2021

Thank you. This worked for me 100%. Previously, I was able to hide a lot of things, but not the column itself.

### Response

**Marin Bratanov** commented on 18 May 2021

Glad I could help!

### Response

**pihi** commented on 21 Mar 2022

Hello, there is a issue with this solution: When performing manual column resize with FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" first column disappear. <style> .no-expand-column.k-grid-content colgroup col:first-of-type, .no-expand-column.k-grid-header thead th:first-of-type, .no-expand-column.k-grid-header colgroup col:first-of-type { width: 0px; } .no-expand-column.k-grid-content td.k-hierarchy-cell * { display: none; } </style> <TelerikGrid FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Class="no-expand-column" Data="salesTeamMembers" Pageable="true" Sortable="true" Groupable="false" Resizable="true" Reorderable="true"> <DetailTemplate> @{ var employee=context as MainModel; <TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Name"></GridColumn> </GridColumns> </TelerikGrid> <TelerikGrid Class="no-expand-column" Data="salesTeamMembers" Pageable="true" Sortable="true" Groupable="false" Resizable="true" Reorderable="true"> <DetailTemplate> @{ var employee=context as MainModel; <TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Name"></GridColumn> </GridColumns> </TelerikGrid> @code { List <MainModel> salesTeamMembers { get; set; } protected override void OnInitialized() { salesTeamMembers=GenerateData(); } private List <MainModel> GenerateData() { List <MainModel> data=new List <MainModel> (); for (int i=0; i <5; i++) { MainModel mdl=new MainModel { Id=i, Name=$"Name {i}" }; mdl.Orders=Enumerable.Range(1, 15).Select(x=> new DetailsModel { OrderId=x, DealSize=x ^ i }).ToList(); data.Add(mdl); } return data; } public class MainModel { public int Id { get; set; } public string Name { get; set; } public List <DetailsModel> Orders { get; set; } } public class DetailsModel { public int OrderId { get; set; } public double DealSize { get; set; } } }

### Response

**Dimo** commented on 24 Mar 2022

@pihi - this is a bug and I logged it in our public portal on your behalf. I experimented to find a workaround, but I am afraid I didn't find one. Your only option is to bring back the expand column. However, you can still hide the [ + ] and [ - ] icons in it, so that users cannot control the hierarchy.
