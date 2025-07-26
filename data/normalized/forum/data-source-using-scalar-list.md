# Data source using scalar list?

## Question

**And** asked on 30 May 2019

Hi - all of the dropdownlist code examples show data binding to lists of non-scalar types. I.e. lists of objects. My question is, can your dropdownlist bind to lists of scalar types? I.e: <TelerikDropDownList Data="@MyList" bind-Value=@MyItem /> @functions { protected List<string> MyList()=new List<string>(); protected string MyItem; } If so, do I need to provide the ValueField and TextField properties?

## Answer

**Marin Bratanov** answered on 30 May 2019

Hi Andrew, Having a field for text and values in a model is mandatory at this point (that is, you need a List<someObject>). How would you expect binding to a list of primitive types to work? How would the dropdown choose what values to render? Would something like the following snippet suit your needs, assuming it worked (it will not work now, as an entire model is required)? At the moment I can see the following options as potentially viable, although each of them would have its drawbacks: Define item type and value type to let the component know what it will be using, and define custom templates to let it know what to render, like in the snippet below. An alternative would be that if a List<string> is used that it automatically gets rendered and chosen as values, but that may limit templates and would then raise the question "what if I want to use an integer, or a float, or some other number, or a boolean". @using Telerik.Blazor.Components.DropDownList <TelerikDropDownList Data="@MyList" bind-Value=@MyItem TItem="string" TValue="string"> <ValueTemplate> @context </ValueTemplate> <ItemTemplate> item: @context </ItemTemplate> </TelerikDropDownList> selected value: @MyItem @functions { protected List<string> MyList=new List<string>() { "a", "b", "c" }; protected string MyItem { get; set; }="b"; } That said, I would encourage you to post a public feature request for the way you want to see this work, perhaps including a similar pseudocode sample that you would expect to work as a sample way of how the component API should be modified/used. You can do that from this link (or from the "Request a Feature" link in the

### Response

**Andrew** answered on 30 May 2019

Thank you. I have submitted feedback request: [https://feedback.telerik.com/blazor/1411181-telerikdropdownlist-should-accept-lists-of-scalar-as-data-source](https://feedback.telerik.com/blazor/1411181-telerikdropdownlist-should-accept-lists-of-scalar-as-data-source)

### Response

**Marin Bratanov** answered on 31 May 2019

Thank you for creating that request, Andrew. If it gets traction with the community, we will consider its implementation. Its status will be updated as we work through it then. --Marin
