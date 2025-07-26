# ProgressBar in Grid dynamic columns With List<ExpandoObject>

## Question

**Moh** asked on 06 Jan 2025

I have a TelerikGrid whose columns is dynamically populated with List<ExpandoObject>. I need a TelerikProgressBar to display one of the columns. I have used the following code but TelerikProgressBar only displays the value of the first record for all rows and individual rows are not displayed properly in TelerikProgressBar. Please help me. Thanks <GridColumns>
@{ if (GridData !=null && GridData.Any())
{ var firstDataItem=(IDictionary<string, object>)GridData.First(); foreach ( var item in firstDataItem)
{ if (item.Key !="ProgressBar_Num" )
{
<GridColumn Field="@item.Key" FieldType="@item.Value.GetType()" @key="@item.Key">
<Template>
<TelerikProgressBar Class="width-100" Max="100" Value="(double)item.Value">
</TelerikProgressBar>
</Template>

</GridColumn>
}
}
}
}
</GridColumns>

## Answer

**Tsvetomir** answered on 07 Jan 2025

Hello Mohamad, To ensure that the TelerikProgressBar displays the correct values for each row in your grid, you need to bind the Value attribute to the specific data of the current row. It seems the current code snippet is using a static value from the first record for all rows. Here's how you can fix this: Solution Use Row Context - Access the current row's data using the context variable. This will ensure that each TelerikProgressBar displays the correct value for its respective row. Here's an example that I have prepared for you: @using System.Dynamic <TelerikGrid Data="@GridData"> <GridColumns> @{
if (GridData !=null && GridData.Any())
{
var firstDataItem=(IDictionary<string, object>)GridData.First();

foreach (var item in firstDataItem)
{
if ( item.Key=="NumericValue" )
{ <GridColumn Field="@item.Key" FieldType="@item.Value.GetType()" @key="@item.Key"> <Template> @{ var currentRow=context as IDictionary<string, object>; var progressBarValue=Convert.ToDouble(currentRow[item.Key]); // get the second property value of the expando object <TelerikProgressBar Class="width-100" Max="100" Value="@progressBarValue"> </TelerikProgressBar> } </Template> </GridColumn> }
else
{ <GridColumn Field="@item.Key" FieldType="@item.Value.GetType()" @key="@item.Key"> </GridColumn> }
}
}
} </GridColumns> </TelerikGrid> @code {
private List <ExpandoObject> GridData { get; set; }=new List <ExpandoObject> ();

private int LastId { get; set; }

protected override async Task OnInitializedAsync()
{
LastId=15;

for (int i=1; i <=LastId; i++)
{
dynamic expando=new ExpandoObject();

expando.Id=i; expando.NumericValue=i * 5; expando.PropertyString="String " + i;

GridData.Add(expando);
}
}
} I hope the provided information helps you to move forward. Regards, Tsvetomir Progress Telerik

### Response

**Mohamad Javad** commented on 07 Jan 2025

Hello, thank you very much for your advice. This advice solved my problem. I also found another solution that seems to be a good one and its code is as follows: <TelerikGrid Data="@Data" <GridColumns>
<GridColumn Field="Tow_Req_Detail_ProgressBar" FieldType="@typeof(string)">
<Template>
@{ dynamic? v=context as ExpandoObject;
<TelerikProgressBar Class="width-100" Max="100" Value="(double)v.Tow_Req_Detail_ProgressBar">
<ProgressBarLabel Visible="true" Position="@ProgressBarLabelPosition.Center">
<Template Context="progressBarContext">
@if (v.Tow_Req_Detail_ProgressBar>=100 )
{
<span style="font-weight:bold;"> 100 </span>
} else {
<span style="font-weight:bold">@(progressBarContext.Value)</span>
}
</Template>
</ProgressBarLabel>
</TelerikProgressBar>
}
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid> Very Thanks

### Response

**Tsvetomir** commented on 08 Jan 2025

Hi Mohamad, Thank you for coming back with feedback. I'm glad to hear that you were able to achieve the desired outcome. Now, I'm closing the ticket. Regards, Tsvetomir
