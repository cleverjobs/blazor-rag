# Still no way to hide a GridCommandButton based on row data for a Grid?

## Question

**RobRob** asked on 09 Jan 2025

Going back to 2020 threads I researched and there is still no way I can tell for easily hiding a GridCommandButton (even when using context)? What is odd, the "ShowInEdit" will indeed hide the GridCommandButton if row selected and in edit mode ... so it seems you folks have a way to control visibility but no property for it? So I'm assuming after 4 years of Blazor UI support, a "visibility" property will NOT happen? Currently this is what I use to "Enable" a GridCommandButton but that's not really what I want to do, I don't want to show it. <GridCommandColumn Context="bookingEquipmentDeleteCommandContext" Width="8rem"> @{
var equipment=bookingEquipmentDeleteCommandContext as BookingEquipmentModel;
} <GridCommandButton Command="Delete" OnClick="@EquipmentDeleteCommandHandler" Class="btn-red" Icon="@FontIcon.Trash" Enabled="@(string.IsNullOrEmpty(equipment?.EquipmentCode))" ShowInEdit="false"> Delete </GridCommandButton> </GridCommandColumn> I would think something as simple as "Visible" would be easy to implement, especially now that we're on version 7 on the control suite? Rob.

## Answer

**Hristian Stefanov** answered on 10 Jan 2025

Hi Rob, I'm pasting here the answer I gave you in the other forum thread so the community that finds this can benefit from it.==I confirm that a Visible parameter is unnecessary, as you can easily show or hide a specific command button by using the context of the command column and conditionally rendering the button. @CustomCommandResult <TelerikGrid Data=@GridData EditMode="@GridEditMode.Inline" OnUpdate="@MyOnUpdateHandler" Pageable="true" PageSize="15" Height="500px"> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="Employee ID" /> <GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" /> <GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" /> <GridCommandColumn Context="dataItem"> @{
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
} If you prefer not to remove the button from the DOM entirely but simply hide it, you can conditionally set the Class parameter of the GridCommandButton tag and use a single line of CSS to hide the button.==Regards, Hristian Stefanov Progress Telerik
