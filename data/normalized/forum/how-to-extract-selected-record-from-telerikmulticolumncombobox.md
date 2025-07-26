# How to extract selected record from TelerikMultiColumnComboBox

## Question

**Pet** asked on 06 Sep 2024

Hello Telerik, How do I feed the selected record from the TelerikMultiColumnComboBox to my custom Component? Do I utilize the ValueMapper="@GetGeneratorRecord" somehow? Thank you <ComGenerator Generator="GetGeneratorRecord" /> @page "/"
@inject SerOHRDatabase serOHRDatabase
@using Telerik.DataSource
@using Telerik.DataSource.Extensions <div> Generator Name Search: </div> <TelerikMultiColumnComboBox TItem="ModtblGenerator" TValue="int" ValueField="@nameof(ModtblGenerator.Id)" TextField="@nameof(ModtblGenerator.GenName)" Filterable="true" @bind-Value="@intSelectedGenID" ItemHeight="260" ListHeight="28" PageSize="15" ScrollMode="@DropDownScrollMode.Virtual" OnRead="@ReadItems" ValueMapper="@GetGeneratorRecord" Width="250px"> <MultiColumnComboBoxColumns> <MultiColumnComboBoxColumn Field="@nameof(ModtblGenerator.GenName)" Title="Gen Name" HeaderClass="header" Class="genNameCell" Width="250px"> </MultiColumnComboBoxColumn> <MultiColumnComboBoxColumn Field="@nameof(ModtblGenerator.GenNum)" Title="Gen Num" HeaderClass="header" Width="150px"> </MultiColumnComboBoxColumn> </MultiColumnComboBoxColumns> </TelerikMultiColumnComboBox> <ComGenerator Generator="GetGeneratorRecord" /> <p> Selected product Id: @intSelectedGenID </p> @code {

List <ModtblGenerator> lstGenerators;
int intSelectedGenID;

protected async Task ReadItems(MultiColumnComboBoxReadEventArgs args)
{
await LoadData();

var result=lstGenerators.ToDataSourceResult(args.Request);
args.Data=result.Data;
args.Total=result.Total;
}

private async Task LoadData()
{
if (lstGenerators==null)
{
lstGenerators=await serOHRDatabase.GetAllGenerators();
}
}

protected Task <ModtblGenerator> GetGeneratorRecord(int intSelectedGenID)
{
return Task.FromResult(lstGenerators.FirstOrDefault(x=> x.Id==intSelectedGenID));
}
} <style>.header { font-weight: bold; color: black;
}.genNameCell { color: darkblue; font-weight: bolder;
} </style>

## Answer

**Tsvetomir** answered on 06 Sep 2024

Hello Peter, To achieve the desired result a ValueMapper is not required. The main point of the required approach here is to use the unique identifier you get from the component after the selection of an item. To see in more detail this approach, check our KB article: Get Model from Drop Down. I hope this serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik

### Response

**Peter** commented on 07 Sep 2024

Thank you Tsvetomir
