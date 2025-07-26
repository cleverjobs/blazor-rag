# Responsive Grid

## Question

**Moh** asked on 06 Jan 2025

I want the Grid to display correctly on different devices like Mobile And Tablet. In other words, I want to have a Responsive Grid. In such a way that the Grid is displayed correctly in different dimensions and the remaining columns that do not fit on the page are scrolled horizontally. Please help me. Currently, on different devices such as mobile and tablet, the Grid is displayed as small columns, which is not suitable at all. Thanks

## Answer

**Tsvetomir** answered on 07 Jan 2025

Hello Mohamad, Thank you for the clear explanation of the result you are looking for. You may get such an appearance if the Grid does not have any value set for its Width parameter. Is that the case on your end? With such configuration the Grid behaves as any regular HTML table - it will fit all the available space and it will shrink on small devices. The columns that do not have an explicit Width set will also shrink. See more details on the column Width behavior here: [https://docs.telerik.com/blazor-ui/components/grid/columns/width.](https://docs.telerik.com/blazor-ui/components/grid/columns/width.) To handle the scenario, you may set explicit Width to the Grid, so it is preserved on small screens, too. If the screen space is not enough to display the whole Grid, you will get a horizontal scrollbar. Another possible approach to achieve a responsive Grid layout is to use the MediaQuery component. Utilize its OnChange event to change the configuration of the Grid component on the page. Let me address below the steps on how to integrate the MediaQuery component with a Grid: Define the Media parameter of the MediaQuery instances. Based on the device resolution, change the value of the Visible parameter of the GridColumns within the OnChange event. To assist you with that, I have prepared a runnable REPL example that demonstrates the above approach. Finally, apart from the above information, we have a feature request for responsive Grid. You may vote for it and follow it to get status updates. Regards, Tsvetomir Progress Telerik

### Response

**Mohamad Javad** commented on 07 Jan 2025

Hi According to your advice, I solved my problem by fixing the size of the columns. Thank you It would be much better if it was possible for the columns to adjust themselves automatically without setting and fixing their width. For example, see the link below. This table is displayed correctly on different devices without setting a fixed width [https://demos.devexpress.com/blazor/Grid](https://demos.devexpress.com/blazor/Grid) Thanks

### Response

**Mohamad Javad** answered on 07 Jan 2025

Hi I am using ExpandoObject for Grid data. Please tell me how to use AutoFitAllColumns for dynamic data. My code is: <TelerikGrid Data="@Data_Grid" @ref="@GridRef".... <TelerikButton OnClick="@AutoFitAllColumns">AutoFit All Columns</TelerikButton>

@code { public List<ExpandoObject>? Data_Grid; public TelerikGrid<ExpandoObject>? GridRef { get; set; } private async Task AutoFitAllColumns () { await GridRef!.AutoFitAllColumnsAsync();
}
} I am getting a compile error when adding @ref="@GridRef" to Grid and if I remove @ref="@GridRef" the AutoFit button does not work. Please help me.

### Response

**Tsvetomir** commented on 08 Jan 2025

Hi Mohamad, I've tried the Autofit Columns feature within this example below. As a result on my end, the Grid columns are resized correctly as expected without any compile errors and exceptions. This leads me to think that I'm missing something from the actual configuration. Run the example on your side to see the result and try to use it as a reference. Here is the code snippet: @using System.Dynamic <TelerikButton OnClick="@AutoFitAllColumns"> AutoFit All Columns </TelerikButton> <TelerikGrid Data="@GridData" Pageable="true" Sortable="true" Resizable="true" @ref="@GridRef"> <GridColumns> @{
if (GridData !=null && GridData.Any())
{
var firstDataItem=(IDictionary<string, object>)GridData.First();

foreach (var item in firstDataItem)
{
if (item.Key !="Id")
{ <GridColumn Field="@item.Key" FieldType="@item.Value.GetType()" @key="@item.Key"> </GridColumn> }
}
}
} </GridColumns> </TelerikGrid> @code {
private List <ExpandoObject> GridData { get; set; }=new List <ExpandoObject> ();

private int LastId { get; set; }

private TelerikGrid <ExpandoObject>? GridRef { get; set; } private async Task AutoFitAllColumns()
{
await GridRef!.AutoFitAllColumnsAsync();
} protected override async Task OnInitializedAsync()
{
LastId=15;

for (int i=1; i <=LastId; i++)
{
dynamic expando=new ExpandoObject();

expando.Id=i;
expando.PropertyInt=i;
expando.PropertyString="String " + i;
expando.PropertyDate=DateTime.Now.AddMonths(-i);

GridData.Add(expando);
}
}
} If the issue persist, modify the example to reproduce the behavior and send it back to me for inspection. This will help me to see the scenario on my side and troubleshoot it further. I look forward for your reply. Regard, Tsvetomir

### Response

**Mohamad Javad** commented on 08 Jan 2025

Hello Thank you for your answer. You are right. The error was in the grouping type. I had used the code OnStateInit="@((GridStateEventArgs<object> args)=> OnGridStateInitHandler(args))" which was causing the error and changing it to the following code resolved the error: OnStateInit="@((GridStateEventArgs<ExpandoObject> args)=> OnGridStateInitHandler(args))" Thank you

### Response

**Tsvetomir** commented on 09 Jan 2025

Hello Mohamad, I'm glad to hear that the issue is resolved. Now I'm closing the ticket. Regards, Tsvetomir
