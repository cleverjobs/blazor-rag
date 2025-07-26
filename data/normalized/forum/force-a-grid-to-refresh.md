# Force a Grid to Refresh

## Question

**Col** asked on 07 Jan 2020

I know there is a refresh method in the works, but is there anyway say I can have a button click even cause a Grid to redraw? I played with the StateHasChanged method but no love yet.

## Answer

**Marin Bratanov** answered on 08 Jan 2020

Hi Collin, You can bind the grid to an observable collection which will let the data notify the grid of changes: [https://demos.telerik.com/blazor-ui/grid/observable-data.](https://demos.telerik.com/blazor-ui/grid/observable-data.) To change the entire data collection, .Clear() the collection first to notify the grid that this old data is gone, then create a new one with the new data. A similar example is available in the selection docs: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview#observable-collections](https://docs.telerik.com/blazor-ui/components/grid/selection/overview#observable-collections) Regards, Marin Bratanov

### Response

**Nick** answered on 13 Jan 2020

Hi Marin, I hope you don't mind me jumping in on this thread, but I was about to ask the same question. In my case I'm using manual data operations. I don't think the observable workaround works in this scenario. I just wanted to mention it in case it so this scenario can be taken into account with the refresh method if one is implemented! Thanks. Nick.

### Response

**Nick** answered on 13 Jan 2020

Excuse the bad English, I was trying to phrase the question, what I meant in the last sentence was: "I just wanted to mention it so this scenario can be taken into account with the refresh method if one is implemented!

### Response

**Marin Bratanov** answered on 14 Jan 2020

Hi guys, Nick, of course you are welcome to join the discussion, that's the goal of the forums. I must begin by saying that at this stage the data update that was implemented was through an ObservableCollection, and a .Refresh() method did not seem to have merits, so it was not implemented. Details: [https://feedback.telerik.com/blazor/1409112-the-grid-does-not-update-on-data-source-change](https://feedback.telerik.com/blazor/1409112-the-grid-does-not-update-on-data-source-change) I also made the following KB article that explains how you can refresh a grid, observable collections always work for me: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-force-refresh.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-force-refresh.) Please try the approach from the KB and let me know if you experience issues. Regards, Marin Bratanov

### Response

**Nick** answered on 23 Jan 2020

Hi Marin, I got around my issue by wrapping the grid in an @if(_drawgrid==true) statement and then swapping it from to false and then back to true with a StateHasChanged() call between each. This seems to force it to re-render. Not ideal, but did the trick, just in case it helps anyone! Thanks, Nick.

### Response

**Matt** commented on 10 Sep 2021

This is the only way I could get my grid to re-render. In my case, the data was clearly being refreshed and when I changed pages, the updated rows would display; meaning, definitely a rendering problem. Wrapping the entire grid in an @If block forced the issue. FWIW, this grid is paged, running in a nested component, with the data being updated inside the OnParametersSetAsync method of the component.

### Response

**Jonathan** commented on 05 Aug 2024

Same issue here. Grid not re-rendering from either Rebind() or StateHasChanged(), even though the results were read. Forcing a redraw as Nick did got around the problem. This is a bug and something Telerik needs to fix. Most of the suggestions and responses below are about other issues not relevant to the bug.

### Response

**Jeff** answered on 03 Feb 2021

Is there an example using the onread with paging from an API datasource? I'm not sure if I am supposed to set the Data variable to the initial page of data and then the OnRead takes care of any subsequent sorting\paging calls? I seem to be experiencing the grid attempting to fire OnRead when the page is initialized and I have already set the Data parameter to the first page of data. Basically it duplicates my initial call. But when I do not set the initial page of data it doesn't appear to automatically call the OnRead method. Just FYI, I have this on a component within another main page. Not sure if that makes any difference.

### Response

**Marin Bratanov** answered on 03 Feb 2021

Hello Jeff, You can find full runnable sample projects for implementing server data source operations in the following folder: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server) When using OnRead, the Data parameter must always hold only the current page of data. OnRead will fire when the grid initializes, and this gives you the opportunity to populate it according to the current Page the grid is on (depending on its Page parameter and even on a State you may be loading for your users). Thus, you do not need to worry about an initial page, OnRead will tell you which page of data to fetch, you don't need to do it beforehand. If this does not happen, I recommend you open a support ticket so you can send us the problematic setup. Regards, Marin Bratanov

### Response

**Jeff** answered on 03 Feb 2021

In my case, I do not want the grid to populate when the page initializes. The user provides search criteria and then initiates the search, which populates the initial page of data (the Data variable). Is there a way to force the grid to read (the initial page of results) rather than providing the first page of results programmatically?

### Response

**Marin Bratanov** answered on 04 Feb 2021

Hi Jeff, If you want to populate a specific page of data, you are free to do that, the service call you make for the grid data can take as many parameters as your app requires, it does not have to be just the DataSourceRequest from the grid, so you can add those other user defined criteria to it too. If you need the user to see a specific page (say, page 8 rather than page 1), you can do so by setting the Page parameter (you should use two-way binding), or by using the grid state (see the state storage example and the StateInit event for initial state). If you don't want data in the grid, just set the Data parameter to an empty collection and the TotalCount to 0. You have full control over the data request and what you put in the view model. Regards, Marin Bratanov

### Response

**Robert** answered on 06 Apr 2021

Reading through this thread, I don't find any answer how to refresh a pageable grid, i.e. to trigger OnRead. How to do this?

### Response

**Marin Bratanov** answered on 06 Apr 2021

Hi Robert, I added a new section in the documentation to clarify my previous post with an example. Here is a commit link and by the time you are reading this it should be live in this page: [https://docs.telerik.com/blazor-ui/components/grid/refresh-data#call-onread.](https://docs.telerik.com/blazor-ui/components/grid/refresh-data#call-onread.) Regards, Marin Bratanov Progress Telerik
