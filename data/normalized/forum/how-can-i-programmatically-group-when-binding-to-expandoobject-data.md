# How can I programmatically group when binding to ExpandoObject data?

## Question

**Ken** asked on 15 Jun 2022

I'm trying to define pre-set groupings for my data on known columns in my dataset. But whenever I try and set the @ref property on the TelerikGrid I get the following build error. I've defined the TelerikGrid object in the @code section TelerikGrid<List<ExpandoObject>>? Grid { get; set; } I've declared the Data property on the TelerikGrid as being bound to List<ExpandoObject> @if (model is not null && model.DegradeTableRows is not null && model.DegradeTableRows.Any())
{ <TelerikGrid Data="@model.DegradeTableRows" Width="100%" Height="100%" Groupable="true" Pageable="false" Sortable="true" FilterMode="@GridFilterMode.FilterMenu"> <GridAggregates> <GridAggregate Field="Total Pieces" FieldType="@typeof(decimal)" Aggregate="@GridAggregateType.Sum" /> <GridAggregate Field="Total % Total" FieldType="@typeof(decimal)" Aggregate="@GridAggregateType.Sum" /> </GridAggregates> <GridColumns> <GridColumn Field="category" Width="110px" FieldType="@typeof(string)" Title="Category" /> <GridColumn Field="month" Width="100px" Title="Month" FieldType="@typeof(DateTime)" DisplayFormat="{0:d}" /> <GridColumn Field="rank" Width="80px" FieldType="@typeof(int)" Title="Rank" /> <GridColumn Field="reason" FieldType="@typeof(string)" Title="Reason" /> @if (LengthColumnNames is not null && LengthColumnNames.Any())
{
foreach (var lengthColumnName in LengthColumnNames)
{ <GridColumn Width="75px" Field="@lengthColumnName" FieldType="@typeof(decimal)" Title="@lengthColumnName" /> }
} <GridColumn Field="Total Pieces" FieldType="@typeof(decimal)" Title="Total Pieces" /> <GridColumn Field="Total % Total" FieldType="@typeof(decimal)" Title="Total % Total" /> </GridColumns> </TelerikGrid> } So I don't know why I'm getting the errors when I try to build. I'd need to group the data when the grid comes up var desiredState=new GridState<List<ExpandoObject>>()
{
GroupDescriptors=new List<GroupDescriptor>()
{ new GroupDescriptor()
{
Member="month",
MemberType=typeof (DateTime)
}
} // end new list of group descriptors }; // end new grid state if (Grid is not null )
{ await Grid.SetState(desiredState);
} If I add the @ref="@Grid" property to the Grid definition, I get the build error. I can comment out the code to set the group state and I still get the build error. Is there a way around this?

### Response

**Marin Bratanov** commented on 18 Jun 2022

Have you tries using "object" as the TItem when grouping with OnRead like explained here?
