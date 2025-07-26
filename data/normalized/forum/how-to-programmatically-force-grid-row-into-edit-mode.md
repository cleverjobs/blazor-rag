# How to programmatically force grid row into edit mode?

## Question

**Kev** asked on 31 Jul 2023

I have code that updates the data source for my grid. However I would like the grid to go into edit mode for the new row of data that got added. Is there a way to do this programmatically with out the user having to click the row edit button?

## Answer

**Hristian Stefanov** answered on 01 Aug 2023

Hi Kevin, I confirm that achieving the desired outcome is entirely feasible by utilizing the Grid state, which allows you to programmatically force the desired row into edit mode. To make it easier for you, I've prepared an example showcasing the approach: @using Telerik.FontIcons <TelerikButton OnClick="@UpdateDataSource "> Update DataSource in Grid </TelerikButton> <br /> <br /> <TelerikGrid Data="@MyData" Height="400px" Pageable="true" EditMode="@GridEditMode.Inline" OnUpdate="@UpdateHandler" @ref="@GridRef"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Editable="false" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridCommandColumn> <GridCommandButton Command="Save" Icon="@FontIcon.Save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="@FontIcon.Pencil"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="@FontIcon.Trash"> Delete </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@FontIcon.Cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @code {
public TelerikGrid <SampleData> GridRef { get; set; } void UpdateDataSource()
{
MyData.Add(new SampleData { Id=MyData.Last().Id + 1 });
MyData=new List <SampleData> (MyData); var updatedItem=MyData.Last();
EditItem(updatedItem); } void EditItem(SampleData item)
{
var currState=GridRef.GetState();
currState.InsertedItem=null;
currState.EditItem=null;
currState.OriginalEditItem=null;

SampleData itemToEdit=SampleData.GetClonedInstance(MyData.FirstOrDefault(x=> x.Id==item.Id));

currState.EditItem=itemToEdit;
currState.OriginalEditItem=item;
GridRef.SetStateAsync(currState);
} async Task UpdateHandler(GridCommandEventArgs args)
{
SampleData itemToUpdate=args.Item as SampleData;
int itemIndex=MyData.IndexOf(itemToUpdate);
if (itemIndex> -1)
{
MyData[itemIndex]=itemToUpdate;
}
}

public List <SampleData> MyData=Enumerable.Range(1, 5).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
}).ToList();

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }

// The new object we create for the state must be able to match an object from the current data
public override bool Equals(object obj)
{
if (obj is SampleData)
{
return this.Id==(obj as SampleData).Id;
}
return false;
}

public SampleData()
{

}

public SampleData(SampleData itmToClone)
{
this.Id=itmToClone.Id;
this.Name=itmToClone.Name;
Team=itmToClone.Team;
}

public static SampleData GetClonedInstance(SampleData itmToClone)
{
return new SampleData(itmToClone);
}
}
} Please run and test it to verify if it addresses your needs. I remain at your disposal if you face any further difficulties during the testing phase. Regards, Hristian Stefanov Progress Telerik

### Response

**Kevin** commented on 01 Aug 2023

Thank you! That worked perfectly!

### Response

**Kevin** answered on 01 Aug 2023

That works! Thank you!
