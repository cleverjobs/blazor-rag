# Example needs WindowAction OnClick event

## Question

**Tyl** asked on 29 Oct 2020

I noticed the example for model window does not have a OnClick event set for the WindowAction [https://demos.telerik.com/blazor-ui/window/modal](https://demos.telerik.com/blazor-ui/window/modal) The problem here is when the close button is clicked it never sets the WindowVisible back to false so if you navigate away and return to the page the Model will show again.

## Answer

**Svetoslav Dimitrov** answered on 30 Oct 2020

Hello Tyler, You observe this behavior because each time the user navigates to a page the OnParametersSet lifecycle hook fires and the property bound to the @bind-Visible is set anew. So if the declaration of the variable looks like this bool WindowVisible=true; as it is in our demo, the event fires, and the value is set to true again. The opposite would be expected too - if you declare it to be false by default the window will not open when the user navigates to the page. This behavior can be observed from the example I added below. You should open the ASP.NET Core Web Server and see the Output tab when navigating back to the page that contains the TelerikWindow. <TelerikWindow Modal="true" @bind-Visible="@isModalVisible"> <WindowTitle> <strong> The Title </strong> </WindowTitle> <WindowContent> I am modal so the page behind me is not available to the user. </WindowContent> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> </WindowActions> </TelerikWindow> <TelerikButton OnClick="@( _=> isModalVisible=true )"> Open the window </TelerikButton> @isModalVisible

@code{
bool isModalVisible { get; set; }=true;

protected override void OnParametersSet()
{
Console.WriteLine("OnParametersSet fired");
base.OnParametersSet();
}
} Regards, Svetoslav Dimitrov

### Response

**Tyler** answered on 30 Oct 2020

Got it, Thanks! noticed however the example is using Visible=@WindowVisible not @bind-Visible="@isModalVisible" Even tho the result is the same, the demo example does not set WindowVisible back to false when closed. bind-Visible does from the example above. If not using @bind-Visible then I would still recommend setting OnClick to update the value. Just don't want others to get confused, especially if they are using the value in other areas of the same route.

### Response

**Svetoslav Dimitrov** answered on 30 Oct 2020

Hello Tyler, Thank you for bringing this to our attention. I have updated the demo to use two-day data binding (@bind-Visible) and it will be live with our next release - 2.19.0. Regards, Svetoslav Dimitrov
