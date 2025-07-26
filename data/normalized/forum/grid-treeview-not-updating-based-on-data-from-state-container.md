# Grid/TreeView not updating based on data from state container

## Question

**Sim** asked on 29 Sep 2019

I'm using a state container to basically one-way bind the data to the state container (see [https://www.youtube.com/watch?v=KlPaM0yWWbQ).](https://www.youtube.com/watch?v=KlPaM0yWWbQ).) I cannot use to CascadingParameter because the code would trigger unnecessary UI updates, so State Container serves my purposes perfectly. Generally, the blazor code w/ the Grid is: <TelerikGrid Data="@Elements" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow"> <GridColumns> <GridColumn Field="@(nameof(ClaimObject.Text))" Title="Text" /> </GridColumns> </TelerikGrid> @code { protected override void OnInitialized() { AppState.StateChanged +=OnClaimStateChange; } public List<ClaimObject> Elements=> AppState.GetElements(); void OnClaimStateChange(object sender, EventArgs e)=> StateHasChanged(); } When the first ClaimObject is added, the grid refreshes. However, adding any subsequent ClaimObjects does not update the UI. Conversely, the following code updates every time: foreach (var element in Elements) { <div>@element.Text</div> } Both Grid and TreeView are updating working this way. Any suggestions to get the grid to refresh when the State Container updates the data?

## Answer

**Simon** answered on 30 Sep 2019

And upon further testing, if I search for test in the grid, it refreshes and shows all the data.

### Response

**Simon** answered on 30 Sep 2019

I see my error. I should have known this, I was not using a collection that implemented INotifyCollectionChanged. Got that working, and the UI updates perfectly.

### Response

**Marin Bratanov** answered on 01 Oct 2019

Hi Simon, Indeed, an observable collection is the answer for this, although it may not always be obvious. So, I marked your last post as an answer to this thread for others who may encounter the same issue. Regards, Marin Bratanov
