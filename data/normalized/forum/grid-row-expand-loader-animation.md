# Grid row expand loader animation?

## Question

**Dea** asked on 15 Jun 2023

So I have a grid with a subgrid. Sometimes the subgrid has enough data rows that it seems to the user the grid is doing nothing when in fact tis still getting ready to display its subgrid contents. I was wondering if there was a way to show the Loader object when these rows are taking a bit to show up?

## Answer

**Hristian Stefanov** answered on 20 Jun 2023

Hi Deasun, I confirm that the desired result is achievable. By utilizing our LoaderContainer component within the OnRowExpand event handler of the Grid, you can easily accomplish your goal. To assist you further, I have prepared an example for you in this REPL link. Please run and test it to observe the desired outcome firsthand. I hope the information provided above addresses your requirements. Should you need to tailor the approach based on your specific data operations, you have the flexibility to do so. If you encounter any difficulties during the testing phase or have any additional questions, please don't hesitate to reach out. I am readily available to assist you. Regards, Hristian Stefanov

### Response

**Deasun** commented on 21 Jun 2023

Can you post your REPL code in forum? Those links never work. All I get on clicking on them is a blank REPL window.

### Response

**Hristian Stefanov** commented on 21 Jun 2023

Hi Deasun, I'm sorry for any inconvenience the problematic link caused. Here is the code from REPL: <TelerikGrid Data="salesTeamMembers" OnRowExpand="@OnRowExpandHandler"> <DetailTemplate> @{
var employee=context as MainModel; <TelerikLoaderContainer Visible="@ShowLoader" Text="Please wait..." /> <TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"> </GridColumn> <GridColumn Field="Name"> </GridColumn> </GridColumns> </TelerikGrid> @code {
bool ShowLoader{ get; set; }

async Task OnRowExpandHandler(GridRowExpandEventArgs args)
{
MainModel item=args.Item as MainModel;

if (item.Orders==null)
{
ShowLoader=true;
await Task.Delay(3000);
item.Orders=await GenerateOrdersData(item.Id);
ShowLoader=false;
}
}

async Task<List <DetailsModel>> GenerateOrdersData(int id)
{
var data=new List <DetailsModel> ()
{
new DetailsModel()
{
OrderId=id,
DealSize=id * 1234,
}
};

return await Task.FromResult(data);
}

List <MainModel> salesTeamMembers { get; set; }

protected override void OnInitialized()
{
salesTeamMembers=GenerateData();
}

private List <MainModel> GenerateData()
{
List <MainModel> data=new List <MainModel> ();
for (int i=1; i <=5; i++)
{
MainModel mdl=new MainModel { Id=i, Name=$"Name {i}" };
data.Add(mdl);
}
return data;
}

public class MainModel
{
public int Id { get; set; }
public string Name { get; set; }
public List <DetailsModel> Orders { get; set; }
}

public class DetailsModel
{
public int OrderId { get; set; }
public double DealSize { get; set; }
}
} Kind Regards, Hristian
