# ComboBox pre-selecting not working

## Question

**Ale** asked on 28 Jun 2022

Hi, I have a combobox control used to complete a country item in a form, but I'm not able to set the control with the existing country field. My code: razor: @inherits Component <TelerikComboBox TItem="CountryModel" TValue="int" Data="SearchResult" OnRead="SearchDataAsync" Filterable="true" TextField="Name" ValueField="Id" @bind-Value="SelectedId" Width="@Width"> </TelerikComboBox> razor.cs using Core.Common.Models;
using Microsoft.AspNetCore.Components;
using Telerik.Blazor.Components;
using Telerik.DataSource;
using WebApp.Client.Services;

namespace WebApp.Client.Components.Views.Common
{
public partial class CountryAutocomplete
{
[Parameter]
public Action <CountryModel> ValueChanged { get; set; }

[Parameter]
public CountryModel Value { get; set; }

[Parameter]
public string Width { get; set; }="100%";

[Inject]
public StaticDataService StaticDataService { get; set; }

private List <CountryModel> SearchResult { get; set; }=new();

private int _selectedId { get; set; }
private int SelectedId
{
get
{
return _selectedId;
}
set
{
_selectedId=value;
var selected=SearchResult.Single(x=> x.Id==value);
ValueChanged?.Invoke(selected);
}
}

protected override async Task OnParametersSetAsync()
{
Console.WriteLine(SelectedId);
if (Value !=null && Value.Id> 0 && SelectedId==0)
{
SearchResult=new List <CountryModel> {
Value
};
SelectedId=Value.Id;
}
await base.OnParametersSetAsync();
}

private async Task SearchDataAsync(ComboBoxReadEventArgs args)
{
if (args.Request.Filters.Count> 0)
{
var filter=args.Request.Filters[0] as FilterDescriptor;
var search=filter.Value.ToString();
if (search.Length>=2)
{
SearchResult=await StaticDataService.GetCountriesAsync(search);
args.Data=SearchResult;
}
}
}
}
} public class CountryModel : Model
{
public int Id { get; set; }

public string Code { get; set; }

public string Name { get; set; }

public EnumCitizenship Citizenship { get; set; }

public override string ToString()
{
return Name;
}
} Value is the country item passed as parameter from a parent component. The control works properly, including ValueChanged callback, except the pre-selecting.

### Response

**Dimo** commented on 30 Jun 2022

We had some issues with the initial ComboBox value when using asynchronous OnRead. Try with the latest version and if it still doesn't work, please send a standalone runnable page for inspection.

### Response

**Alexandru** commented on 05 Jul 2022

I found another solution. I posted it below. Thanks!

## Answer

**Timothy J** answered on 28 Jun 2022

Try this.StateHasChanged() in your SelectedId.Set?

### Response

**Alexandru** commented on 29 Jun 2022

Yes. Still not working.

### Response

**Alexandru** answered on 05 Jul 2022

I solved by modifying the OnRead event function. The parameter data should also be added via args.Data=SearchResult; I will repost the working code: Razor: @inherits Component <TelerikComboBox TItem="CourtModel" TValue="EnumCourt" OnRead="SearchDataAsync" Filterable="true" TextField="Name" ValueField="Id" @bind-Value="SelectedId" Width="@Width"> </TelerikComboBox> Razor.cs: using Core.Common.Models; using Core.Common.Models.Enums; using Microsoft.AspNetCore.Components; using Telerik.Blazor.Components; using Telerik.DataSource; using WebApp.Client.Services; namespace WebApp.Client.Components.Common.Views { public partial class CourtAutocomplete {
[ Parameter ] public Action<CourtModel> ValueChanged { get; set; }

[ Parameter ] public CourtModel Value { get; set; }

[ Parameter ] public string Width { get; set; }="100%";

[ Inject ] public StaticDataService StaticDataService { get; set; } private List<CourtModel> SearchResult { get; set; }=new (); private EnumCourt _selectedId { get; set; } private EnumCourt SelectedId
{ get { return _selectedId;
} set {
_selectedId=value; var selected=SearchResult.Single(x=> x.Id==value );
ValueChanged?.Invoke(selected);
}
} private async Task SearchDataAsync ( ComboBoxReadEventArgs args ) { if (args.Request.Filters.Count> 0 )
{ var filter=args.Request.Filters[ 0 ] as FilterDescriptor; var search=filter.Value.ToString();
SearchResult=new (); if (search.Length>=2 )
{
SearchResult=await StaticDataService.GetCourtListAsync(search);
args.Data=SearchResult;
}
} else if (Value !=null && Value.Id> 0 ) //set source from parameter {
SearchResult=new List<CourtModel>
{
Value
};
SelectedId=Value.Id;
}
args.Data=SearchResult;
}
}
} public class CountryModel: Model { public int Id { get; set; } public string Code { get; set; } public string Name { get; set; } public EnumCitizenship Citizenship { get; set; } public override string ToString ( ) { return Name;
}
} Thanks!
