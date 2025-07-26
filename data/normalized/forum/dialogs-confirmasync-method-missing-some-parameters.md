# Dialogs.ConfirmAsync Method missing some Parameters

## Question

**Joe** asked on 31 Jan 2024

It seems this documentation isn't correct: Blazor Predefined Dialogs - Alert, Confirm, Prompt - Telerik UI for Blazor When I create the following dialog it seems to be missing 2 overloads: bool isDeactivate=await Dialogs.ConfirmAsync($"Deactivate the {ContextLink.Name} {Title}?", "Deactivate Record?", "Yes", "No"); I get this error: Severity Code Description Project File Line Suppression State
Error CS1501 No overload for method 'ConfirmAsync' takes 4 arguments Gsi.Cloud.Maintenance.Rebuild C:\GSI Cloud\Dev\Gsi.Cloud.Maintenance\Gsi.Cloud.Maintenance.Rebuild\Components\ContextLinks\Details.razor.cs 195 Active When I chop out the "yes", "no" parameters then no error. It'd be nice to have the option to set those values as advertised in the documentation... but, its not there.

## Answer

**Hristian Stefanov** answered on 02 Feb 2024

Hi Joel, The ability to customize the text of the predefined dialog buttons was introduced in version 5.1. Therefore, to take advantage of this feature, upgrade your version to our latest version, 5.1. Furthermore, for your convenience, here is an article showing what features each version comes with: Release History. Regards, Hristian Stefanov Progress Telerik
