# Disabling the header level TelerikGridCheckboxColumn

## Question

**Afr** asked on 10 Apr 2023

Hi, I am using the TelerikGrid control to present the data. I am also using a TelerikGridCheckboxColumn which is bind to a IEnumerableList. I want to disable header checkbox when all the values of IsSelected property in the list are false. How can I do that? Thanks, Afreen

## Answer

**Hristian Stefanov** answered on 13 Apr 2023

Hi Afreen, I confirm that the desired result is easily achievable through some custom CSS styles and an " if " block with the needed condition. I have prepared an example that shows a disabled header checkbox when all checkboxes are false (see highlighted part): <TelerikGrid @ref="@GridRef" Data="@GridData" SelectionMode="GridSelectionMode.Multiple" @bind-SelectedItems="SelectedItems"> <GridColumns> <GridCheckboxColumn Width="140px" HeaderClass="header-select-all"> <HeaderTemplate> @{ <TelerikCheckBox Class="checkbox-in-header" @bind-Value="@SelectAllCheckBoxValue" Enabled="@SelectAllEnabled" TabIndex="-1" Indeterminate="@(SelectAllCheckBoxValue==null)" /> } </HeaderTemplate> </GridCheckboxColumn> <GridColumn Field="@(nameof(Product.Name))" Title="Product Name" /> </GridColumns> </TelerikGrid> <style>.k-grid.header-select-all.k-checkbox { vertical-align: middle;
}.k-grid.header-select-all,.k-grid td:first -child { text-align: center;
} </style> @if (SelectedItems.Count()==0)
{ <style>.checkbox-in-header { pointer-events: none; opacity: 0.5;
} </style> } @code {
List <Product> GridData { get; set; }
TelerikGrid <Product> GridRef { get; set; }
IEnumerable <Product> SelectedItems { get; set; }=Enumerable.Empty <Product> ();
bool SelectAllEnabled { get; set; }

void ToggleSelectAll()
{
if (SelectAllCheckBoxValue.HasValue && SelectAllCheckBoxValue.Value)
{
SelectAllCheckBoxValue=false;
}
else
{
SelectAllCheckBoxValue=true;
}
}

bool? SelectAllCheckBoxValue
{
get
{
if (IsAllDataSelected())
{
return true;
}
else if (IsAnyDataSelected())
{
return null;
}

return false;
}

set
{
if (value.HasValue && value.Value==true)
{
SelectedItems=GridRef.Data;
}
else
{
SelectedItems=new List <Product> ();
}
}
}

bool IsAnyDataSelected()
{
return GridRef.SelectedItems.Count()> 0 && GridRef.SelectedItems.Count() <GridRef.Data.Count();
}

bool IsAllDataSelected()
{
return GridRef.SelectedItems.Count()==GridRef.Data.Count();
}

bool GridHasData()
{
return GridRef.Data.Count()> 0;
}

protected override void OnInitialized()
{
GridData=Enumerable.Range(1, 5).Select(x=> new Product
{
Id=x,
Name="Product name " + x
}).ToList();

// OR use an empty collection to test the behavior with no data
//GridData=new List <Product> ();

base.OnInitialized();
}

protected override void OnAfterRender(bool firstRender)
{
if (firstRender)
{
var gridHasData=GridHasData();

if (SelectAllEnabled !=gridHasData)
{
SelectAllEnabled=gridHasData;
StateHasChanged();
}
}
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Please run and test it to see if the result covers your needs. Regards, Hristian Stefanov Progress Telerik

### Response

**Afreen** commented on 13 Apr 2023

Thanks Hristian Stefanov! Is there any event also we apply this if condition and use the given style? Can you please give an example? Regards, Afreen

### Response

**Hristian Stefanov** commented on 18 Apr 2023

Hi Afreen, Thank you for getting back to me with feedback. As far as I understand, the desired result is to change the " if " block condition inside an event that fires upon selection. For that goal, you can use the SelectedItemsChanged event. I modified the sample so now it shows how the event works: <TelerikGrid @ref="@GridRef" Data="@GridData" SelectionMode="GridSelectionMode.Multiple" SelectedItems="SelectedItems" SelectedItemsChanged="@((IEnumerable<Product> productsList)=> OnSelect(productsList))"> <GridColumns> <GridCheckboxColumn Width="140px" HeaderClass="header-select-all"> <HeaderTemplate> @{ <TelerikCheckBox Class="checkbox-in-header" @bind-Value="@SelectAllCheckBoxValue" Enabled="@SelectAllEnabled" TabIndex="-1" Indeterminate="@(SelectAllCheckBoxValue==null)" /> } </HeaderTemplate> </GridCheckboxColumn> <GridColumn Field="@(nameof(Product.Name))" Title="Product Name" /> </GridColumns> </TelerikGrid> <style>.k-grid.header-select-all.k-checkbox { vertical-align: middle;
}.k-grid.header-select-all,.k-grid td:first -child { text-align: center;
} </style> @if ( disableHeaderCheckbox )
{ <style>.checkbox-in-header { pointer-events: none; opacity: 0.5;
} </style> }

@code {
List <Product> GridData { get; set; }
TelerikGrid <Product> GridRef { get; set; }
IEnumerable <Product> SelectedItems { get; set; }=Enumerable.Empty <Product> ();
bool SelectAllEnabled { get; set; } bool disableHeaderCheckbox { get; set; }=true; protected void OnSelect(IEnumerable <Product> products)
{
SelectedItems=products;
if (SelectedItems.Count()==1)
{
disableHeaderCheckbox=true;
}
else
{
disableHeaderCheckbox=false;
}
} void ToggleSelectAll()
{
if (SelectAllCheckBoxValue.HasValue && SelectAllCheckBoxValue.Value)
{
SelectAllCheckBoxValue=false;
}
else
{
SelectAllCheckBoxValue=true;
}
}

bool? SelectAllCheckBoxValue
{
get
{
if (IsAllDataSelected())
{
return true;
}
else if (IsAnyDataSelected())
{
return null;
}

return false;
}

set
{
if (value.HasValue && value.Value==true)
{
SelectedItems=GridRef.Data;
}
else
{
SelectedItems=new List <Product> ();
}
}
}

bool IsAnyDataSelected()
{
return GridRef.SelectedItems.Count()> 0 && GridRef.SelectedItems.Count() <GridRef.Data.Count();
}

bool IsAllDataSelected()
{
return GridRef.SelectedItems.Count()==GridRef.Data.Count();
}

bool GridHasData()
{
return GridRef.Data.Count()> 0;
}

protected override void OnInitialized()
{
GridData=Enumerable.Range(1, 5).Select(x=> new Product
{
Id=x,
Name="Product name " + x
}).ToList();

// OR use an empty collection to test the behavior with no data
//GridData=new List <Product> ();

base.OnInitialized();
}

protected override void OnAfterRender(bool firstRender)
{
if (firstRender)
{
var gridHasData=GridHasData();

if (SelectAllEnabled !=gridHasData)
{
SelectAllEnabled=gridHasData;
StateHasChanged();
}
}
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Let me know if I'm still missing something. Kind Regards, Hristian
