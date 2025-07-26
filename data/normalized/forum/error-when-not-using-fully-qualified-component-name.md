# Error when not using fully qualified component name

## Question

**Chr** asked on 05 Aug 2019

When the TelerikButton component's fully qualified name isn't used I get an error. Examples of working and non-working code below: This works: @page "/teleriktest" @using Telerik.Blazor.Components.TextBox <TelerikTextBox Value="My text value"></TelerikTextBox> <Telerik.Blazor.Components.Button.TelerikButton>My button</Telerik.Blazor.Components.Button.TelerikButton> This does not work @page "/teleriktest" @using Telerik.Blazor.Components.TextBox @using Telerik.Blazor.Components.Button <TelerikTextBox Value="My text value"></TelerikTextBox> <TelerikButton>My button</TelerikButton> I get the error: Unhandled exception rendering component: Object of type 'TestProject.Pages.TelerikButton' does not have a property matching the name 'ChildContent'. As you can see, doing something similar with the TelerikTextBox works fine, so I'm thinking it might not be me.

## Answer

**Chris** answered on 05 Aug 2019

Forgot to include: VS 2019 v16.2.0 Telerik UI v1.4.1

### Response

**Marin Bratanov** answered on 06 Aug 2019

Hello Chris, I can see two likely reasons for this problem: VS 2019 Preview must be used, because the "official" VS 2019 does not work with Blazor (yet) there is a component in the project that is also called TelerikButton: [https://docs.telerik.com/blazor-ui/knowledge-base/components-with-same-name.](https://docs.telerik.com/blazor-ui/knowledge-base/components-with-same-name.) I suspect this is the problem, because the error cites a component whose namespace is TestProject.Pages.TelerikButton - so the TelerikButton component becomes ambiguous. Regards, Marin Bratanov

### Response

**Chris** answered on 06 Aug 2019

Martin, you are a genius :) I had page named TelerikButton.razor Thanks

### Response

**Robert** answered on 10 Oct 2019

Marin, do we still need to use VS 2019? Blazor server side is now official.. I'm using VS 2019 v16.3.2 and Telerik.UI.for.Blazor.Trial 1.7.0 and still have to put a fully qualified name

### Response

**Robert** answered on 10 Oct 2019

After updating to v 2.1.1 everything works..

### Response

**Marin Bratanov** answered on 10 Oct 2019

Hello Robert, Indeed, keeping up to date with our versions is needed, because as the framework gets updates we have to ship releases that support those new versions, and the case is (so far) that new framework versions break old ones. On VS 2019 - yes, it is still needed, and I'd still recommend using the Preview channel even though some features are already in the RTM channel. Regards, Marin Bratanov
