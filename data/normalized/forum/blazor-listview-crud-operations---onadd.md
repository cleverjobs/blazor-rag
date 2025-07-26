# Blazor ListView CRUD operations - OnAdd

## Question

**Dee** asked on 13 Feb 2024

Hi, I couldn't find OnAdd event for Blazor Listview component CRUD operations(like the one available for Grid) . I would like to initialize certain properties of the model when 'Add' button is clicked, is there any other workaround? Thanks, Deepa

## Answer

**Hristian Stefanov** answered on 14 Feb 2024

Hi Deepa, To handle the click on the Add action button, you can leverage its OnClick event. The absence of a dedicated OnAdd event in the ListView is by design, as clicking the Add action typically doesn't require additional arguments, unlike the other available actions. I have prepared an example for you that demonstrates how you can handle this: @using Telerik.SvgIcons <TelerikListView Data="@ListViewData" Pageable="true" OnCreate="@CreateHandler" OnDelete="@DeleteHandler" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnCancel="@CancelHandler"> <EditTemplate> <div style="border: 1px solid green; margin: 10px; padding: 10px; display: inline-block;"> <TelerikTextBox @bind-Value="@context.Name" DebounceDelay="0" /> <br /> <TelerikDropDownList Data="@Teams" @bind-Value="@context.Team" /> <ListViewCommandButton Command="Save" Icon="@SvgIcon.Save"> Save </ListViewCommandButton> <ListViewCommandButton Command="Cancel" Icon="@SvgIcon.Cancel"> Cancel </ListViewCommandButton> </div> </EditTemplate> <Template> <div style="border: 1px solid black; margin: 10px; padding: 10px; display: inline-block;"> Employee: @context.Id <br /> Name: @context.Name in team: @context.Team <ListViewCommandButton Command="Edit" Icon="@SvgIcon.Pencil"> Edit </ListViewCommandButton> <ListViewCommandButton Command="Delete" Icon="@SvgIcon.Trash"> Delete </ListViewCommandButton> </div> </Template> <HeaderTemplate> <ListViewCommandButton Command="Add" Icon="@SvgIcon.Plus" OnClick="@HandleOnAdd"> Add Employee </ListViewCommandButton> </HeaderTemplate> </TelerikListView> @code {
private List <Employee> ListViewData { get; set; }
private List <string> Teams { get; set; } private async Task HandleOnAdd()
{
//Your OnAdd logic here
} private async Task UpdateHandler(ListViewCommandEventArgs args)
{
Employee item=(Employee)args.Item;

await MyService.Update(item);

await GetListViewData();
}

private async Task DeleteHandler(ListViewCommandEventArgs args)
{
Employee item=(Employee)args.Item;

await MyService.Delete(item);

await GetListViewData();
}

private async Task CreateHandler(ListViewCommandEventArgs args)
{
Employee item=(Employee)args.Item;

await MyService.Create(item);

await GetListViewData();
}

private async Task EditHandler(ListViewCommandEventArgs e)
{
Employee currItem=e.Item as Employee;
}

private async Task CancelHandler(ListViewCommandEventArgs e)
{
Employee changedItem=e.Item as Employee;
}

private async Task GetListViewData()
{
ListViewData=await MyService.Read();
Teams=await MyService.GetTeams();
}

protected override async Task OnInitializedAsync()
{
await GetListViewData();
}

public class Employee
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
}

public static class MyService
{
private static List <Employee> _data { get; set; }=new List <Employee> ();
private static List <string> _teams=new List <string> { "Sales", "Dev", "Support" };

public static async Task Create(Employee itemToInsert)
{
itemToInsert.Id=_data.Count + 1;
_data.Insert(0, itemToInsert);
}

public static async Task<List <Employee>> Read()
{
if (_data.Count <1)
{
for (int i=1; i <50; i++)
{
_data.Add(new Employee()
{
Id=i,
Name=$"Name {i}",
Team=_teams[i % _teams.Count]
});
}
}

return await Task.FromResult(_data);
}

public static async Task<List <string>> GetTeams()
{
return await Task.FromResult(_teams);
}

public static async Task Update(Employee itemToUpdate)
{
var index=_data.FindIndex(i=> i.Id==itemToUpdate.Id);
if (index !=-1)
{
_data[index]=itemToUpdate;
}
}

public static async Task Delete(Employee itemToDelete)
{
_data.Remove(itemToDelete);
}
}
} Let me know if this approach meets your requirements or if you have any specific considerations. Regards, Hristian Stefanov Progress Telerik
