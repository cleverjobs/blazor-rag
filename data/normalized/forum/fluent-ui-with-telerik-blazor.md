# Fluent UI with Telerik Blazor

## Question

**Joe** asked on 16 Feb 2025

Do you have any examples that show Fluent UI working in the same project with Telerik Blazor?

### Response

**Dimo** commented on 19 Feb 2025

Hi Joel, the Telerik UI for Blazor team hasn't implemented such examples. If there is some integration issue that requires our attention, please elaborate and send a runnable example.

## Answer

**Joel** answered on 19 Feb 2025

I have attached an example project that doesn't work. The main question is around what the MainLayout should look like. We have the TelerikRootComponent but we also have the FluentMainLayout. Which one should be the actual root? <TelerikRootComponent> <CascadingValue Value="this"> <div class="k-content"> <div class="container"> <FluentDesignTheme StorageName="gsi-design-theme" /> <FluentStack HorizontalAlignment="HorizontalAlignment.SpaceBetween" VerticalAlignment="VerticalAlignment.Bottom"> <FluentNavLink href="@LogoUrl"> <img src="@LogoImageUrl" height="100" width="200" /> </FluentNavLink> <FluentNavLink href="@AccountUrl" class="gsi-color-black gsi-hyperlink-underline gsi-keyboard-focusable-not"> <h1> @AccountName </h1> </FluentNavLink> </FluentStack> <FluentCheckbox Label="Show Jump Menu" ValueChanged="@(args=> OnIsShowJumpMenuChanged(args))" /> <FluentCheckbox Label="Is Logged In" ValueChanged="@(args=> OnIsLoggedInChanged(args))" /> <FluentMainLayout NavMenuTitle="Navigation menu"> <Header> <FluentStack HorizontalAlignment="HorizontalAlignment.SpaceBetween" VerticalAlignment="VerticalAlignment.Center"> <FluentStack> <FluentNavLink> Home </FluentNavLink> <FluentNavLink> About </FluentNavLink> </FluentStack> <FluentStack HorizontalAlignment="HorizontalAlignment.Right"> @if (IsLoggedIn)
{ <FluentNavLink> Logout </FluentNavLink> }
else
{ <FluentNavLink> Login </FluentNavLink> } <FluentIcon Value="@(new Icons.Regular.Size20.Settings())" Color="Color.FillInverse" OnClick="@ShowSettingsAsync" /> </FluentStack> </FluentStack> </Header> <Body> @if (IsShowJumpMenu)
{ <div class="gsi-background-color-darkgray gsi-color-white"> <FluentStack HorizontalAlignment="HorizontalAlignment.Right" Orientation="Orientation.Horizontal"> <FluentNavLink Href="/" Text="Home"> Users </FluentNavLink> <FluentNavLink Href="/" Text="Home"> Groups </FluentNavLink> <FluentNavLink Href="/" Text="Home"> Devices </FluentNavLink> <FluentNavLink Href="/" Text="Home"> Patients </FluentNavLink> <FluentNavLink Href="/" Text="Home"> Sessions </FluentNavLink> </FluentStack> </div> }

@Body </Body> </FluentMainLayout> <FluentDialogProvider /> </div> </div> </CascadingValue> </TelerikRootComponent>

### Response

**Dimo** commented on 19 Feb 2025

@Joel Please follow our Getting Started guides to setup Telerik UI for Blazor correctly. The provided app is missing: Telerik JavaScript file in App.razor Telerik theme in App.razor Telerik namespaces in _Imports.razor See: First steps with Blazor Web Apps A more advanced version of the previous link The nesting order of the Telerik and Fluent root components may or may not matter, depending on the exact usage. Based on my understanding what the FluentMainLayout does, keep your current setup with the TelerikRootComponent on the "outside". You need to comply with these recommendations and avoids this problem.

### Response

**Joel** commented on 19 Feb 2025

Okay, but this doesn't answer the original question.

### Response

**Dimo** commented on 19 Feb 2025

I edited my previous post.
