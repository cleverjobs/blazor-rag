# Setting Filterable="true on DropDownList throws an exception

## Question

**Sim** asked on 14 Jun 2021

Hello, When I add the tag Filterable="true" to my DropDownList I get the following exception when I try to click on the dropdown: " Could not find 'TelerikBlazor.initDropDownListFilter' ('initDropDownListFilter' was undefined)." The project build without a problem but the error occurs when I click the dropdown. Am I missing a using statement or what could be the problem?

## Answer

**Marin Bratanov** answered on 14 Jun 2021

Hello Simon, Try following the bullets and ideas from this article: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.) I suspect that the JS Interop file your app uses is either the wrong version, or cached by the browser and dev server. Regards, Marin Bratanov

### Response

**Simon** answered on 15 Jun 2021

Emptying the cache removed the warning but the DropDownList is still looking weird in every browser. Any idea why?

### Response

**Marin Bratanov** commented on 15 Jun 2021

It looks like the Telerik Theme is not registered properly, see the following article on how that should look: [https://docs.telerik.com/blazor-ui/themes/overview.](https://docs.telerik.com/blazor-ui/themes/overview.) There may also be other stylesheets interfering (custom themes, more than one theme, project specific rules) that you may have to remove or fix (e.g., ensure there is only one Telerik Theme registered, regenerate a custom theme from scratch and ensure it is based on the SASS themes we have).
