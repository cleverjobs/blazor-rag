# Telerik ComboBox bind-Value not selected after async data load

## Question

**And** asked on 28 Apr 2021

Hi, I have burned some time trying to understand why ComboBox is not selecting predefined value. If myComboData is null/empty initially and loaded from remote API then predefined value is not selected. Workaround 1: Set _selectedValue to -1 and then back to 2 to trigger selection. Workaround 2: Wrap combo with if(myComboData !=null). Both seem dirty to me. In samples ( [https://demos.telerik.com/blazor-ui/combobox/overview](https://demos.telerik.com/blazor-ui/combobox/overview) ) we don't have a null checks. <TelerikComboBox @bind-Value=_selectedValue Data="@myComboData" TextField="MyTextField" ValueField="MyValueField" TValue="int" TItem="MyDdlModel">
</TelerikComboBox>

@code { int _selectedValue { get; set; }=2; // Preselected value IEnumerable<MyDdlModel> myComboData { get; set; }=Enumerable.Empty<MyDdlModel>(); protected override async Task OnInitializedAsync ( ) {
myComboData=await LoadData(); await base.OnInitializedAsync();
} private async Task<IEnumerable<MyDdlModel>> LoadData()
{ await Task.Delay( 1 ); return Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
}
}

## Answer

**Marin Bratanov** answered on 29 Apr 2021

Hi Andrzej, This will be fixed in our next release (2.24.0), you can check its portal page for more details. Regards, Marin Bratanov

### Response

**Mikael** commented on 01 Oct 2021

Hello! Will this be fixed for the TelerikDropDownList as well?

### Response

**Marin Bratanov** commented on 02 Oct 2021

Are you perhaps hitting this issue: [https://feedback.telerik.com/blazor/1518099-selected-text-does-not-update-when-changing-the-data-collection?](https://feedback.telerik.com/blazor/1518099-selected-text-does-not-update-when-changing-the-data-collection?) If yes, do click the Vote and Follow buttons on its page. If not, I suggest you open a new ticket where you can add a small snippet/sample to show the issue. The original report, changed to a dropdownlist seems to work fine for me, Item 2 is selected initially (I tested with 2.27.0): <TelerikDropDownList @bind-Value=_selectedValue Data="@myComboData" TextField="MyTextField" ValueField="MyValueField" TValue="int" TItem="MyDdlModel">
</TelerikDropDownList>

@code { int _selectedValue { get; set; }=2; // Preselected value IEnumerable<MyDdlModel> myComboData { get; set; }=Enumerable.Empty<MyDdlModel>(); protected override async Task OnInitializedAsync ( ) {
myComboData=await LoadData(); await base.OnInitializedAsync();
} private async Task<IEnumerable<MyDdlModel>> LoadData()
{ await Task.Delay( 1 ); return Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
}
}

### Response

**Robert** commented on 03 Dec 2021

I am experiencing this problem with version 2.29 when the drop-down list is in a "component" It seems to be intermittent but dependent on how long the async method takes to complete. Edit page @page "/"
@using System.Diagnostics
@using System.Threading
@using BlazorApp1.Components <h1> Hello, world! </h1> <EditForm class="form-inline" Model="@Model"> <MyComponent /> </EditForm> Welcome to your new app.

@code {
object Model=new();
private Guid InstanceId;

public Index()
{
InstanceId=Guid.NewGuid();
Debug.WriteLine($"Index - {InstanceId}");
}

protected override Task OnInitializedAsync()
{
Debug.WriteLine("Index - OnInitializedAsync");
return base.OnInitializedAsync();
}

protected override Task OnParametersSetAsync()
{
Debug.WriteLine("Index - OnParametersSetAsync");
return base.OnParametersSetAsync();
}
} Component @using System.Diagnostics <h3> My Component </h3> <br /> <TelerikDropDownList @bind-Value=_selectedValue Data="@myComboData" TextField="MyTextField" ValueField="MyValueField" TValue="int" TItem="MyDdlModel"> </TelerikDropDownList> <br /> <TelerikButton OnClick="@SayHelloHandler" Primary="true"> Say Hello </TelerikButton> <br /> @helloString <br /> @code {
private Guid InstanceId;
MarkupString helloString;

int _selectedValue { get; set; }=2; // Preselected value
IEnumerable <MyDdlModel> myComboData { get; set; }=Enumerable.Empty <MyDdlModel> ();

void SayHelloHandler()
{
string msg=string.Format("Hello from <strong> Telerik Blazor </strong> at {0}. <br /> Now you can use C# to write front-end!", DateTime.Now);
helloString=new MarkupString(msg);
}

public MyComponent()
{
InstanceId=Guid.NewGuid();
Debug.WriteLine($"MyComponent - {InstanceId}");
}

protected override async Task OnInitializedAsync()
{
Debug.WriteLine("MyComponent - OnInitializedAsync");
myComboData=await LoadData();
await base.OnInitializedAsync();
}

protected override Task OnParametersSetAsync()
{
Debug.WriteLine("MyComponent - OnParametersSetAsync");
return base.OnParametersSetAsync();
}

private async Task<IEnumerable <MyDdlModel>> LoadData()
{
await Task.Delay(100);
return Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
}

public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
}
}

### Response

**Marin Bratanov** commented on 05 Dec 2021

A potential reason could be that when <MyComponent> re-renders (due to the data arriving) its parent also re-renders, and re-initializes <MyComponent> with its initial state. I'd suggest tracking through the OnAfterRender events and which fires when, and see if keeping the value in the parent component helps (right now it is not kept). Also, see this thread [https://feedback.telerik.com/blazor/1545143-telerikdropdownlist-binding-does-not-work-correctly-when-using-components-and-async-methods](https://feedback.telerik.com/blazor/1545143-telerikdropdownlist-binding-does-not-work-correctly-when-using-components-and-async-methods)
