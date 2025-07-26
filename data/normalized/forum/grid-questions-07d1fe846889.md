# Grid questions

## Question

**Nic** asked on 03 Jun 2019

Hi, I appreciate it's still under development so maybe what I ask is unavailable, but I have a couple of questions about the grid: 1. If I have a lot of columns can I set the size of the columns and have the grid display a horizontal scrollbar. 2. I'm having trouble getting sorting working with templated columns: It doesn't seem to work at all when I just set the Items and when using the ReadItems method, which is ultimately what I want to do the sort descriptor is passed in but the sort descriptor member field is empty (the sort direction does contain a value). Do I need to set something on the column template as a sort value or something? Thanks, Nick

## Answer

**Nick** answered on 03 Jun 2019

Also how do I set the sorted columns initially?

### Response

**Marin Bratanov** answered on 03 Jun 2019

Hi Nick, To each question: If I have a lot of columns can I set the size of the columns and have the grid display a horizontal scrollbar. - this can be achieved by having a lot of columns, but the grid container having limited width. With this, the entire grid would be scrolled in its container. For later releases (hopefully, R1 2020), we intend to have scrolling options as a feature in the grid. For the time being, I must note there is a bug in this scenario, you can see here for a sample of such a scrollbar, the bug, and its workaround. I'm having trouble getting sorting working with templated columns - as long as their Field is in the main grid model, this should work, and I suggest you compare against the demo we have which works as expected: [https://demos.telerik.com/blazor-ui/grid/sorting.](https://demos.telerik.com/blazor-ui/grid/sorting.) Perhaps you should also check the following page for a similar case that the grid cannot handle: [https://feedback.telerik.com/blazor/1408650-column-sorting-breaks-under-subclassing-scenarios.](https://feedback.telerik.com/blazor/1408650-column-sorting-breaks-under-subclassing-scenarios.) When an OnRead handler is attached, however, the grid will no longer sort, filter or page the data, as described here, so you will need to extract that information form the DataSourceRequest field of the event arguments. I'm attaching below a small example that works fine for me and extracts the sort status so you can use it as a reference. how do I set the sorted columns initially - I would encourage you to post a feature request for this feature in the

### Response

**Nick** answered on 03 Jun 2019

Thanks Marin, I will have a play with getting the scrollbar to work. My grid isn't fixed width but it does fit within in the screen - I guess it may be to do with my not understanding the CSS/HTML going on (I'm using the standard template at the moment so the body width is flexible but only up to a point and the grid columns are wrapping rather than stretching) I will also raise a feature request, so thanks for that. Regarding the sorting, I think it may be to do with the way my object model works. Effectively I am binding to a list of Item objects (one per row), that has a list of FieldValue objects which represent a field/column in a row. The FieldValue has a name and a value of type object, some of the values will be standard types like string, decimal and some are our own types - for example we have a DateOnly type. Separately to this we have a "view definition" which tells us all of the columns to expect, I use this to create the actual list of columns. Here's is some example code: Represents a "row": public class Item { public string EntityTypeName { get; set; } public FieldValues FieldValues { get; set; } } Represents a column on a row: public class FieldValues : KeyedCollection<string, FieldValue> { public FieldValues() : base(StringComparer.OrdinalIgnoreCase) { } public FieldValues(IEnumerable<FieldValue> fields) : this () { AddRange(fields); } public void AddRange(IEnumerable<FieldValue> fields) { foreach (var fieldValue in fields) { Add(fieldValue); } } public void Add(string fieldName, object value) { Add(new FieldValue(fieldName, value)); } protected override string GetKeyForItem(FieldValue item) { return item.FieldName; } } } Defines how the grid should look (this is cut down for simplicity): public class ViewDefinition { public string Name { get; set; } public List<ViewColumn> Columns { get; set; } public List<SortDef> SortColumns { get; set; } } Defines how a column should look (this is cut down for simplicity): public class ViewColumn { public string FieldName { get; set; } public int Width { get; set; } public string Label { get; set; } public FieldType FieldType { get; set; } } In my UI I am creating the colums like this: <TelerikGrid Data=@Items TItem="Item" Sortable="true" Pageable=true PageSize=15 TotalCount=@Total> <TelerikGridEvents> <EventsManager OnRead=@ReadItems></EventsManager> </TelerikGridEvents> <TelerikGridColumns> @foreach (var column in ViewDefinition.Columns) { <ViewGridColumn ViewColumn="@column"></ViewGridColumn> } </TelerikGridColumns> </TelerikGrid> ViewGridColumn is my own component which I use for rendering a column. A snippet from ViewGridColumn which shows the creation of a column for a FieldValue that contains a string looks like this: switch (ViewColumn.FieldType) { case FieldType.String: <TelerikGridColumn Title="@ViewColumn.Label" Width="@(ViewColumn.Width + "px")"> <Template> @{ var stringFieldValue=GetFieldValue(ViewColumn.FieldName, @context); <span>@stringFieldValue?.Value</span> } </Template> </TelerikGridColumn> break; The switch statement has further branches and lets me render the different types in the correct way. Now I appreciate why the automatic sorting doesn't work, but when I us the ReadItems method I don't get the column name or label in the args. It passes me a single sort descriptor in args.Request.Sorts but whilst SortDirection is set, Member is null. Obviously this makes it impossible for me to tell which column the grid thinks it is sorting on. From my tracing in the console you can see that I get one sortdef passed but the member is null: WASM: Sort Descriptor Count=1 blazor.webassembly.js:1:32035 WASM: sortDescriptor.Member=Null sortDescriptor.SortDirection=Ascending I hope this makes some sense!

