# Detail Template requires double click to expand after filtering

## Question

**Mar** asked on 20 Feb 2024

When using a detail template on a grid control, the user must click twice to expand the detail section after filtering. Executable: [https://blazorrepl.telerik.com/QyummElT43XLHu3R42](https://blazorrepl.telerik.com/QyummElT43XLHu3R42) Steps to reproduce: 1) Load Page 2) Make a selection from the category drop down filter 3) Attempt to expand the detail section of any record by clicking on the "+" @page "/"
@using Telerik.DataSource <TelerikGrid TItem="@Person" OnRead="@LoadGrid" SelectionMode="GridSelectionMode.Single" FilterMode="GridFilterMode.FilterRow" FilterRowDebounceDelay="200" Pageable="true" PageSize="15"> <DetailTemplate> @{
var selected=context as Person;
} <div class="row"> <div class="col-2"> <h1> @selected.First </h1> </div> <div class="col-2"> <h1> @selected.Last </h1> </div> </div> </DetailTemplate> <GridColumns> <GridColumn Field="@nameof(Person.First)" Title="First" Filterable="false"> </GridColumn> <GridColumn Field="@nameof(Person.Last)" Title="Last" Filterable="false"> </GridColumn> <GridColumn Field="@nameof(Person.Category)" Title="Category"> <FilterCellTemplate> @{
CategoryFilter=context;
} <TelerikDropDownList Data="Categories" @bind-Value="SelectedCategory" OnChange="SetupCategoryFilter"> </TelerikDropDownList> </FilterCellTemplate> </GridColumn> </GridColumns> </TelerikGrid> @code
{
private FilterCellTemplateContext CategoryFilter { get; set; }=new();

private List <int> Categories=[0, 1, 2, 3, 4];

private int SelectedCategory { get; set; }

private async Task SetupCategoryFilter()
{
var filter=CategoryFilter.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor;

if (filter is null)
{
return;
}

filter.Value=SelectedCategory;
filter.Operator=FilterOperator.IsEqualTo;

await CategoryFilter.FilterAsync();
}

protected void LoadGrid(GridReadEventArgs args)
{
List <Person> list=[
new Person {First="John", Last="Doe", Category=1},
new Person {First="Jane", Last="Doe", Category=2},
new Person {First="John", Last="Smith", Category=3},
new Person {First="Jane", Last="Smith", Category=4}
];

args.Data=list;
args.Total=list.Count;
} public class Person { public string First { get; set; } public string Last { get; set; } public int Category { get; set; } } }

## Answer

**Tsvetomir** answered on 22 Feb 2024

Hi Mark, Thank you for the detailed explanation and the provided demo. The problem you are experiencing is not related to the usage of the details template, but it comes from the OnChange event of the DropDownList. More specifically the OnChange event will fire twice, first when the user selects a category and then again when the component loses focus. In this case, the first click on the Grid will blur the DropDownList and fire OnChange again. This will make the Grid to refresh its data and cancel out the first click on the plus (+) button (in your case), then the second click will work as expected. To fix this problem, I suggest you to use the ValueChanged event. The main difference with the OnChange event is that ValueChanged fires upon user interaction only, and not when the component loses its focus. For your convenience, I have modified your code. Here is a link to it REPL, where you can test it on your own. Regards, Tsvetomir Progress Telerik
