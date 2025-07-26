# Can I set grid grouping and collapse on initialization?

## Question

**Jas** asked on 22 Jun 2020

Good Afternoon, I am building an elections app. I would like to use the Telerik Grid to display the candidates and votes. Each candidate will have a table row/record for each precinct vote tally. I have set the ability to group and to group by the candidate column. However I have to click/drag manually to group the candidates. What I would like is when the page loads is a listing of each candidate grouping with a footer of the total vote count in a collapsed state. Then the user if they want to see a breakdown of the votes by precinct, they can expand the candidate. Can I setup the grid to do be in this state programatically? If so, can you get me pointed in the right direction? Below is my grid <TelerikGrid Data="@officeList" Groupable="true"> <GridAggregates> <GridAggregate Field="@(nameof(VotingMainModel.Votes))" Aggregate="@GridAggregateType.Sum" /> </GridAggregates> <GridColumns> <GridColumn Field="@(nameof(VotingMainModel.Candidate))" Title="Candidate" Groupable="true" /> <GridColumn Field="@(nameof(VotingMainModel.Affiliation))" Title="Affiliation" /> <GridColumn Field="@(nameof(VotingMainModel.Precinct))" Title="Precinct" /> <GridColumn Field="@(nameof(VotingMainModel.Votes))" Title="Votes"> <GroupFooterTemplate> Total Votes: <strong>@context.Sum</strong> </GroupFooterTemplate> </GridColumn> </GridColumns> </TelerikGrid>

## Answer

**Marin Bratanov** answered on 22 Jun 2020

Hello Jason, You can do that through the grid state: [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) While I encourage you to review the entire article to get an idea of all the other capabilities this provides you with, the shortcut to your goal is: use the OnStateInit event to set default state (there is a sample about using it in the article) set the desired grouping (there is a sample about choosing grouping futher down) instead of deserializing it from some storage Unfortunately, there is a bug in the aggregates when set from the state init event and you can Follow it here: [https://feedback.telerik.com/blazor/1470690-aggregates-don-t-work-when-grouping-is-set-in-onstateinit.](https://feedback.telerik.com/blazor/1470690-aggregates-don-t-work-when-grouping-is-set-in-onstateinit.) I've added your Vote to it to raise its priority. So, here's the main concept with a workaround for this issue: @using Telerik.DataSource;

<TelerikGrid Data="@MyData" Groupable="true" @ref="@GridRef" Pageable="true" PageSize="40" FilterMode="@GridFilterMode.FilterMenu" OnStateInit="@((GridStateEventArgs<VotingMainModel> args)=> OnStateInitHandler(args))">
<GridColumns>
<GridColumn Field="@nameof(VotingMainModel.Votes)">
<GroupFooterTemplate>
Total Votes: <strong>@context.Sum</strong>
</GroupFooterTemplate>
</GridColumn>
<GridColumn Field="@(nameof(VotingMainModel.Name))" Title="Candidate Name" />
<GridColumn Field="@(nameof(VotingMainModel.Precinct))" Title="Precinct" />
</GridColumns>
<GridAggregates>
<GridAggregate Field="@(nameof(VotingMainModel.Votes))" Aggregate="@GridAggregateType.Sum" />
</GridAggregates>
</TelerikGrid>

@code { // when [https://feedback.telerik.com/blazor/1470690-aggregates-don-t-work-when-grouping-is-set-in-onstateinit](https://feedback.telerik.com/blazor/1470690-aggregates-don-t-work-when-grouping-is-set-in-onstateinit) // is fixed, you can use that handler again, for the time being, use the workaround through OnAfterRender async Task OnStateInitHandler ( GridStateEventArgs<VotingMainModel> args ) { //GridState<VotingMainModel> desiredState=GetDesiredInitialState(); //args.GridState=desiredState; } // start workaround TelerikGrid<VotingMainModel> GridRef { get; set; } protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{ await GridRef.SetState(GetDesiredInitialState());
}
} GridState<VotingMainModel> GetDesiredInitialState ( ) { return new GridState<VotingMainModel>()
{
GroupDescriptors=new List<GroupDescriptor>()
{ new GroupDescriptor()
{
Member="Name",
MemberType=typeof ( string )
}
},
CollapsedGroups=Enumerable.Range( 0, 9 ).ToList() // first 10 groups to be collapsed - you can increase to however many candidates you may habe on the first page };
} //end workaround // sample data follows below public IEnumerable<VotingMainModel> MyData=Enumerable.Range( 1, 30 ).Select(x=> new VotingMainModel
{
Id=x,
Name="Candidate " + (x % 4 ),
Precinct="Precinct " + (x % 5 ),
Votes=x,
}); public class VotingMainModel { public int Id { get; set; } public string Name { get; set; } public string Precinct { get; set; } public int Votes { get; set; }
}
} Regards, Marin Bratanov

### Response

**Jason** answered on 22 Jun 2020

This is exactly what I was looking for and it works perfectly Marin! Thank you for your time! I also now see the Group Grid From code section in the documentation which was also helpful. I totally missed that!
