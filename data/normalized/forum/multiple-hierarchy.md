# Multiple Hierarchy

## Question

**Mic** asked on 04 Oct 2019

I'm trying to see more than 1 level of hierarchy in my grid but i don't know how i would to such a thing with the current infrastructure. any idea?

## Answer

**Marin Bratanov** answered on 04 Oct 2019

Hello Michael, If you put a grid in the DetailTemplate of the first grid, you should be able to use its own DetailTemplate to provide further hierarchy. Are you facing issues with this approach? Regards, Marin Bratanov

### Response

**Michael** answered on 08 Oct 2019

I've attached a screenshot of what happened when i first try this solution.

### Response

**Marin Bratanov** answered on 08 Oct 2019

Hello Michael, When nesting RenderFragments, you should name their context variables, so that the framework can tell them apart. Here's an example I made for you that seems to work as expected (a screenshot of the result is attached at the end of this message): <TelerikGrid Data="salesTeamMembers">
<DetailTemplate Context="employeeItem">
@{ var employee=employeeItem as MainModel;
<TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5">
<GridColumns>
<GridColumn Field="OrderId"></GridColumn>
<GridColumn Field="DealSize"></GridColumn>
</GridColumns>
<DetailTemplate Context="orderInfo">
<TelerikGrid Data=" orderInfo.ShippingHistory">
<GridColumns>
<GridColumn Field="HistoryItem"></GridColumn>
</GridColumns>
</TelerikGrid>
</DetailTemplate>
</TelerikGrid>
}
</DetailTemplate>
<GridColumns>
<GridColumn Field="Id"></GridColumn>
<GridColumn Field="Name"></GridColumn>
</GridColumns>
</TelerikGrid>

@code {
List<MainModel> salesTeamMembers { get; set; } protected override void OnInitialized ( ) {
salesTeamMembers=GenerateData();
} private List<MainModel> GenerateData ( ) {
List<MainModel> data=new List<MainModel>(); for ( int i=0; i <5; i++)
{
MainModel mdl=new MainModel { Id=i, Name=$"Name {i} " };
mdl.Orders=Enumerable.Range( 1, 15 ).Select(x=> new DetailsModel { OrderId=x, DealSize=x ^ i }).ToList(); foreach (DetailsModel item in mdl.Orders)
{
List<ThirdLevel> history=new List<ThirdLevel>(); for ( int j=0; j <5; j++)
{
history.Add( new ThirdLevel { HistoryItem=$"step {j} for Order {item.OrderId} " });
}
item.ShippingHistory=history;
}
data.Add(mdl);
} return data;
} public class MainModel { public int Id { get; set; } public string Name { get; set; } public List<DetailsModel> Orders { get; set; }
} public class DetailsModel { public int OrderId { get; set; } public double DealSize { get; set; } public List<ThirdLevel> ShippingHistory { get; set; }
} public class ThirdLevel { public string HistoryItem { get; set; }
}
} Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 09 Oct 2019

Hello, I am writing to let everyone stumbling on this thread know that the example of multi-level hierarchy is available in the following KB article: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-three-level-hierarchy](https://docs.telerik.com/blazor-ui/knowledge-base/grid-three-level-hierarchy) and more details on nesting RenderFragment content is available in this KB article: [https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment](https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment) Regards, Marin Bratanov
