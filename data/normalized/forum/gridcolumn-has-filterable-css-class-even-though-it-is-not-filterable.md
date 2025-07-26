# GridColumn has filterable css-class even though it is not filterable

## Question

**Arm** asked on 08 Nov 2021

Hi! My grid data is ExpandoObjects. The grid has ShowColumnMenu set to true, FilterMode set to GridFilterMode.FilterMenu and FilterMenuType set to FilterMenuType.CheckBoxList. I am defining a bunch of GridColumn by looping a list. When defining these i set the Filterable parameter to false. But the th element still has the k-filterable css class, which add the extra padding to the right. How do I get rid of the extra padding in my headers? Here's a peek of my code: <TelerikGrid @ref="Grid" Data="Data" Pageable="true" Sortable="true" Resizable="true" Reorderable="true" ShowColumnMenu="true" Groupable="true" SortMode="@SortMode.Multiple" FilterMode="GridFilterMode.FilterMenu" FilterMenuType="FilterMenuType.CheckBoxList" ScrollMode="GridScrollMode.Scrollable" OnRowContextMenu="OnRowContextMenuClick" OnRowDoubleClick="HandleOnRowDoubleClick" Width="100%" RowHeight="40" PageSize="100"> <GridColumns> @*

Other GridColumns

*@@if (Data?.Count()> 0)
{
foreach (var property in ((IDictionary<string, object>)Data.FirstOrDefault()).Where(p=> AllDomainIdentifiers.Contains(p.Key)))
{
var domainModel=(DomainModel)property.Value; <GridColumn Field="@($" { domainModel.Name } Field ")" FieldType="typeof(bool)" Width="30px" Filterable="false" Groupable="false" Sortable="false" ShowColumnMenu="false" Title="@domainModel.Abbreviation"> <HeaderTemplate> <span id="@( $" domainHeader- { domainModel.Id.ToString ()}" )" alt="@domainModel.Name"> @domainModel.Abbreviation </span> <TelerikTooltip TargetSelector="@( $" # domainHeader- { domainModel.Id.ToString ()}" )" ShowOn="@TooltipShowEvent.Hover" Position="@TooltipPosition.Top" /> </HeaderTemplate> <Template> <div class="d-flex justify-content-center align-items-center"> <TelerikCheckBox Value="@HasDomainActivated(context as ExpandoObject, domainModel)" ValueChanged="@((bool value)=> HandleDomainActivationChanged(context as ExpandoObject, domainModel, value))" Enabled="@(IsAuthorizedForAllDomains() || IsAuthorizedForDomain(domainModel))" /> </div> </Template> </GridColumn> }
} </GridColumns> </TelerikGrid>

## Answer

**Hristian Stefanov** answered on 10 Nov 2021

Hi Ola, The k-filterable CSS class is used for adding extra padding to the right due to the design requirements. This CSS class doesn't depend on the Filterable property of the column. The name "k-filterable" is chosen because of the menu icon in the header, not because the column has filtering or not. I understand that the name of the CSS class can be a little confusing sometimes. However, you can remove the padding-right style as a whole by using a custom CSS style. I have prepared for you an example, and I also used a Class for the Grid to specify the desired instance: <style>.myGrid.k-filterable { padding-right: 0px;
} </style> <TelerikGrid Class="myGrid" Data="@MyData" Pageable="true" PageSize="5" FilterMode="GridFilterMode.FilterMenu" FilterMenuType="FilterMenuType.CheckBoxList" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="80px" /> <GridColumn Field="@(nameof(SampleData.Name))" ShowColumnMenu="false" Filterable="false" Title="Employee Name" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> </GridColumns> </TelerikGrid> @code {
public IEnumerable <SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5
});

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
} } I hope this clarifies things. If you have any other concerns, I would be glad to help. Regards, Hristian Stefanov Progress Telerik

### Response

**Sergio** commented on 10 Jan 2022

C'mon, Telerik, that's a bug. If a column is marked with Filterable="false" then the CSS class should not be added to the header, plain and simple. Your "solution" affects all columns, even those where it would be needed. And if that CSS class is being overloaded for the column menu, then you should have created a separate class for that case. It's not nice to force your users to create custom templates for every column that isn't filterable in a grid view.

### Response

**Hristian Stefanov** commented on 13 Jan 2022

Hi Sergio, Thank you for sharing your thoughts on the topic here. Your words are making sense indeed. I've discussed this with our Front-end team. Still, my previous statement stays - the name "k-filterable" is chosen because of the menu icon in the header, not because the column has filtering or not. If we decide to make a change in the CSS class in the future, we will log an item on our Public Feedback Portal. Currently, we can offer the following modified example that will allow you to apply the style only for specific columns. This way, you will not be forced to create a custom template for every non-filterable column. <style>.myGrid.k-filterable:nth-of-type(2n) { padding-right: 0px;
} </style> <TelerikGrid Class="myGrid" Data="@MyData" Pageable="true" PageSize="5" FilterMode="GridFilterMode.FilterMenu" FilterMenuType="FilterMenuType.CheckBoxList" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="80px" /> <GridColumn Field="@(nameof(SampleData.Name))" ShowColumnMenu="false" Filterable="false" Title="Employee Name" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> </GridColumns> </TelerikGrid> @code {
public IEnumerable <SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5
});

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
}
}

### Response

**Arman** answered on 12 Nov 2021

Hi Hristian, thank you for your answer. I found a solution for my problem. The problem was how I defined my HeaderTemplate. I am now defining it the same way your are without a template like this <HeaderTemplate> <span class="k-cell-inner"> <span class="k-link" id="@( $" domainHeader- { domainModel.Id.ToString ()}" )" alt="@domainModel.Name"> <span class="k-column-title"> @domainModel.Abbreviation </span> </span> </span> <TelerikTooltip TargetSelector="@( $" # domainHeader- { domainModel.Id.ToString ()}" )" ShowOn="@TooltipShowEvent.Hover" Position="@TooltipPosition.Top" /> </HeaderTemplate>

### Response

**Hristian Stefanov** commented on 15 Nov 2021

Hi Ola, Thank you for sharing with us how things turned out. I'm glad to hear that the case is resolved. Regards, Hristian Stefanov Progress Telerik
