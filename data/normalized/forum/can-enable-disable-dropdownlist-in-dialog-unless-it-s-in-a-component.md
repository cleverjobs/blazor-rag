# Can enable/disable DropDownList in dialog unless it's in a component

## Question

**Kyl** asked on 22 Feb 2025

EDIT: Title should say *Can't* enable/disable DropDownList rather than *Can* I have a Dialog component with a DropDownList and a MultiSelect. When no items are selected in the MultiSelect, I want the DropDownList to be disabled. I've set it up like so: <TelerikDropDownList Data="@Data" @bind-Value="@SelectedValue" Enabled="@IsEnabled" /> <TelerikMultiSelect Data="@SelectData" TextField="Text" ValueField="TheValue" OnChange="@SelectChange" @bind-Value="@SelectValue" /> @code {

public class MyData
{
public string Text { get; set; }
public string TheValue { get; set; }
}

private string @SelectedValue { get; set; }="One";

private List <string> Data { get; set; }=[
"One",
"Two",
"Three"
];

private List <MyData> SelectData { get; set; }=[
new MyData { Text="One", TheValue="1" },
new MyData { Text="Two", TheValue="2" },
new MyData { Text="Three", TheValue="3" }
];

private List <string> SelectValue { get; set; }=[];
private bool IsEnabled=false;
private void SelectChange()
{
IsEnabled=SelectValue.Count> 0;
}

} When I put the DropDownList and MultiSelect directly into a Dialog, this doesn't work. Specifically, when I add items to the MultiSelect, the DropDownList doesn't get enabled. However, when I move this exact same code into a separate component and then embed THAT component into the Dialog, then it does. Any ideas why that would be? I have a reproduction of the issue here: [https://github.com/kbaley/TelerikBlazor/blob/main/TelerikBlazor/TelerikBlazor.Client/Pages/Home.razor](https://github.com/kbaley/TelerikBlazor/blob/main/TelerikBlazor/TelerikBlazor.Client/Pages/Home.razor) EDIT: I've tried calling StateHasChanged in the SelectChange handler but it doesn't change the behaviour.

## Answer

**Tsvetomir** answered on 24 Feb 2025

Hello Kyle, Thank you for the provided code snippets and clear explanation about the encountered issue. To achieve the desired result, use the Dialog Refresh() method, to re-render the Dialog content. This will ensure that the DropDownList is enabled after the selection in the MultiSelect. To assist you further, I've modified the provided code snippet: <PageTitle> Home </PageTitle> <h1> Hello, world! </h1> Welcome to your new app. <TelerikButton ThemeColor="@ThemeConstants.Button.ThemeColor.Primary" OnClick="@SayHelloHandler"> Say Hello </TelerikButton> <p> @HelloString </p> <TelerikDialog Width="500px" @bind-Visible="@DialogVisible" @ref="@DialogRef"> <DialogContent> <h2> Component </h2> <TestComponent /> <h2> Embedded </h2> <TelerikDropDownList Data="@Data" @bind-Value="@SelectedValue" Enabled="@IsEnabled" /> <TelerikMultiSelect Data="@SelectData" TextField="Text" ValueField="TheValue" OnChange="@SelectChange" @bind-Value="@SelectValue" /> </DialogContent> </TelerikDialog> @code {

public class MyData
{
public string Text { get; set; }
public string TheValue { get; set; }
} private TelerikDialog DialogRef { get; set; } private MarkupString HelloString { get; set; }
private string @SelectedValue { get; set; }="One";
private List <string> Data { get; set; }=[
"One",
"Two",
"Three"
];
private List <MyData> SelectData { get; set; }=[
new MyData { Text="One", TheValue="1" },
new MyData { Text="Two", TheValue="2" },
new MyData { Text="Three", TheValue="3" }
];
private List <string> SelectValue { get; set; }=[];
private bool DialogVisible { get; set; }=false;

private bool IsEnabled=false;

private void SayHelloHandler()
{
string msg=$"Hello from <strong> Telerik UI for Blazor </strong> at {DateTime.Now.ToString("HH:mm:ss")}!" +
" <br /> Now you can use C# to write front-end!";

HelloString=new MarkupString(msg);
DialogVisible=true;
}

private void SelectChange()
{
IsEnabled=SelectValue.Count> 0; DialogRef.Refresh(); }
} Regards, Tsvetomir
