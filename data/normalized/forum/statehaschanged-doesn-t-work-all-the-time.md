# StateHasChanged doesn't work all the time

## Question

**Mau** asked on 07 Sep 2022

Hi, I have a blazor grid which works in the following simplified way public class modelVm { public int Id { get; set;}
} protected override void OnInitialized ( ) {
griddate=new List<modelVm>;
} protected override async Task OnAfterRenderAsync ( bool firstRender ) {
griddata. add ( new ModelVm{Id=1 });
StateHasChanged();
} And on the razor page itself <TelerikGrid Data="@GridData" AutoGenerateColumns="true" /> If I debug the code I can see giddata has 1 item but the grid isn't showing it. The strangest thing is that I have other grids using the same code and they work. But all new code doesn't. Even a copy/paste of an old razor page and changing the modelVm will result in not refreshing the telerik Grid. If I put on the razor page a @griddata.count you will see that the griddata has 1 item. Does somebody has any idea?

### Response

**Maurice** commented on 07 Sep 2022

moving griddata. add ( new ModelVm{Id=1 }); to protected override void OnInitialized () Does help but I can't understand why it doesn't work with the OnAfterRenderAsync. I have used it on several other grids where it works

### Response

**Maurice** commented on 07 Sep 2022

If I get my data in the OnAfterRenderAsync it does work if I use GridRef?. Rebind ();

## Answer

**Svetoslav Dimitrov** answered on 12 Sep 2022

Hello Maurice, The best way to refresh the data of the Grid is to use the Rebind() method from the Grid reference. Adding a new item to a collection would not change the reference of that collection and the Blazor framework is not aware that any change occurred - thus it does not render the Grid anew. You can see other options to refresh the Grid's data from the Refresh Data article. Regards, Svetoslav Dimitrov