### Response

**Nick** answered on 03 Jun 2019

P.S As an aside I noticed there is some formatting issues of the page numbers when there are a lot of pages and click on one that is over 100. See attached image.

### Response

**Marin Bratanov** answered on 04 Jun 2019

Hello Nick, Perhaps a key thing to having the grid scroll more predictably is setting Width for the columns. Without the width, the browser decides how wide a column will be, and the narrower the <table> that's holding it, the more different the behavior can be, as it can depend on CSS, and on the contents of the cells. The grid itself (and the <table> it uses) are block elements and take the available width in their parent element unless something else is specified (like width on the column, or other CSS rules). On the provided sorting scenario - indeed, the case is the same as the page I linked above - the nested classes and fields are not something the grid can know about. For the built-in operations to work, the model (in this example the Item class) needs to be a flattened list of primitive fields that can be sorted. Alternatively, the classes that represent columns must implement their own sorting. That said, I think they key issue for the missing Member value is that the Field property of the column is not set. Without it, the column does not know to which field (member) of the data source it is bound, and so it cannot pass this information along to the data source. I'd suggest hardcoding a string in the Field property of the columns as a start to see if it will come up in OnRead. If so, you can then proceed to take it from ViewColumn.FieldName. This bring me to the feature request - indeed, the ability to set the sort direction would be useful for such cases, especially when you already implement the sort operation through OnRead. As for the pager numbers - I have logged it for fixing and you can Follow its status here: [https://feedback.telerik.com/blazor/1411728-pager-items-appearance-is-unclear-with-page-numbers-1000.](https://feedback.telerik.com/blazor/1411728-pager-items-appearance-is-unclear-with-page-numbers-1000.) The page also contains a workaround which I am pasting below too. <style> /* The workaround */ .k-pager-wrap.k-grid-pager .k-link, .k-pager-wrap.k-grid-pager .k-state-selected { min-width: calc( 10px + 1.4285714286em ); width: auto; } </style> Regards, Marin Bratanov

### Response

**Nick** answered on 04 Jun 2019

Thanks for all your help Marin, much appreciated!

### Response

**Nick** answered on 05 Jun 2019

Hi Marin, Just to let you know setting the Field property did the trick - I now get the column name in the sort descriptors passed to the ReadItem event. Thanks for that! Nick.

### Response

**Marin Bratanov** answered on 06 Jun 2019

Thanks for letting me know, Nick, I appreciate it. I'm happy to hear you have things working. --Marin
