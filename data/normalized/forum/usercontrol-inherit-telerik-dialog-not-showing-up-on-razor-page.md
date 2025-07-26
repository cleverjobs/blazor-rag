# UserControl Inherit Telerik Dialog not showing up on Razor Page

## Question

**Abb** asked on 17 Oct 2022

Hopefully this makes sense. Currently using Telerik Blazor on .net Core 6 C#. I took a Telerik Blazor Dialog and Created my owner user control out of it. I am inheriting from TelerikDialog. I can create a simple telerik dialog on a razor page. It shows and hides like I would expect it. I move that same code off to a UserControl that Inherits from Telerik Blazor Dialog. Then I used that User Control on another Razor page. When I call the User Control, it does not blow up. However.... It does not display anywhere on the page. What is wrong? I have tried putting a really high z-index on it. I mage the control really big. Ther really isn't anything special about this other then it is inheriting Telerik Dialog. When I look for the flag visible, it is set to true. ANy thoughts? If I need to show more details I can. But I Thought I would try this at high level. THanks!

### Response

**Dimo** commented on 20 Oct 2022

Based on the provided information, my assumption is that the Dialog visibility is controlled outside the UI thread, and that's why changes are not applied. See Thread Safety. If that's not the case, please provide a runnable example.
