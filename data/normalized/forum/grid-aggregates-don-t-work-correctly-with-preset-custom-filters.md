# Grid aggregates don't work correctly with preset custom filters

## Question

**Ray** asked on 10 Jun 2021

Hi, Within our Blazor application I use a Grid with custom row filters: <TelerikGrid Data="@RecordList" SelectionMode="GridSelectionMode.Multiple" Width="100%" Pageable="true" PageSize="@PageSize" FilterMode="@GridFilterMode.FilterRow" Sortable="true" Groupable="false" Height="760px" Resizable="true"> <GridColumns> <GridColumn Width="200px" Field="@nameof(Demo.Name)" Title="@L[" Name "]"> <FilterCellTemplate> <CustomListRowFilter Context="@context" ListValues="EmployeeFilterList" AddNoneItem="false" /> </FilterCellTemplate> </GridColumn> <GridColumn Width="200px" Field="@nameof(Demo.Datum)" Title="@L[" Date "]"> <FilterCellTemplate> <CustomDateSpanRowFilter Context="@context" InitialValueFrom="@InitialDateFromFilter" InitialValueTo="@InitialDateToFilter" /> </FilterCellTemplate> </GridColumn> <GridColumn Width="200px" Field="@nameof(Demo.Hours)" Title="@L[" Hours "]"> <FilterCellTemplate> <CustomNumberRowFilter Context="@context" /> </FilterCellTemplate> <FooterTemplate> <span> Total: @context.Sum?.ToString("0.00") </span> </FooterTemplate> </GridColumn> <GridColumn Width="200px" Field="@nameof(Demo.Checked)" Title="@L[" Checked "]"> <FilterCellTemplate> <CustomBooleanRowFilter Context="@context" InitialValue="false" /> </FilterCellTemplate> <Template> <input type="checkbox" checked="@(((Demo) context).Checked)" @onchange="@(args=> OnCheckChanged((Demo) context, args))" /> </Template> </GridColumn> </GridColumns> <GridAggregates> <GridAggregate Field=@nameof(Demo.Hours) Aggregate="@GridAggregateType.Sum" /> </GridAggregates> </TelerikGrid> For example, the custome date filter looks like: <select value="@Value" @onchange="OnFilterChanged"> <option value="@string.Empty"> All </option> <option value="True"> True </option> <option value="False"> False </option> </select> @code {
private string Field { get; set; }
private string Value { get; set; }
private bool? _boolValue;
[Parameter]
public FilterCellTemplateContext Context { get; set; }
[Parameter]
public bool? InitialValue { get; set; }

protected override async Task OnInitializedAsync()
{
Field=((FilterDescriptor) Context.FilterDescriptor.FilterDescriptors[0])?.Member;
if (InitialValue !=null)
{
SetValue(InitialValue.Value);
await SetFilter();
}
else
{
SetValue(((FilterDescriptor)Context.FilterDescriptor.FilterDescriptors[0]).Value);
}
}

private void SetValue(object value)
{
if (string.IsNullOrEmpty(value?.ToString()) || value.ToString()=="All")
{
_boolValue=null;
Value=string.Empty;
}
else
{
bool.TryParse(value.ToString(), out var parseResult);
_boolValue=parseResult;
Value=_boolValue.ToString();
}
}

protected async Task OnFilterChanged(ChangeEventArgs args)
{
var value=args.Value;
SetValue(value);
await SetFilter();
}

private async Task SetFilter()
{
if (_boolValue !=null)
{
var filterDescriptors=Context.FilterDescriptor.FilterDescriptors.Where(descriptor=>
((FilterDescriptor)descriptor).Member==Field).ToList();

var filterDescriptor=(FilterDescriptor) filterDescriptors[0];
filterDescriptor.Value=_boolValue;

((FilterDescriptor)filterDescriptors[0]).Operator=FilterOperator.IsEqualTo;
await Context.FilterAsync();
}
else
{
await Context.ClearFilterAsync();
}
}
} In my example the filter for the column "Checked" gets an initial value when page is loaded. The grid filters correctly. But the sum of the hours column show the overall sum and not the filtered one. Do I miss something? Maybe within the filter component? Best regards, Rayko

## Answer

**Eric R | Senior Technical Support Engineer** answered on 14 Jun 2021

Hi Rayko, Thank you for providing the Grid markup and Filter Template component. From it, I was able to reproduce a sample locally. However, it doesn't appear to be anything related to the implementation information that was provided. For your reference, I have attached a sample that illustrates the desired approach. I recommend using it as as a baseline for comparison to your existing project. Please let me know if you need any additional information. Thank you for being a valued UI for Blazor developer. Regards, Eric R | Senior Technical Support Engineer

### Response

**Rayko** answered on 23 Aug 2021

Hi Eric, First, sorry for my late reply! And thank you for your sample! It shows the same issue which I've tried to explain: Initially, the grid is filtered by "Is FTE?=True". It shows 20 lines. The sum of "Hours" should be 800. But the footer shows another value (depends on the random logic which you've implemented): Then, when changing the filter, the correct sum is shown. But I need the correct value initially... Best regards, Rayko

### Response

**Rayko** commented on 23 Aug 2021

I've just found out that using the OnRead event instead of the standard data binding solves the issue. Better said, it's a possible work-around.

### Response

**Hristian Stefanov** answered on 26 Aug 2021

Hi Rayko, Thank you for reporting this issue. I'm also glad to hear that you can continue with your application using the OnRead event. We have opened a bug report on your behalf regarding the Grid aggregates on initial load on our Public Feedback Portal. The status is set to "Unplanned", which means that this is a verified/confirmed bug, but with no scheduled date for implementation yet. Since we created this bug report on your behalf, you are automatically subscribed to receive email notifications on status updates. We prioritize bug reports depending on community interest. I added your vote there on your behalf to increase the item's popularity. I am sorry to report that we are not aware of any other workarounds except using the OnRead in the meantime. Please let me know if you have any other questions. Regards, Hristian Stefanov
