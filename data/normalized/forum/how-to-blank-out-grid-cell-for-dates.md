# How to blank out grid cell for dates?

## Question

**Kev** asked on 14 Aug 2023

I have a grid that has a couple of dateonly fields. There can be dates or null for the data supplying the information. Which ends up looking like this: I would rather see blank than 1/1/0001, but I am not sure how to do this. Here is the code for the grid: <TelerikGrid TItem="EngineModel" Data="@EngineShowList" EditMode="@GridEditMode.Inline" OnEdit="@EditHandler" OnUpdate="@UpdateHandler" @ref="@Grid"> <GridColumns> <GridColumn Field="ProductionLine.EffectiveGuid" Title="EffectiveGuid" FieldType="@typeof(Guid)" Editable="false" Visible="false" /> <GridColumn Field="ProductionLine.EffectiveFrom" Title="From" FieldType="@typeof(DateOnly)" Editable="true" Width="20%"> <EditorTemplate> <TelerikDatePicker Id="EffFromDate" @bind-Value="@SelectedFromDate" DebounceDelay="250" Min="@Min" Max="@Max"> </TelerikDatePicker> </EditorTemplate> </GridColumn> How would I get the display to just show blank for 1/1/0001? Thanks!

## Answer

**Hristian Stefanov** answered on 15 Aug 2023

Hi Kevin, I'm ready to shed some light on the situation and help you achieve your goal quickly. To ensure an empty cell when the date is null and to avoid displaying the default date (1/1/0001), a key step is to grant the " From " and " To " properties nullable types. You can accomplish this by appending a question mark at the end of their type declarations. For instance: " public DateOnly? From { get; set; } ". However, while the aforementioned question mark grants the properties nullability, our Grid system currently lacks compatibility with the DateOnly type. We already have an open feature request for introducing support for DateOnly and TimeOnly structures in conjunction with their respective pickers. It has already gained enough popularity, so it is likely that we include it in our short-term backlog. Hence, in the present scenario, my recommended approach involves leveraging the DateTime type along with templates. This combination enables you to exhibit either a vacant cell or only a date without hours, or even personalized text in instances of absence. I have prepared an example for you: @using System.ComponentModel.DataAnnotations <TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" OnUpdate="@UpdateHandler" OnCancel="@CancelHandler"> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Title="ID" Editable="false" /> <GridColumn Field=@nameof(SampleData.From) Title="From"> <Template> @if (((context as SampleData).From) !=null)
{
@(((context as SampleData).From.Value).ToShortDateString())
} </Template> </GridColumn> <GridColumn Field=@nameof(SampleData.To) Title="To"> <Template> @if (((context as SampleData).To) !=null)
{
@(((context as SampleData).To.Value).ToShortDateString())
}
else
{
@("Set Date..")
} </Template> </GridColumn> <GridColumn Field=@nameof(SampleData.Name) Title="Name" /> <GridCommandColumn> <GridCommandButton Command="Edit"> Edit </GridCommandButton> <GridCommandButton Command="Save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @code {
async Task UpdateHandler(GridCommandEventArgs args)
{
SampleData item=(SampleData)args.Item;

await MyService.Update(item);

await GetGridData();
}

async Task CancelHandler(GridCommandEventArgs args)
{
SampleData item=(SampleData)args.Item;
}

public class SampleData
{
public int ID { get; set; }
[Required]
public string Name { get; set; }
public DateTime? From { get; set; }
public DateTime? To { get; set; }
}

public List <SampleData> MyData { get; set; }

async Task GetGridData()
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

public static async Task Create(SampleData itemToInsert)
{
itemToInsert.ID=_data.Count + 1;
_data.Insert(0, itemToInsert);
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
From=i % 2==0 ? null : DateTime.Now,
To=i % 2 !=0 ? null : DateTime.Now
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

public static async Task Delete(SampleData itemToDelete)
{
_data.Remove(itemToDelete);
}
}
} I'm looking forward to your feedback on whether this aligns with your requirements. If it doesn't meet your needs, please know that I am fully available to provide further assistance in order to help you achieve your desired outcome. Regards, Hristian Stefanov Progress Telerik

### Response

**Kevin** commented on 15 Aug 2023

I think that will work... I would like to use DateOnly, but I understand the limitations for the current version. Thank you!

### Response

**Hristian Stefanov** commented on 15 Aug 2023

Hi Kevin, Thank you for sharing your feedback and for your understanding. You can also subscribe to the public item of the feature request by clicking the "Follow" button to receive email notifications for status updates. Kind Regards, Hristian
