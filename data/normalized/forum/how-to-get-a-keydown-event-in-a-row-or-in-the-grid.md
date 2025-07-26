# how to get a KeyDown event in a row or in the grid

## Question

**Dan** asked on 29 Jul 2021

Greetings, could you help me with the information on how I obtain a keyDown event in the grid, or a row of this, what happens is that I need to obtain when the user presses the delete key in order to eliminate the current row that he is selecting. I use Blazor 2.25 web server vs 2019

## Answer

**Matthias** answered on 31 Jul 2021

Hello Danny, sorry, I used it for searching the grid and didn't need the "escape" key. But there is also a solution for that. razor: @page "/"
@using System.Collections.ObjectModel <h1> Hello, world! </h1> Welcome to your new app. <div @ref="testRef" tabindex="0" @onkeydown="HandleKeyDown"> <TelerikGrid Data="@customers"> <GridColumns> <GridColumn Field="@nameof(Customer.Name)" Title="Name"> </GridColumn> <GridColumn Field="@nameof(Customer.City)" Title="City"> </GridColumn> </GridColumns> </TelerikGrid> </div> @pressedKey code: @code{ private ElementReference testRef; private string pressedKey; public ObservableCollection<Customer> customers { get; set; } protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{ await testRef.FocusAsync();
}
} protected override void OnInitialized ( ) {
customers=new ObservableCollection<Customer>();
customers.Add( new Customer()
{
Name="Tom", City="Berlin" });
customers.Add( new Customer()
{
Name="Tim", City="New York" });
customers.Add( new Customer()
{
Name="Jim", City="Paris" }); base.OnInitialized();
} private void HandleKeyDown ( KeyboardEventArgs e ) {
pressedKey=e.Key;
} public class Customer { public string Name { get; set; } public string City { get; set; }
}
} Important: the ref needs the focus and the tabindex Attached is a small video showing the behavior after pressing the escape key. Have a nice weekend - Greetings Matthias

### Response

**Matthias** commented on 31 Jul 2021

there is still a bug - once the grid has the focus. I'll have a look at the weekend - I think it should be possible with Javascript.

### Response

**Matthias** answered on 29 Jul 2021

Hi - I use a key handler Have a look at the snippet: <div @onkeypress="@KeyHandler"> <TelerikGrid Data="@Customers" Height="100%" Pageable="true" PageSize="15" Resizable="true" Sortable="true" Navigable="true" ScrollMode="GridScrollMode.Scrollable" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@(nameof(customer.CustName))" Visible="false" /> <GridColumn Field="@(nameof(customer.CustCity))" Width="80px" Visible="false" /> <GridColumn Field="@(nameof(customer.CustPhone))" /> <GridColumn Field="@(nameof(customer.CustZip))" Width="80px" /> </GridColumns> </TelerikGrid> </div> and the handler: public string aKey { get; set; } void KeyHandler ( KeyboardEventArgs e ) {
aKey=$"pressed: {e.Key} ";

} this works perfect in my scenario Best regards Matthias

### Response

**Matthias** commented on 29 Jul 2021

of course you have to check which row is selected :) and then you can delete the row

### Response

**Danny** commented on 30 Jul 2021

Greetings, Thank you very much for the comment, if I had imagined something like that, a shame that the Telerik Blazor controls are very basic in events, we hope you hear our prayers and increase the benefits of the controls.

### Response

**Matthias** answered on 01 Aug 2021

Hi Danny, as I had already suspected, it will probably not work without JavaScript. I have written a small script for this, which now intercepts all keystrokes and then calls "dotnet" from the script. the parameter: jsInteropTest: assemblyname jsKeyHandler: methodname insert in a suitable place: (_Host.cshtml, index.html) <script> window.onload=function ( ) {
eventHandler=function ( e ) { if (e.keyCode==46 || e.keyCode==8 )
{
DotNet.invokeMethodAsync( 'jsInteropTest', 'jsKeyHandler',e.keyCode);

}

} window.addEventListener( 'keydown', eventHandler, false );
}
</script> In the code, the corresponding method is then called: (I have implemented the method in MainLayout.) [ JSInvokable( "jsKeyHandler" ) ] public static void jsKeyHandler ( object text ) { string FromjsKey=text.ToString();

} From there, the value can then be transmitted. (Cascading value, State Container...) The advantage now is that this method should work for all components. ... And here a complete example with CascadingParameter: MainLayout @using System.ComponentModel
@using jsInteropTest.Data
@inherits LayoutComponentBase

<TelerikRootComponent>
<div class="page">
<div class="sidebar">
<NavMenu />
</div>

<div class="main">
<div class="top-row px-4">
<a href="[https://docs.microsoft.com/aspnet/"](https://docs.microsoft.com/aspnet/") target="_blank">About</a>
</div>

<div class="content px-4">
<CascadingValue Value=@jsKey Name="KEY">
@Body
</CascadingValue>
</div>

</div>
</div>
</TelerikRootComponent>

@code
{ public string jsKey { get; set; } private static Func<string, Task> KeyDownAction; private async Task LocalKeyDownAction ( string value ) {
jsKey=value; await InvokeAsync(StateHasChanged);

}

[ JSInvokable( "jsKeyHandler" ) ] public static async Task jsKeyHandler ( object text ) { await KeyDownAction(text.ToString());

} protected override void OnInitialized ( ) {
KeyDownAction=LocalKeyDownAction;

}


} the page/component with the grid: @page "/" @using System.Collections.ObjectModel
@using Microsoft.JSInterop;
@inject IJSRuntime _jsRuntime

<h1>Hello, world!</h1>

<TelerikGrid Data="@customers">
<GridColumns>
<GridColumn Field="@nameof(Customer.Name)" Title="Name"></GridColumn>
<GridColumn Field="@nameof(Customer.City)" Title="City"></GridColumn>
</GridColumns>
</TelerikGrid>
<span>
User pressed: @jsKey
</span>

@code{

[ CascadingParameter(Name="KEY" ) ] string jsKey { get; set; } public ObservableCollection<Customer> customers { get; set; } protected override void OnInitialized ( ) {
customers=new ObservableCollection<Customer>();
customers.Add( new Customer()
{
Name="Tom", City="Berlin" });
customers.Add( new Customer()
{
Name="Tim", City="New York" });
customers.Add( new Customer()
{
Name="Jim", City="Paris" }); base.OnInitialized();
} public class Customer { public string Name { get; set; } public string City { get; set; }
}
} As an attachment the complete code

### Response

**Danny** answered on 30 Jul 2021

Matthias, I tell you that it implements what you mention, and it does not enter the KeyPress of the div, the telerik grid steals the key event

### Response

**Danny** answered on 30 Jul 2021

Matthias, it works but with keyUp, not with keypress or keyDown
