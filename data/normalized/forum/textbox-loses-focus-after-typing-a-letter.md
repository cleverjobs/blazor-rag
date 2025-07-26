# TextBox loses focus after typing a letter

## Question

**Ger** asked on 09 Feb 2021

Hi, I'm trying to create a custom EditForm component by i just can't get it working. The TelerikTextBox loses focus after every keystroke and also never causes the EditContext to getb into a modified start. My model look like: public class MyModel { public string Code { get; set; } public string Name { get; set; } } The EditForm is split into a razor and a razor.cs file: @inherits MyEditFormBase <EditForm EditContext="@MyEditContext"> <CascadingValue Name="EditContext" Value="@MyEditContext"> @ChildContent(MyEditContext) </CascadingValue> </EditForm> <TelerikButton Title="Ok" OnClick="(()=> Console.WriteLine(MyEditContext.IsModified()))" /> public class MyEditFormBase : ComponentBase { public EditContext MyEditContext; [Parameter] public RenderFragment<EditContext> ChildContent { get; set; } [Parameter] public MyModel Value { get; set; } protected override Task OnParametersSetAsync() { MyEditContext=new EditContext(Value); return base.OnParametersSetAsync(); } } And finally to apply the MyEditForm i'm using this: <MyEditForm Value="@Value"> <TelerikTextBox Value="@Value.Code" ValueExpression="@(()=> Value.Code)" ValueChanged="@((string s)=> Value.Code=s)" /> </MyEditForm> @code { public MyModel Value { get; set; }=new MyModel(); } It all looks relatively simple, but i can't figure out how to make it work properly. Am i missing something, or am i trying to use the Telerik controls in a way they can't handle? Regards, Gerrit

## Answer

**Eric R | Senior Technical Support Engineer** answered on 11 Feb 2021

Hi Gerrit, Thank you for providing the code for your project. However, I don't believe I have enough information to fully understand the scenario. Let me review what I can gather from the information below. Investigation The TelerikTextBox losing focus after each keystroke appears to be a side-effect of the implementation. This is probably happening because the Telerik Blazor controls fire after OnInput where the standard Blazor controls fire after the OnChanged event, and something goes wrong with updating the model data in the parent components, somewhere in the application logic. Additionally, the EditContext is already a cascading parameter on the edit form and shouldn't need to be implemented as a CascadingValue. Let me provide a sample that might help illustrate using these concepts in a Parent/Child Relationship. Example From my understanding, the goal is to pass a model property down to a child componenet. The best parctice for this is to use Two-Way Binding. To get started, let's create a custom editor like the following code snippet. Custom Input Editor The following component will behave like a TelerikTextbox. Note the binding of the oninput event and the EditContext cascading parameter. <input value="@Value" @oninput="@OnInputHandler" /> @code {
[Parameter]
public string Value { get; set; }

[Parameter]
public EventCallback <string> ValueChanged { get; set; }

[CascadingParameter]
public EditContext TheEditContext { get; set; }

async Task OnInputHandler(ChangeEventArgs e)
{
Value=e.Value.ToString();

Console.WriteLine(TheEditContext);

await ValueChanged.InvokeAsync(Value);
}
} The Parent Form In the following code snippet, the parent EditForm nests the custom input editor which creates the parent/child relationship. Additionally, the inputs use two-way binding. @page "/" <EditForm Model="@theModel"> <span> InputText: OnChanged </span> <InputText @bind-Value="@theModel.MyProperty"> </InputText> <br /> <br /> <span> Custom Editor: OnInput </span> <MyEditor @bind-Value="@theModel.MyProperty"> </MyEditor> <br /> <br /> <span> Telerik TextBox: OnInput </span> <TelerikTextBox @bind-Value="@theModel.MyProperty"> </TelerikTextBox> <br /> <br /> @theModel.MyProperty </EditForm> @code{
MyModel theModel { get; set; }=new MyModel();
public class MyModel
{
public string MyProperty { get; set; }
}
} Wrapping Up The above sample will print the EditContext to the console after each event is fired for the custom editor which I believe is the overal goal of the implementation. Please let me know if you need any additional information. Thank you for using the Blazor forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Gerrit** answered on 12 Feb 2021

Thanks Eric, In the mean time i finally managed to figuer out what was causing the effects i had. By creating a new instance of the EditContext in the OnParametersSetAsync it got recreated upon each keystroke... resulting in a new (unmodified) EditContext . And as a result upsetting the TelerikTextBox in such a way it lost focus :)
