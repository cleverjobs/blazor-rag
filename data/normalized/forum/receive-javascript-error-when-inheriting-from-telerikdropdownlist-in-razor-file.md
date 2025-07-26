# Receive javascript error when inheriting from TelerikDropDownList in razor file

## Question

**Ada** asked on 10 Apr 2023

Using blazor server with latest Telerik Blazor package (currently 4.1.0). I created a very simple CustomDropDownList.razor file with the following: @typeparam TItem
@typeparam TValue
@inherits TelerikDropDownList<TItem, TValue> and attempted to use the new component in a page: @page "/test" <CustomDropDownList Data="testData" @bind-Value="value" />

@code { int? value=null; private List<Model> testData=new List<Model>()
{ new Model() { Id=1, Text="Item 1" }, new Model() { Id=2, Text="Item 2" }
}; class Model { public int? Id { get; set; } public string Text { get; set; }
}
} I get the javascript error: Cannot read properties of null (reading addEventListener) I'm aware you have a page regarding this error, but it only suggests making sure telerik-blazor.js file is up to date. Mine is. Now, if I define the same component in a .cs file instead of a .razor file, the scenario works fine: public class CustomDropDownList <TItem, TValue> : TelerikDropDownList <TItem, TValue>
{
} REPL with error (using .razor file): [https://blazorrepl.telerik.com/GRaoFuvr00aqKiQq27](https://blazorrepl.telerik.com/GRaoFuvr00aqKiQq27) REPL that works (using .cs file): [https://blazorrepl.telerik.com/wHkyFubg58jPmb8D40](https://blazorrepl.telerik.com/wHkyFubg58jPmb8D40) So what is going on here? Ultimately, I'm trying to inherit from TelerikDropDownList to encapsulate a reusable custom dropdown. I have done this with .cs files a number of times with no problem, but in this case I was wanting to define an ItemTemplate and it's much more practical to do .razor file - that's when I discovered this issue.

## Answer

**Dimo** answered on 11 Apr 2023

Hi Adam, When you use the.razor file approach, the custom component has no HTML output. This causes the client-side initialization algorithm to fail, because it can't find the expected DOM element on the page. So the correct ways to proceed are: Use the.cs approach, OR Use the.razor approach, but in this case, do not inherit our component. Just wrap it in another reusable .razor file and pass parameters to it. Regards, Dimo Progress Telerik

### Response

**Adam** commented on 13 Apr 2023

Thank you Dimo. I prefer to use .cs approach so that I don't have to create parameters just to pass to the wrapped component. Is there a way I can continue to use the .cs approach but define just a RenderFragment for ItemTemplate in a razor file that I can reference in the .cs file?

### Response

**Dimo** commented on 13 Apr 2023

Unless I am missing something, there is no need for anything special to achieve this: <CustomDropDownList Data="testData" @bind-Value="value" TextField="Text" ValueField="Id"> <ItemTemplate> @{ var item=(Model)context; }
@item.Id - @item.Text </ItemTemplate> </CustomDropDownList>

### Response

**Adam** commented on 13 Apr 2023

I want to define a default custom template within the CustomDropDownList component so that the template doesn't have to be specified every time CustomDropDownList is used and markup is not allowed in .cs file, only .razor. I'm aware I can achieve this in .cs but once a template is more complex it is not practical. ItemTemplate=model=> builder=> builder.AddContent( 1, $" {model.Id} - {model.Text} " ); So I need my .cs custom component to have a corresponding .razor file to set a more complex RenderFragment @code {
RenderFragment<TItem> customItemTemplate=(TItem item)=>
@<text>
<div class="something">
<h5>@item.Id</h5>
<div class="something-else">
@item.Text
</div>
</div>
</text>;
} Then reference customItemTemplate in the .cs file

### Response

**Dimo** commented on 13 Apr 2023

Using a RenderTreeBuilder is the required approach for such requirements. The Blazor framework doesn't provide an easier way. Alternatively, here is another idea that you can try: define the RenderFragment in a Razor file, which has a public static method that returns this fragment to any other Razor component, which requests it. Then, use the default ItemTemplate for every CustomDropDownList instance that needs it.

### Response

**Adam** commented on 13 Apr 2023

Ok, no problem. Thanks.
