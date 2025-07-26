# Change Form Model inside a TabStrip throws Exception (It renders the model just fine but still An unhandled error has occurred. Reload...

## Question

**Don** asked on 25 Sep 2022

crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Value cannot be null. (Parameter 'property') System.ArgumentNullException: Value cannot be null. (Parameter 'property') at System.Dynamic.Utils.ContractUtils.RequiresNotNull(Object value, String paramName) at System.Linq.Expressions.Expression.Property(Expression expression, PropertyInfo property) at Telerik.Blazor.Extensions.ReflectionExtensions.GetNestedExpression[Object](Object item, String field) at Telerik.Blazor.Components.FormItem.get_ValueExpression() at Telerik.Blazor.Components.FormItem.get_FieldIdentifier() at Telerik.Blazor.Components.FormItem.get_IsValid() at Telerik.Blazor.Components.FormItem.ValidationStateChanged(Object sender, ValidationStateChangedEventArgs e) at Microsoft.AspNetCore.Components.Forms.EditContext.NotifyValidationStateChanged() at Microsoft.AspNetCore.Components.Forms.EditContextDataAnnotationsExtensions.DataAnnotationsEventSubscriptions.Dispose() at Microsoft.AspNetCore.Components.Forms.DataAnnotationsValidator.System.IDisposable.Dispose() at Microsoft.AspNetCore.Components.Rendering.ComponentState.TryDisposeInBatch(RenderBatchBuilder batchBuilder, Exception& exception) Form Component @typeparam T
@try
{ <div class="demo-section"> @if (ValidSubmit)
{ <div class="demo-alert demo-alert-success" role="alert"> The form was submitted successfully. </div> }
else if (Fields !=null)
{ <TelerikForm Model="@Model" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormItemComponent Data="Fields"> </FormItemComponent> </FormItems> </TelerikForm> } </div> }
catch (Exception e)
{

throw;
}

@code {
[Parameter]
public T Model { get; set; }
[Parameter]
public EventCallback <T> ValidSubmitHandler { get; set; }
private List <PropertyInfo> Fields=new List <PropertyInfo> ();

protected override void OnParametersSet()
{
if(Model is not null){
Fields=Model.GetType().GetProperties().ToList();
}
}

public bool ValidSubmit { get; set; }=false;

async Task HandleValidSubmit()
{
Console.WriteLine(Model);
Console.WriteLine("Saved");
ValidSubmit=true;
await ValidSubmitHandler.InvokeAsync(Model);
ValidSubmit=false;
StateHasChanged();
}

void HandleInvalidSubmit()
{
ValidSubmit=false;
}
} TabStrip Component <TelerikTabStrip ActiveTabIndex="ActiveTab" ActiveTabIndexChanged="@TabChangedHandler"> @if(Tabs !=null)
{
@foreach (var item in Tabs.OrderBy(x=> x.Order))
{ <TabStripTab Title=@item.Title> <FormComponent Model="@item.Model"> </FormComponent> </TabStripTab> }
} </TelerikTabStrip> using Microsoft.AspNetCore.Components;
using DemoApp.Helpers.Models;
using DemoApp.Helpers.Models.ConfigureElements;

namespace DemoApp.Components
{
public partial class TabStrip
{
protected override void OnInitialized()
{
}
protected override void OnParametersSet()
{
}

[Parameter]
public List <Tab> Tabs { get; set; }
string result { get; set; }

int ActiveTab;
void TabChangedHandler(int newIndex)
{
ActiveTab=newIndex;
result=$"current tab {newIndex} selected on {DateTime.Now}";
}
}
}

## Answer

**Svetoslav Dimitrov** answered on 28 Sep 2022

Hello Donald, I would like to ask for a small runnable snippet where we can reproduce the issue. This will allow us to investigate in depth and determine what causes the thrown exception. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Donald** commented on 03 Oct 2022

Hi Svetoslav, I am working on a Demo and it is not possible to share some working snippet without sharing the entire solution. The Main idea is somewhere inside here: <TelerikForm Model="@Model" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormItemComponent Data="Fields"> </FormItemComponent> </FormItems> </TelerikForm> When I change the Model it throws the error highlighted in the code. If there is another way to share the project only with you please ping me.

### Response

**Svetoslav Dimitrov** commented on 06 Oct 2022

Hello Donald, I can see that you are using a FormItemComponent that has a Data parameter, where you pass a List<PropertyInfo>. My best guess is that you have created an abstraction of our FormItem where you are looping through that List<PropertyInfo> and creating the FormItems dynamically. The issue suggests that there is a problem with the FormItem which should be defined in the FormItemComponent in your application. You can send me a runnable snippet where I can investigate in a private ticket.

### Response

**Jim** answered on 21 Jul 2023

I have the exact same issue. Any news/information on this matter? PS: I have found the reason to my problem. I dynamically recreated the EditContext while the component was rendered. This somehow caused the error. If I hide the form, recreate context and show the form, the problem doesn't exist anymore.
