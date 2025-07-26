# Bug? AutoComplete inside EditForm - infinite loop with OnParametersSet

## Question

**BenBen** asked on 11 Jul 2020

Hi, I'm trialling the latest version at the moment (v2.15.0) with a WebAssembly project and I've encountered an odd issue. Essentially, when I have a component with a Guid parameter, and a TelerikAutoComplete component inside an EditForm there's some kind of render loop happening on the page. The browser tools show the DOM being updated constantly and the OnParametersSet override is being called constantly. Tested in MS Edge 83. Moving the AutoComplete outside the EditForm or changing the parameter to something else such as an Int32 causes the issue to no longer present itself. Not sure if this is being caused by the Telerik component or a bug in Blazor itself, but I imagine it's a fairly common scenario. Simple reproduction code below. @page "/customers/test/{Parameter1:guid}" @if (Model !=null ) { <EditForm Model="Model"> <TelerikAutoComplete Data="@Fruit" Filterable="true" @bind-Value="@Model.SelectedFruit" ValueField="@(nameof(SimpleObject.DisplayName))" /> </EditForm> } @code { [Parameter] public Guid Parameter1 { get; set; } public SimpleTestModel Model { get; set; } public IEnumerable<SimpleObject> Fruit { get; set; } protected override async Task OnInitializedAsync() { await Task.Delay(100); this.Fruit=new SimpleObject[] { new SimpleObject(1, "Lemon" ), new SimpleObject(2, "Orange" ), new SimpleObject(3, "Kiwi" ) }; } protected override async Task OnParametersSetAsync() { Console.WriteLine( "ParametersSet" ); await Task.Delay(100); this.Model=new SimpleTestModel(); } public class SimpleTestModel { public string SelectedFruit { get; set; } } public class SimpleObject { public SimpleObject( int id, string name) { this.Id=id; this.DisplayName=name; } public int Id { get; set; } public string DisplayName { get; set; } } }

## Answer

**Marin Bratanov** answered on 13 Jul 2020

Hi Ben, The infinite loop comes from updating the Model field - it triggers the OnParametersSet, where the model gets updated again, and that triggers the lifecycle method again. There is also a report to Microsoft that using a GUID as parameter causes this, but other types don't and you can follow through the discussion here: [https://github.com/dotnet/aspnetcore/issues/21348.](https://github.com/dotnet/aspnetcore/issues/21348.) We suspect that the checks around here cause re-renders and perhaps the MS team will address this in the future. Here's a solution I can suggest that lets you monitor certain parameters ("Parameter1" in this example) for changes so you can get the new form model only when needed and thus - avoid the infinite loop. This can be helpful as a general pattern where you can monitor parameters and control re-rendering and data requests: bool shouldFetchModel { get; set; } public override async Task SetParametersAsync ( ParameterView parameters ) { if (parameters.TryGetValue( "Parameter1", out Guid parameterValue))
{ if (parameterValue !=Parameter1)
{
shouldFetchModel=true;
}
} await base.SetParametersAsync(parameters);
} protected override async Task OnParametersSetAsync ( ) { if (shouldFetchModel)
{
Console.WriteLine( "getting new model, special parameter changed" ); await Task.Delay( 100 ); this.Model=new SimpleTestModel();
}
shouldFetchModel=false;
} Regards, Marin Bratanov

### Response

**Ben** answered on 15 Jul 2020

Thanks Marin, that definitely seems related, I thought that OnParametersSet was only triggered by changes to properties decorated with [Parameter] or [CascadingParameter] etc. In case it's not clear in the example I need to call into a web service and get a different Model when a parameter (Parameter1) changes. I'm assuming I'm using the right pattern here and that I'm really only hitting some bad change detection code in Blazor because of the Guid Type? Could another work around be to make the Model property a field instead if I don't need to expose it as an attribute to a parent?

### Response

**Marin Bratanov** answered on 15 Jul 2020

Hello Ben, I suspect that this particular issue comes from an issue in the diffing with GUIDs, althouth the pattern from my post is a little more explicit. It has the following benefits: you fully control the change on which parameter and even to what value causes the new data to be requested changes to other parameters from local execution in the current component can also be skipped You don't have control over either with the basic approach. For example, if you want a new model only if the GUID parameter changes - you need the approach from my post, especially if you have more than one parameter and/or if those parameter values can be changed from within the component. Regards, Marin Bratanov

### Response

**Ben** answered on 15 Jul 2020

Perfect, thanks again!

### Response

**Stan** answered on 16 Nov 2020

Is this still the best option? This seems like a bad solution as you are making the OnParametersSetAsync much less usable and making users completely change how they handle the lifecycle to use a control. 8.5.2

### Response

**Marin Bratanov** answered on 17 Nov 2020

Hi Stan, The change detection is in the framework and we can't influence that. So, we have provided the best solution we could come up with. If you find anything better, feel free to post it. You can also participate in the GitHub issues in the Microsoft repo too. Regards, Marin Bratanov
