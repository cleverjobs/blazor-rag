# Popup stops appearing after clicking on the inputbox

## Question

**NiV** asked on 04 Sep 2023

Hi there. Using the Grid component, setting "Navigable" to "true" and having a DropDownList makes the popup of the component not appear after the user has clicked on the input box. The DropDownList has a button (with an arrow pointing down) on its right side. Clicking on the button makes the popup appear. The popup also appears if the user clicks on the input box of the component, but this last scenario does not happen if the component is inside a Grid which has "Navigable" set to "true". In this state, the button mentioned also makes the popup not appear. Here is a gif which showcases this behaviour: [https://i.gyazo.com/a071f9fba72d08261d438e31b240d606.mp4](https://i.gyazo.com/a071f9fba72d08261d438e31b240d606.mp4) This also affects the ComboBox component: [https://i.gyazo.com/bcf2f10a6a6c923d825865ecdf0a7f5a.mp4](https://i.gyazo.com/bcf2f10a6a6c923d825865ecdf0a7f5a.mp4) Here is the REPL link: [https://blazorrepl.telerik.com/mnkDOScb41h1aOK602](https://blazorrepl.telerik.com/mnkDOScb41h1aOK602)

## Answer

**Dimo** answered on 07 Sep 2023

Hi Fabio, By default, the Grid doesn't assume that its display template will contain an editor. In your case, please wrap the DropDownList in: <span @onclick:stopPropagation> <TelerikDropDownList @bind-Value="@item.UserType" Data="@item.Types"> </TelerikDropDownList> </span> Regards, Dimo Progress Telerik
