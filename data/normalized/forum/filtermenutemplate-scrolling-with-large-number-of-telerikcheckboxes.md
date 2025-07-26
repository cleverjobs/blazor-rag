# FilterMenuTemplate scrolling with large number of TelerikCheckBoxes

## Question

**Joh** asked on 21 Jun 2022

I like the concept of having a list of values that can be checked to filter. My problem is the list can be really long. Long enough that if you have to use the scroll bar on the page to try to see the remaining entries. However using the scroll bar closes the filter menu. Is there a way to add a scroll bar to the filter menu list?

## Answer

**Hristian Stefanov** answered on 24 Jun 2022

Hi John, The easiest way to apply a scrollbar for a long list in the filter menu is to use the CSS style - " overflow: auto ". Here is an example I have prepared for you: @using Telerik.DataSource <style>.k-filter-menu { height: 200px; overflow: auto;
} </style> <TelerikGrid Data=@GridData FilterMode="@GridFilterMode.FilterMenu" ShowColumnMenu="true" FilterMenuType="@FilterMenuType.CheckBoxList" Height="400px" Width="600px" Pageable="true"> <GridColumns> <GridColumn Field="Id" Filterable="false" Width="80px" /> <GridColumn Field="Size" Context="context"> <FilterMenuTemplate> @{
theFilterContext=context;
} <TelerikCheckBoxListFilter Data="@Sizes" Field="@(nameof(NameFilterOption.Size))" @bind-FilterDescriptor="@theFilterContext.FilterDescriptor"> </TelerikCheckBoxListFilter> </FilterMenuTemplate> </GridColumn> <GridColumn Field="ProductName" Title="Product" Filterable="false" /> </GridColumns> </TelerikGrid> @code {
FilterMenuTemplateContext theFilterContext { get; set; }
public List <SampleData> GridData { get; set; }

protected override void OnInitialized()
{
GridData=Enumerable.Range(1, 70).Select(x=> new SampleData
{
Id=x,
Size=Sizes[x % Sizes.Count].Size,
ProductName=$"Product {x}",
TestCheckbox=x % 2==0 ? true : false
}).ToList();
base.OnInitialized();
}

public class SampleData
{
public int Id { get; set; }
public string Size { get; set; }
public string ProductName { get; set; }
public bool TestCheckbox { get; set; }
}

public List <NameFilterOption> Sizes=new List <NameFilterOption> () { new NameFilterOption { Size="XS" }, new NameFilterOption { Size="S" }, new NameFilterOption { Size="M" }, new NameFilterOption { Size="L" } };

public class NameFilterOption
{
public string Size { get; set; }
}
} Regards, Hristian Stefanov

### Response

**John** commented on 24 Jun 2022

Thanks Hristian, the styling nicely resolved my issue
