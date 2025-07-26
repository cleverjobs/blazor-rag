# grid with observable collection - paging issue

## Question

**RoyRoy** asked on 25 Sep 2019

Here is my situation : I have a grid (grid 1) where a user selects a row and then information of that selected item is displayed in a different group of controls. In particular, the selected item has an observable collections that bound to a second grid (grid 2). My issue is that if I select an item from the grid 1 and the item's collection displayed in grid 2 has multiple pages then I click on a page greater than 1 (for example page 3). Then I select a new item on grid 1 and all of its items in the respective collection bound to grid 2 are bound to the grid but I see nothing displayed in the grid if this collection doesn't have enough items to appear on the page from the previous selected item (ie page 3 in this case). I do see the paging control and if I click on the "1" for page one then I see everything in the collection correctly. Is this by design? Am I supposed to reset the page on the grid manually? Is this because it is an observable collection?

## Answer

**Marin Bratanov** answered on 26 Sep 2019

Hello Roy, I logged this for improvement and you can Follow it in this page: [https://feedback.telerik.com/blazor/1431474-grid-with-observable-collection-page-index-to-reset-if-unavailable-upon-data-source-change.](https://feedback.telerik.com/blazor/1431474-grid-with-observable-collection-page-index-to-reset-if-unavailable-upon-data-source-change.) In the meantime, you can, indeed, try resetting the page index through two-way binding: [https://demos.telerik.com/blazor-ui/grid/paging.](https://demos.telerik.com/blazor-ui/grid/paging.) Regards, Marin Bratanov
