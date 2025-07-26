# Placing a second Grid Command Button to the right of the Grid Toolbar Template?

## Question

**Joh** asked on 12 Nov 2024

I would like to place a second button on the Grid Toolbar. That button should reside to the right side of the Toolbar so that the GridCommandButton for Add is on the far left and my second button should be on the far right. What is the best/proper way to do this on the Blazor Grid?

## Answer

**Hristian Stefanov** answered on 13 Nov 2024

Hi John, To place a second button on the right side of the Grid Toolbar while keeping the GridCommandButton "Add" on the left, you can use a combination of a container for the toolbar content and CSS for styling. Here's how you can achieve this: <style>.toolbar-container { display: flex; justify-content: space-between; width: 100%;
} </style> <TelerikGrid Data=@MyData Pageable="true" PageSize="15" EditMode="@GridEditMode.Inline" Height="500px" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler"> <GridToolBarTemplate> <div class="toolbar-container"> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus"> Add Employee </GridCommandButton> <TelerikButton Class="custom-button" OnClick="CustomButtonClick"> Custom Action </TelerikButton> </div> </GridToolBarTemplate> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="Employee ID" /> <GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" /> <GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" /> <GridCommandColumn> <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil"> Edit </GridCommandButton> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @code {
private List <SampleData> MyData { get; set; }

private void CustomButtonClick()
{
// Custom button action logic
}

private async Task UpdateHandler(GridCommandEventArgs args)
{
SampleData item=args.Item as SampleData;

SampleData updatedItem=await MyService.Update(item);

await GetGridData();
}

private async Task CreateHandler(GridCommandEventArgs args)
{
SampleData item=args.Item as SampleData;

SampleData insertedItem=await MyService.Create(item);

await GetGridData();
}

public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

private async Task GetGridData()
{
MyData=await MyService.Read();
}

protected override async Task OnInitializedAsync()
{
await GetGridData();
}

public static class MyService
{
private static List <SampleData> _data { get; set; }=new List <SampleData> ();

public static async Task <SampleData> Create(SampleData itemToInsert)
{
itemToInsert.ID=_data.Count + 1;
_data.Insert(0, itemToInsert);

return await Task.FromResult(itemToInsert);
}

public static async Task<List <SampleData>> Read()
{
if (_data.Count <1)
{
for (int i=1; i <50; i++)
{
_data.Add(new SampleData()
{
ID=i,
Name="Name " + i.ToString(),
HireDate=DateTime.Now.AddDays(-i)
});
}
}

return await Task.FromResult(_data);
}

public static async Task <SampleData> Update(SampleData itemToUpdate)
{
var index=_data.FindIndex(i=> i.ID==itemToUpdate.ID);
if (index !=-1)
{
_data[index]=itemToUpdate;
return await Task.FromResult(_data[index]);
}

throw new Exception("no item to update");
}
}
} Regards, Hristian Stefanov Progress Telerik
