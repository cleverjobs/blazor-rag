# grid by key, not by index

## Question

**Ale** asked on 20 Sep 2021

is it possible to have sate by key, for example now the grid located the record by index and if some of the rows were expended & them some removed, thу grid will incorrectly expand rows after update & refresh because the index was changed

### Response

**Aleksandr** commented on 21 Sep 2021

any way to have the ability to filter the data by the Grid State? Do not suggest OnRead :-) i am going to do all what i have out of the box manually

### Response

**Aleksandr** commented on 21 Sep 2021

seems found a solution for sorting/filtering, but still, need for search box

## Answer

**Radko** answered on 23 Sep 2021

Hello Aleksandr, The Grid Toolbar Searchbox does take into account the currently applied filters, thus you can apply filters to the results returned from the Searchbox. Its behavior and customization options are covered in this article - Grid Toolbar Searchbox. If you require different behavior, then perhaps it would be best to use the OnRead event you mentioned already. Regards, Radko Stanev

### Response

**Aleksandr** commented on 23 Sep 2021

basically, I just need to have the resultset which is currently shown in the grid with all filters/searches applied, how can I have it?

### Response

**Radko** commented on 24 Sep 2021

Hello Aleksandr, You can use the Grid's State to access its current state, such as sorting, filtering, paging, grouping, edited items, selection, column size, and order. However, the filter descriptors from the Searchbox itself are not included in this state. You can check this feature request, where you can find more details in regards to the reason behind why they are not included in this. Regards, Radko Stanev

### Response

**Aleksandr** commented on 24 Sep 2021

Radko, I already voted, but don't get me wrong, building the grid you already have code that applies all the filters & searches to the dataset, so, just make it public :-) in some helper or state I need it to have the grid being exported exactly as it is shown to the user (i do export manually (using document processing) to have custom format) Thx Alex

### Response

**Radko** commented on 28 Sep 2021

Hi Aleksandr, The Searchbox is intentionally not included in the GridState. Adding it will lead to rather unexpected behavior to the rest of the filter state. We consider the Searchbox intermittent, with a rather transient nature, as the queries done through it are temporary and short-lived. What you can do, however, is cast your vote for this Feature Request, if it sounds beneficial to you - Ability to clear the SearchBox on Escape key, with an "X" in the input and Programmatically. Such a feature could potentially allow to programmatically read and write the Searchbox text. Regards, Radko Stanev
