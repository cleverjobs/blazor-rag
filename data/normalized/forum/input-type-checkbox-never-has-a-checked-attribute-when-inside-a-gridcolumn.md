# <<input type="checkbox"> never has a "checked" attribute when inside a <GridColumn>

## Question

**Rol** asked on 14 Sep 2021

Using the latest Telerik for Blazor in a Blazor Server web application. <GridColumn...> <Template> @{
var alert=(...)context; // NB: Telerik suppresses the checked attribute, but the UI is correct and onchange() works <input type="checkbox" checked="@(alert.Checked)" @onchange="@(e=> ...(alert, (bool)e.Value!))" /> } </Template> </GridColumn>

### Response

**Roland** commented on 14 Sep 2021

Nevermind. When I use bUnit to render the <TelerikGrid> without a browser, the rendered HTML does contain the checked="" attribute when the input is checked, so it may have something to do with the Chrome Debugger tools.
