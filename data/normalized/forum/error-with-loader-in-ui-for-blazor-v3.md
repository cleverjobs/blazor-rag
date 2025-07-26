# Error with Loader in UI for Blazor V3

## Question

**Cla** asked on 19 Jan 2022

Hey guys, I just upgraded to the new UI for Blazor 3.0.0 and I have an error 'The type or namespace name 'LoaderSize' does not exist in the namespace 'Telerik.Blazor.Components' (are you missing an assembly reference?)' Is that normal, it was ok with 2.30? Here's my line of code: <TelerikLoader Class="loader-indicator" Type="@LoaderType.InfiniteSpinner" Size="@LoaderSize.Small"></TelerikLoader> Thanks, Claude.

## Answer

**Matthias** answered on 19 Jan 2022

Hi Claude, try this: Size="@ThemeConstants.Loader.Size.Large" Regards Matthias

### Response

**Matthias** commented on 19 Jan 2022

of course you can als use Small instead of Large
