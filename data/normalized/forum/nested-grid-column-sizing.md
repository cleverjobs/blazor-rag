# Nested Grid column sizing

## Question

**EdEd** asked on 23 Nov 2020

Hello, I'm having trouble getting nested grid and or column sizes to work. If we use this as our example: [https://docs.telerik.com/blazor-ui/components/grid/hierarchy](https://docs.telerik.com/blazor-ui/components/grid/hierarchy) The nested grid, DetailTemplate, when expanded fills the row space as defined by the parent grid. Even if I add Width parameters to the DetailTemplate Grid and GridColumn controls the DetailTemplate Grid and columns still fill the row space. Looks funny to me to have the OrderId and DealSize columns in the DetailTemplate to be so large. Is it possible to size the DetailTemplate Grid and column more appropriatly? Thanks

## Answer

**Marin Bratanov** answered on 23 Nov 2020

Hi Ed, The grid takes the available width by default, and its columns take the width of the grid too (see more on the behavior of column widths in the docs, as there are several cases depending on the configuration: [https://docs.telerik.com/blazor-ui/components/grid/columns/width](https://docs.telerik.com/blazor-ui/components/grid/columns/width) ). Thus, setting the Width of the nested grid can let you reduce its size, for example (screenshot of the result is attached): Click the + icon to expand the row details

<TelerikGrid Data="salesTeamMembers">
<DetailTemplate>
@{ var employee=context as MainModel;
<TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5" Width="200px">
<GridColumns>
<GridColumn Field="OrderId"></GridColumn>
<GridColumn Field="DealSize"></GridColumn>
</GridColumns>
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
mdl.Orders=Enumerable.Range( 1, 15 ).Select(x=> new DetailsModel { OrderId=x, DealSize=x ^ i }).ToList();
data.Add(mdl);
} return data;
} public class MainModel { public int Id { get; set; } public string Name { get; set; } public List<DetailsModel> Orders { get; set; }
} public class DetailsModel { public int OrderId { get; set; } public double DealSize { get; set; }
}
} Regards, Marin Bratanov

### Response

**Ed** answered on 23 Nov 2020

Rookie mistake, I coded the width as "200" and not "200px" Let me echo as so many people have, how impressed I am with customer support from you guys. We have bid the Blazor UI components on a recent opportunity and I'm looking forward to bidding them on more opportunities as we go forward :) Thanks again.

### Response

**Marin Bratanov** answered on 23 Nov 2020

Glad to see you moving forward, Ed! Thank you for the kind words, I will make sure the team sees your post :) Regards, Marin Bratanov
