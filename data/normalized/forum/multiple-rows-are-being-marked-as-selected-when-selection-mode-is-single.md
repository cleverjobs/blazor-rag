# Multiple rows are being marked as selected when selection mode is single

## Question

**Har** asked on 12 May 2022

I have a grid defined with SelectionMode="GridSelectionMode.Single". I'm handling the SelectedItemsChanged event and when returning the previously selected row is selected with the newly selected row. This appears to be happening when an async call to a web api using http client is made. If I comment out the http call the selection works as expected. Can someone explain why the http client call could be impacting the selection functionality or how I may go about debugging this? <div> <div> <label for="label"> Labels </label> <div> <TelerikGrid Data="@Labels" FilterMode="@GridFilterMode.FilterRow" ScrollMode="GridScrollMode.Scrollable" SelectionMode="GridSelectionMode.Single" SelectedItems="@SelectedLabels" SelectedItemsChanged="@((IEnumerable<LabelDto> labelList)=> OnSelectAsync(labelList))" Height="200px"> <GridColumns> <GridColumn Field="@(nameof(LabelDto.Name))"> </GridColumn> </GridColumns> </TelerikGrid> </div> </div> </div> public partial class LabelSelection
{
private ObservableCollection <LabelDto>? _labels;
private int? _selectedValue;
public IEnumerable <LabelDto> SelectedLabels { get; set; }=Enumerable.Empty <LabelDto> ();

protected async Task OnSelectAsync(IEnumerable <LabelDto> labels)
{
var l=labels.ToList();
SelectedLabels=l;

if (l.Any())
await LabelChangedAsync(l[0]);

StateHasChanged();
}
...
}

public async Task LabelChangeHandlerAsync(LabelDto label)
{
_currentLabel=label;

var labelWithAttributes=await LabelRepo.GetLabelAsync((int)label.Id);

//LabelAttributeList.Clear();

//if (labelWithAttributes.Attributes.Any())
//{
// LabelAttributeList.AddRange(labelWithAttributes.Attributes);
//}
} public async Task<LabelWithAttributesDto> GetLabelAsync(int id) { var req=$"labels/{id}?includeAttributes=true"; _logger.Log(LogLevel.Warning, $"GetLabelsAsync({_client.BaseAddress}{req})..."); // The next call will cause multiple rows to be selected. Commenting this out will make the selections work. var apiResponse=await _client.GetStreamAsync(req); //_logger.Log(LogLevel.Warning, $"...back from GetLabelsAsync({_client.BaseAddress}{req})"); //var label=await JsonSerializer.DeserializeAsync<LabelWithAttributesDto> // (apiResponse, new JsonSerializerOptions() { PropertyNameCaseInsensitive=true }); //return label; return new LabelWithAttributesDto(1, "new", "filename", "100", new List<LabelAttributeDto>()); }

## Answer

**Marin Bratanov** answered on 15 May 2022

Hello Harold, Does using a synchronous handler for SelectedItemsChanged help? It is not designed for async operations and if you need that, I suggest you use the OnRowClick event, as advised here. Regards, Marin Bratanov Progress Telerik

### Response

**Harold** commented on 16 May 2022

How can I determine which event/methods support ASYNC and which do not?

### Response

**Marin Bratanov** commented on 16 May 2022

Most do, if there is something specific, the documentation should note it.

### Response

**Harold** commented on 16 May 2022

The documentation online for the Grid does not say anything about not supporting ASYNC. Telerik UI for Blazor : Grid : SelectedItemsChange

### Response

**Marin Bratanov** commented on 17 May 2022

It links to examples that link the row click event and the code explains that for async operations the row click should be used. As a general principle, the <ParameterName>Changed events are often there for parameter binding and not really for long slow operations.
