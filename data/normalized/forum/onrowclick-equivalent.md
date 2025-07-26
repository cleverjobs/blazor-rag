# OnRowClick equivalent?

## Question

**Ron** asked on 01 Apr 2021

If I select an item in a ListView is there any way I can get the whole row like for a Grid? If there were a Grid I would assign a function to be called OnRowClick. But that does not seem to be available for ListView?

## Answer

**Marin Bratanov** answered on 05 Apr 2021

Hello Ronald, The ListView, unlike the grid, does not control the rendering of its items, so it can't offer such an event to you. You can, however, hook your own events, like @onclick and get the item with a simple lambda. You can find a very similar example in this project: [https://github.com/telerik/blazor-ui/tree/master/listview/item-selection](https://github.com/telerik/blazor-ui/tree/master/listview/item-selection) Regards, Marin Bratanov

### Response

**Ronald** answered on 05 Apr 2021

One more question. Again forgive me but I am new. When forming the lambda, is there a way to pass in the whole row that was clicked on?

### Response

**Ronald** answered on 05 Apr 2021

Basically I want to pass in the whole context?

### Response

**Marin Bratanov** answered on 05 Apr 2021

Hello Ronald, You can pass whatever object you choose to. I chose to pass an ID in the example for selection I made, you can pass the whole model, just touch up the corresponding method signature to accept that. The basics would look something like: <TelerikListView Data="@ListViewData" Width="700px" Pageable="true"> <HeaderTemplate> <h2> Employee List </h2> </HeaderTemplate> <Template> <div class="listview-item @( context.Selected ? " selected-item ": "" )" @onclick="@( _=> Console.WriteLine( context ) )"> <h4> @context.Date.ToShortDateString() </h4> <h5> @context.TemperatureC &deg; C </h5> <h6> @context.Summary </h6> </div> </Template> </TelerikListView> Regards, Marin Bratanov Progress Telerik
