# Form value not rebinding from within Grid Footer

## Question

**Tod** asked on 22 Apr 2025

I have a grid footer and am needing to bind the sum value with a NumericTextBox (TotalDailyDeposit) that is outside the grid. Both the Grid and NumericTextBox are inside an EditForm. The sum is being calculated/displayed in the grid successfully on row value update, but the value displayed in TotalDailyDeposit isn't being changed when a new sum is calculated in the grid. There is also a second NumericTextBox (PriorDailyLimit) outside of the grid. After changing a value in a grid row I can click in and out of PriorDailyLimit and the TotalDailyDeposit value will update. This only happens, though, if PriorDailyLimit has an OnChange event handler defined (even if the handler contains no code). TotalDailyDeposit will also rebind when a Grid row's Edit button is subsequently clicked. Not updated, just clicked. It seems like the page-level bind events aren't firing from within the footer because the context is the Grid at that point, but do fire based on other subsequent events that occur at the page level. Is there any way to cause a rebind of TotalDailyDeposit from within the Grid footer? Things I've tried: Binding TotalDailyDeposit to a model property Binding TotalDailyDeposit to a page variable Using @bind-Value Using Value/ValueExpression <TelerikNumericTextBox id="PriorDailyLimit" class="form-control form-control-sm" @bind-Value="Model!.PriorDailyLimit" Format="C" Width="150px" Arrows="false" /> ... <FooterTemplate> @{
float? total=(float?)context?.Sum;
if (total !=null)
{
Model!.TotalDailyDeposit=(float)total;
}
else
{
total=0f;
}
}
@(((float)total).ToString("C")) </FooterTemplate>... <TelerikNumericTextBox @bind-Value="Model!.TotalDailyDeposit" class="form-control form-control-sm" Format="C" ReadOnly="true" />

### Response

**Anislav** commented on 23 Apr 2025

It would be helpful if you could extract a minimal sample from your code that reproduces the issue and share it through this site: [https://blazorrepl.telerik.com/](https://blazorrepl.telerik.com/) Regards, Anislav Atanasov

### Response

**Todd** commented on 25 Apr 2025

Thanks... [https://blazorrepl.telerik.com/cfEIQTFs21O7zPTG29](https://blazorrepl.telerik.com/cfEIQTFs21O7zPTG29) If you notice, on page load SummaryValue does not populate with the sum from the grid even though it was set in the footer template via the Model (although it does initially populate when running in any project on my pc). When a grid value is edited/saved, SummaryValue will always be one sum behind. Also, if you click in/out of the AnotherValue textbox after edit/save it will cause SummaryValue to repopulate correctly but only if OnChange is implemented on AnotherValue. Basically what I need is for controls outside the grid to have the most up to date values of grid aggregates. Thanks for your help!

## Answer

**Nadezhda Tacheva** answered on 29 Apr 2025

Hi Todd, Thank you for isolating the code! I revised it and just posted my response in your private ticket but I will also share my observations here for visibility. The problem is related to timing. The template is rendered after the NumericTextBox. The Model.SummaryValue is properly set but nothing forces the component to refresh after that. To handle the scenario, I can suggest the following: Handle OnAfterRenderAsync. Add some delay to give time to the template content to render. Call StateHasChanged() - it is important to ensure you call it only during the first render to avoid an infinite loop. Here is the modified working snippet: [https://blazorrepl.telerik.com/cpOIGDEM27jOz8jb19.](https://blazorrepl.telerik.com/cpOIGDEM27jOz8jb19.) Regards, Nadezhda Tacheva Progress Telerik

### Response

**Todd** answered on 30 Apr 2025

Thanks! I had hit on recalculating the totals in the OnUpdate/OnDelete handlers yesterday afternoon. Not sure why I didn't think of that sooner... forest for the trees. Basically what I ended up with is the following: I have a SetTotals() method in my view model that does its own sum calculation separately from the grid and sets the values for other calculated controls ViewModel.SetTotals() is called in OnAfterRenderAsync() during firstRender to populate the page-level controls on page load ViewModel.SetTotals() is called in the grid's OnUpdate() and OnDelete() handlers ViewModel.SetTotals() is called in OnChange() for all other page-level controls involved in the calculations
