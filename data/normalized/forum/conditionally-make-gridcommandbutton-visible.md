# Conditionally Make GridCommandButton Visible

## Question

**BobBob** asked on 08 Mar 2021

I want to make a Custom GridCommandbutton Visible based on a value in the row. For example, if the Status column of a row is 2, I want the command button to be visible, otherwise I want it hidde. Is this possible?

## Answer

**Svetoslav Dimitrov** answered on 09 Mar 2021

Hello Bob, We have an open feature request for providing context to the Grid command column (similar to the context for the standard column). Once this feature is available you would be able to easily hide or show buttons based on certain conditions. I have given your Vote for it and you can Follow the thread for email notifications on status updates. For the time being, in the public thread, we have made several examples and information on how to make a custom command column where you can access the context. Let me know if you need any further assistance! Regards, Svetoslav Dimitrov

### Response

**Rob** commented on 09 Jan 2025

Did this ever get implemented? I can't find an "Visible" property regardless of context usage? I've been able to set Enabled property, but I'd rather use a Visible property. There is a "ShowInEdit" property but nothing like just "Show" (regardless of grid mode). The link Svetoslav provided doesn't really address anything to do with controlling command button visibility? Rob

### Response

**Hristian Stefanov** commented on 10 Jan 2025

Hi Rob, I confirm that a Visible parameter is unnecessary, as you can easily show or hide a specific command button by using the context of the command column and conditionally rendering the button. @CustomCommandResult <TelerikGrid Data=@GridData EditMode="@GridEditMode.Inline" OnUpdate="@MyOnUpdateHandler" Pageable="true" PageSize="15" Height="500px"> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="Employee ID" /> <GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" /> <GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" /> <GridCommandColumn Context="dataItem"> @{
var item=(SampleData)dataItem;
} <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil"> Edit </GridCommandButton> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true" OnClick="@CustomSaveOnClickHandler"> Save </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true"> Cancel </GridCommandButton> @if (item.ID % 2==0)
{ <GridCommandButton Command="MyOwnCommand" Icon="@SvgIcon.InfoCircle" ShowInEdit="false" OnClick="@MyCustomCommandOnClickHandler"> My Command </GridCommandButton> } </GridCommandColumn> </GridColumns> </TelerikGrid> @code {
private List <SampleData> GridData { get; set; }
private MarkupString CustomCommandResult;

public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

private async Task CustomSaveOnClickHandler(GridCommandEventArgs args)
{
SampleData theUpdatedItem=args.Item as SampleData;
}

private async Task MyCustomCommandOnClickHandler(GridCommandEventArgs args)
{
CustomCommandResult=new MarkupString(CustomCommandResult + string.Format(" <br /> Custom command triggered for item {0}", (args.Item as SampleData).ID));
}

private async Task MyOnUpdateHandler(GridCommandEventArgs args)
{
SampleData theUpdatedItem=args.Item as SampleData;

await MyService.Update(theUpdatedItem);

await GetGridData();
}

private async Task GetGridData()
{
GridData=await MyService.Read();
}

protected override async Task OnInitializedAsync()
{
await GetGridData();
}

public static class MyService
{
private static List <SampleData> _data { get; set; }=new List <SampleData> ();

public static async Task<List <SampleData>> Read()
{
if (_data.Count <1)
{
for (int i=1; i <50; i++)
{
_data.Add(new SampleData()
{
ID=i,
Name="name " + i,
HireDate=DateTime.Now.AddDays(-i)
});
}
}

return await Task.FromResult(_data);
}

public static async Task Update(SampleData itemToUpdate)
{
var index=_data.FindIndex(i=> i.ID==itemToUpdate.ID);
if (index !=-1)
{
_data[index]=itemToUpdate;
}
}
}
} If you prefer not to remove the button from the DOM entirely but simply hide it, you can conditionally set the Class parameter of the GridCommandButton tag and use a single line of CSS to hide the button. Kind Regards, Hristian

### Response

**Jay** answered on 12 May 2022

This can be done by setting the GridCommandColumn's Context="dataItem", then using it in a code block: [https://docs.telerik.com/blazor-ui/components/grid/columns/command#context](https://docs.telerik.com/blazor-ui/components/grid/columns/command#context) Thanks, Jay
