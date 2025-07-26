# ValueChanged not firing when initialized

## Question

**Geo** asked on 09 Oct 2019

It appears that ValueChanged isn't fired when the control is initialized. This is case if Value is populated, or it falls back to the first item from the data source. Is this intentional? It's a bit of a pain having to specifically call it in OnInitialized, I expected it to be called automatically.

## Answer

**Marin Bratanov** answered on 09 Oct 2019

Hello George, The ValueChanged event is fired only when the user changes the selection. The initial load takes the value from the view-model, which implies that the parent component already knows what the value is, it happens in the code of the parent component, not as a user action. In other words, populating with data is not a change of the selected item. This is also valid for the standard inputs. The following example will only fire the ValueChanged event after a user change, not on initializing: <EditForm Model="theModel">
<InputText Value="@theModel.myVar" ValueExpression="@(()=> theModel.myVar)" ValueChanged="@( (string txt)=> MyHandler(txt) )"></InputText>
</EditForm>

@logger

@code {
MyModel theModel { get; set; } string logger { get; set; } void MyHandler ( string theNewText ) {
logger=$"Value Changed fired last on {DateTime.Now} ";
} protected override void OnInitialized ( ) {
theModel=new MyModel();
theModel.myVar=DateTime.Now.Millisecond.ToString();
} public class MyModel { public string myVar { get; set; }
}
} Regards, Marin Bratanov

### Response

**George** answered on 09 Oct 2019

Thanks, Marin. This makes sense when Value is populated (or @bind-value), however, when Value isn't populated and the component is making the decision to use the first item from the data source it might make sense for the event to fire IMO. It's not a problem as such, as I can bind to a field and set that to `dataSource.First().Id;` then call MyHandler(id) manually, it's just not what I expected.

### Response

**Marin Bratanov** answered on 09 Oct 2019

Hi George, In the common case when @bind-Value is used, the field this points to will get updated so further logic will work as expected - the primary use case for Blazor is supposed to be MVVM where the values properties are important, not so much their changed events. When two-way binding is not used, the developer will need to handle all events in their own code anyway, so your approach with checking the data, the value and firing the handler is correct. In no other suite (as far as I know, and I've been through most of our web tools) do we fire a changed event upon initial load, as we believe this will be quite confusing for people and they won't be able to tell a real user action from data binding, which is likely to cause problems with business logic being called in the wrong place or with wrong data. I marked your post as an answer as well because it also explains how to handle such a situation. Regards, Marin Bratanov
