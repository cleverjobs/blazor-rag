# refresh grid on demand

## Question

**kha** asked on 07 Jun 2020

Hello, i have a button that changes some data in backend after that i need to refresh data of a grid and also i need sort, pagesize, ... data of grid

## Answer

**Marin Bratanov** answered on 08 Jun 2020

Hello, The following KB article explains how you can do that: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-force-refresh.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-force-refresh.) On enabling sorting, paging, filtering and so on, I suggest you start by following our documentation: [https://docs.telerik.com/blazor-ui/components/grid/overview.](https://docs.telerik.com/blazor-ui/components/grid/overview.) If you want to implement the operations yourself, see this article: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations.) Regards, Marin Bratanov

### Response

**Brian** answered on 22 Jun 2020

First, Marin's great, so this is no reflection on him. But this solution is a hack because Engineering hasn't delivered a core feature .Refresh() of a Grid. (Yes, yes, there are priorities and only so much engineering staff. I deal with this daily myself. But don't give me a car without a steering wheel! Some features are mandatory.) I've got a solid 3 level hierarchical grid working using List<>, and I have to do a lookup on the 3rd level and insert new values. I'm using a nested model from Cosmos DB so I want to keep things simple. My only problem is that the Inserts into the 3rd level are ignored by the Grid. Invoking.Clear() on the List or setting it null, counting to 10 mil, assigning it again does nothing. I've followed the KBs and such, and nothing. No effect. But a simple browser refresh and the Grid is rendered up to date with the new data. So now I am supposed to rewrite a working and tested program to use ObservableCollection, and retest, because Grid.Refresh() STILL doesn't exist? I'm going to go find that feature request and give it my up vote.

### Response

**Marin Bratanov** answered on 22 Jun 2020

Hi Brian, I would recommend you put your nested grid content in separate components and step through their lifecycle methods. This will ease debugging, and will also give you some more hooks to add breakpoints to (mostly the OnInitialized and OnParametersSet events of this child component). The added benefit is that the main grid code will be simpler and you can encapsulate the necessary CRUD operations in the child component. You can even use load on demand for its data: [https://github.com/telerik/blazor-ui/tree/master/grid/load-on-demand-hierarchy.](https://github.com/telerik/blazor-ui/tree/master/grid/load-on-demand-hierarchy.) That said, if you have access to the particular component, a .Refresh() method on the grid would not do anything more than call .StateHasChanged() which you can do now already, and you can also change a parameter reference (such as the pointer to the Data collection) to call the grid's OnParameterSet event and have it redraw). If this does not work on your end, the most likely reasons are either that the data is not there yet, or that the pointer to its collection does not change. The item for updating the grid data source is here, and it was resolved through the ObservableCollection binding and by using the standard approach of changing pointers. Regards, Marin Bratanov

### Response

**Brian** answered on 22 Jun 2020

Howdy Marin. Actually, we hit on a totally different hack. During testing of an ObservableCollection refactor, it was noticed that the manual collapsing and expanding of the hierarchy would display the newly added data. Reading through the docs on Hierarchy Collapse and Expansion through code, and State preservation, it was learned that just simply resetting the state and expanding the hierarchy after adding data and voila, the new data is displayed. The code used was straight from the examples: async Task ExpandHierarchy() { GridState<User> desiredState=new GridState<User>() { ExpandedRows=new List<int> { 0, 1 }//expand the first two rows }; await Grid.SetState(desiredState); } public async void SearchResultHandler(Results Item) { showSpinner=true; IsVisibleFuzzySearch=false; StateHasChanged(); ... Add some data to model.... await Grid.SetState(null); await ExpandHierarchy(); StateHasChanged(); } That's it. Works really well. Not perfectly (still a hack, some flicker), but "good enough" to move on to other, bigger issues (delivery!) It looks like there might be a better solution using "Insert an Item" State change, but that will take more investigation, and we're under the gun. We're good for now.
