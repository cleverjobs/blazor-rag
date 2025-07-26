# How to display third-party icon in Button or GridCommandButton in 4.0.00 ?

## Question

**Bru** asked on 19 Jan 2023

Before upgrading to 4.0, I used to define a GridCommandButton this way (with FontAwesome custom icons) : <GridCommandButton Icon Class="fal fa-sync-alt fa-lg" OnClick="Refresh"> @Resources.Refresh </GridCommandButton> But now with 4.0, IconClass parameter has been removed. Documention says to use Icon parameter, that only accept a FontIcon or SvgIcon object value. But how do a use those to display my custom icon in above code?

### Response

**Adrian** commented on 19 Jan 2023

Same here, this seems to be the same across the board... <TelerikButton Icon="file"> Like </TelerikButton> results in the exception: The name 'file' does not exist in the current context

### Response

**Bruno** commented on 20 Jan 2023

I opened a ticket for this issue and here is the answer from support team: This was indeed a change that was rolled out with the major version upgrade (3.7 to 4.0). Please take a moment to review the UI for Blazor 4.0.0 (telerik.com) Release
Notes and the two breaking changes mitigation articles (linked in the
release notes), which explains the changes more clearly. There are a couple of options to continue to use third-party Icons such as FontAwsome: 1. Include the Icon in a span like this: <TelerikButton> <span class="fa-solid fa-ghost"> </span> Ghost </TelerikButton> 2. Use the Icon parameter like this: <TelerikButton Icon="@(" fa-solid fa-pizza-slice ")"> Pizza </TelerikButton>

### Response

**Adrian** commented on 20 Jan 2023

Thanks, I definitely read that article but don't recall seeing that example for the icon parameter.

### Response

**Bruno** commented on 20 Jan 2023

Breaking changes documentation has been updated just yesterday. I got the same reaction. By the way, there is still an issue if you use fontawesome icon with size (like "fa-large") other than default: the icon is offset and overlap the button. Dev team is aware of that, and a fix is planned for next week. In the mean time, you can use a workaround using styles. A runnable example is available here: [https://blazorrepl.telerik.com/cRubcEvH466BA32i45](https://blazorrepl.telerik.com/cRubcEvH466BA32i45)

### Response

**Ivan** commented on 22 Jan 2023

The Icon parameter don't apply custom css classes. Create simple TelerikBlazor App Template and type: <TelerikButton Icon="@("oi oi-plus") " /> The icon will be empty.
