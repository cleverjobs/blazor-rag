# Custom Filter Row - Check Box List

## Question

**Vad** asked on 18 Jul 2022

Hello I am implementing Custom Filter Row. The main task is to implement Check Box List in the row filter (multi select). Could someone please provide information how can I implement Custom Row Filter like Check Box List Filter for Filter menu?

## Answer

**Hristian Stefanov** answered on 21 Jul 2022

Hi Vadzim, The easiest way that comes to my mind is to use the TelerikCheckBoxListFilter component we expose and bind the desired collection of values. I have prepared for you a base example to show the idea and the component usage below. You can use the same approach by configuring it in the FilterCellTemplate for Row Filtering wrapped in a scrollable element. @using Telerik.DataSource <TelerikGrid Data=@GridData FilterMode="@GridFilterMode.FilterMenu" FilterMenuType="@FilterMenuType.CheckBoxList" Height="400px" Width="600px" Pageable="true"> <GridColumns> <GridColumn Field="Id" Filterable="false" Width="80px" /> <GridColumn Field="Size" Context="context"> <FilterMenuTemplate> <TelerikCheckBoxListFilter Data="@Sizes" Field="@(nameof(NameFilterOption.Size))" @bind-FilterDescriptor="@context.FilterDescriptor"> </TelerikCheckBoxListFilter> </FilterMenuTemplate> </GridColumn> <GridColumn Field="ProductName" Title="Product" Filterable="false" /> </GridColumns> </TelerikGrid> @code {
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

public List <NameFilterOption> Sizes=new List <NameFilterOption> () { new NameFilterOption { Size="XS" }, new NameFilterOption { Size="S" }, new NameFilterOption { Size="M" } };

public class NameFilterOption
{
public string Size { get; set; }
}
} I hope that covers the desired result. Let me know if the idea is different or if further information is needed. Regards, Hristian Stefanov
