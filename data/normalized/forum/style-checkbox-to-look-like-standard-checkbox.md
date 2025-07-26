# Style CheckBox to look like standard Checkbox

## Question

**Jon** asked on 11 Jun 2020

Hi How do I style the CheckBox to appear like the standard Check Box? I want it to be large, width=50 <td><InputCheckbox id="chkpopup" class="form-control" style="width: 50px;" @bind-Value="Popup" /> </td> <TelerikCheckBox Id="chkpopup" @bind-Value="@Popup" OnChange="@PopUpCheckChanged"> </TelerikCheckBox> See attachment.. I want the small Telerik CheckBox to appear large and blue. thx

## Answer

**Svetoslav Dimitrov** answered on 12 Jun 2020

Hello Jonathan, I can see you would like our CheckBox to have Bootstrap styling on it. I would suggest you use our Bootstrap theme. In order to do so you can go to the _Host.cshtml file and swap these two lines: Default theme (to be swapped): <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme- default /all.css" /> Bootstrap theme (to swap with): <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme- bootstrap /all.css" /> If you go with the Bootstrap theme you would only need the first part of the CSS rules in the code snippet below, however - if you choose to stick to the default, you would need them both. Also, the Class parameter of the CheckBox should be changed according to the selected theme, I have left a comment in the code snippet for that. <style>.big-checkbox,.big-checkbox::before { font-size: 36px; text-align: center; height: 40px; width: 40px;
} /* The CSS rules below apply if you would like to stick to the default theme
and still get the blue backgroud color. If you use our Bootstrap theme they are redundant and can be removed */.big-checkbox-selected,.big-checkbox-selected::before { font-size: 36px; text-align: center; height: 40px; width: 40px; background-color: blue; border-color: blue;
}
</style> @* If you are using the Bootstrap theme your Class parameter would be: Class="big-checkbox" *@<TelerikCheckBox Id="chkpopup" @bind-Value="@Popup" OnChange="@PopUpCheckChanged" Class="@( Popup==true ? " big-checkbox-selected ": " big-checkbox ")">
</TelerikCheckBox>

@code { public bool Popup { get; set; } void PopUpCheckChanged ( object value )
{
//Your custom logic here
}
} Regards, Svetoslav Dimitrov

### Response

**Jonathan** answered on 12 Jun 2020

thx again!!!!!!!!! Big help
