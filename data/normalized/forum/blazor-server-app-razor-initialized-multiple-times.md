# Blazor Server App.razor Initialized Multiple Times

## Question

**Cod** asked on 30 Oct 2023

Greetings, When adding the TelerikRootComponent to the MainLayout.razor, the App.razor is initialized multiple times. If I remove the TelerikRootComponent, then App.razor is initialized once as expected. The problem is within App.razor, we use the NavigationManager to navigate to a login endpoint when a user is not authorized. The navigation now gets triggered multiple times before actually completing. What change do I need to make in order to have the App.razor initialize once while still using TelerikRootComponent? I followed the guide wrapping @Body with TelerikRootComponent and then tried creating the TelerikLayout which had the same result. This is in a .NET 7 Blazor Server app. Thanks in advance for the help.

### Response

**Dimo** commented on 02 Nov 2023

Cody, on my side OnInitialized of App.razor fires twice, no matter if there is a TelerikRootComponent in the layout or not. (Thе second execution is due to the ServerPrerendered render mode of the application). Do I understand correctly that you are not using the usual way to redirect inside <RedirectToLogin />? What happens if you move the <TelerikRootComponent> to App.razor and wrap it around the <Router>? If you have <CascadingAuthenticationState> in App.razor, then place our root component inside it. If the problem persists, please provide a simple runnable project for inspection.

### Response

**Cody** commented on 03 Nov 2023

I believe we have it figured out. To answer your questions first for context, we are using the <CascadingAuthenticationState> and moving the <TelerikRootComponent> into the App.razor like you suggested did not fix the issue but got me rethinking things. I ended up moving our navigation logic to the OnInitializedAsync method of MainLayout.razor which then fires the redirect after App.razor has finished loading, which is the desired end result I was looking for. The App.razor still loads five times for me but I believe this is just how it works with the <CascadingAuthenticationState> and doesn't impact anything else. @Dimo your comments were helpful in working out the root of the problem. I appreciate your time.

### Response

**Dimo** commented on 03 Nov 2023

Great, thanks for sharing, Cody!

## Answer

**Cody** answered on 03 Nov 2023

The answer for this question is checking the AuthenticationState of a user in MainLayout.razor instead of the App.razor, because App.razor may need to render multiple times. Using the TelerikRootComponent made this issue more apparent, but was not the root cause of our issue.
