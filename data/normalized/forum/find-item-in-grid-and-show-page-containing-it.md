# Find item in grid and show page containing it

## Question

**Mar** asked on 03 Apr 2023

I have a grid using paging and sorting features. When a user edit a record (I am using an edit form that show an edit form) and he changed the value from the sorted column, the item is no more visible in the current page since it moved in another page according to the sorting feature. My question how can I find in which page my item is now on, and to programmatically select that page so my item will stay in the current view after edition. Thanks

### Response

**Marc** commented on 03 Apr 2023

I know how to set the current page using the Page attribute, but don't know how to know on which page an item is located according to the current sort.

## Answer

**Dimo** answered on 06 Apr 2023

Marc - Usually, this task will require a manual calculation in the app. What you can use from our product to help you is the ToDataSourceResult () method. Get the Grid state Create a new DataSourceRequest instance Populate all relevant DataSourceRequest properties, based on the information from the Grid state. Do not include paging settings. Execute ToDataSourceResult () over the whole dataset and pass the DataSourceRequest object as an argument. In this way you will get all items in the current sorted and filtered state, but without paging. Get the item index and calculate the page number. Go to that page. If this approach is not practical, because the total number of items is too large to load in memory, then implement some custom algorithm that will perform better.
