# Blazor-TelerikGrid with Field-Binding that is kind of Dictionary property of the Main Object

## Question

**Mic** asked on 19 May 2020

Hello, I need to migration some legacy stuff and some weird Object-constellation is giving me some problems with the binding in the Blazor Telerik-Grid. Maybe some-one can give me some advise. Example Code of legacy data structure: class MainObject() { string Id { get; set;} SubObject[] SubObject { get; set;} } SubObject { string Key { get; set;} string Value { get; set; } Details: the SubObject contains some-kind of descriptive Information that is customized for every system. Goal: protected IList<MainObject> MainObjectList{ get; set; } <TelerikGrid Data=@MainObjectList> <GridColumn Field="Id" Title="Id"></GridColumn> <GridColumn Field="SubObject.First().Value" Title="SubObject.First().Key"></GridColumn> What I try to achieve is to show some of the normal properties of the MainObject and some of the Descriptive-Informations inside the SubObjects in the Grid. I did not even managed to show any of the Informations of the SubObject, is this even possible?

## Answer

**Marin Bratanov** answered on 19 May 2020

Hello Michael, I can suggest you start by reviewing the following article (and especially the Notes section at the end) to see how the grid works with data binding: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound.](https://docs.telerik.com/blazor-ui/components/grid/columns/bound.) The key thing is that the field the grid binds to must be readily readable and comparable. A collection (list, array, dictionary,...) is not, there is no built-in method that will let .NET and the Grid know what you want to do with such a collection, so it is not sortable, groupable, filterable, and there is no way to know what to render for it. It's even likely to throw exceptions. That said, what you can do is to: remove the Field from this column (which will prevent it from throwing errors, and from being filterable, sortable, groupable) use the column template to show the desired item from the current model in the desired way Of course, another approach is to flatten the data so the model that you bind the grid to only has a simple string (or int) field that you want to show. Regards, Marin Bratanov

### Response

**Michael** answered on 19 May 2020

Thanks for the input! I will try what works best for my scenario.

### Response

**Michael** answered on 20 May 2020

The Template did the trick! With following code I am even able to use Linq expressions to just show the specific fields configured externally: <GridColumns> @foreach(var field in FieldsToShow) { <GridColumn Field="Id" Title="@field.Label"> <Template> @((context as MainObject).SubObjects.(First)(entry=> entry.Key==field.Key).Value) </Template> } </GridColumns> I still lost the possibility to sort, group and filter because my actual model is messed up but these features are in current state not needed so should be good enough for my use case. If they will be relevant later I will follow your other suggestions. Thanks again!
