# DataGrid: Page up/down not working without paging

## Question

**Mar** asked on 21 Feb 2022

[https://blazorrepl.telerik.com/QmEGmFYM497yvJqU02](https://blazorrepl.telerik.com/QmEGmFYM497yvJqU02) I can't get page up/down to work. Arrow navigation works fine in the grid. I stumbled on this when I was trying to expand on the grid searchbox. I would like to implement this usecase User type a key shortcut I have implemented and the searchbox get focus (this I have implemented) user type something and the grid are filtered (works) user presses enter and the first row in the grid get focus ( Not sure how to set focus on a row in a filtered grid ) user navigates to the desired row and use space to activate the row (this should also work out of the box) Right now I don't use the Navigable property because of the issue with page up/down This has to be fixed first. Then I would like some help with setting focus on the first filtered row. I found this article [https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data](https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data) Maybe when the user presses ENTER I can use the ToDataSourceResult extension method and then take the first row and add it to the selected rows collection. Or are there a easier way to set focus on the first row of a filtered dataset?

### Response

**Dimo** commented on 24 Feb 2022

Hi Martin, If I understand correctly, you are trying to use keyboard navigation inside the Grid with Navigable="false". This is possibly only if you modify our JavaScript source code and implement everything manually. In general, every custom navigation that does not match our built-in feature will require custom source code. Page up/down should work when Navigable="true" and paging is enabled.

### Response

**Martin Herløv** commented on 24 Feb 2022

No of course not 😊 Just saying when I use Navigable="true". then arrow keys work fine but not page up/down. So you have to hold and press arrow down to get to the bottom

### Response

**Dimo** commented on 24 Feb 2022

Ah, maybe I understand now. When the Grid keyboard navigation is enabled and the Grid is focused, the Page Up/Down keys page the Grid, but do not scroll the browser page. Is this what you meant? This behavior is expected. Otherwise paging the Grid will cause the component to disappear from the viewport. The same applies to the Up/Down arrow keys. Depending on the exact use case, you can consider a variety of options. Here are two that come to mind: scroll the page with JavaScript or execute scrollIntoView (), so that the Grid is fully visible adjust the Grid PageSize or Height, so that the component can fit in the viewport

### Response

**Martin Herløv** commented on 24 Feb 2022

We are getting closer 👍 Still Navigable="true" are eating page up/down because it's used when paging is enabled. I like that the users can navigate around in the grid using the arrow keys. And normal I use paging but some users prefer list when data are under 300 rows. So I guess I can look in the js file and get inspired on how to implement this for my usecase
