# Changing Notification size isn't working?

## Question

**RobRob** asked on 20 May 2025

In my _Host.cshtml <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <base href="~/" /> <component type="typeof(ApplicationInsightsInit)" render-mode="ServerPrerendered" /> <link href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css?@telerikUiForBlazorVersion" rel="stylesheet" /> <link href="_content/Telerik.UI.for.Blazor/css/kendo-font-icons/font-icons.css" rel="stylesheet" /> <link href="lib/fontawesome/css/all.css" rel="stylesheet" /> <link href="css/styles.css" rel="stylesheet"> <link href="css/site.css" rel="stylesheet" /> In my Site.css .TelerikNotification.k-notification-container.k-notification { width: 300px; height: 50px; font-size: 1.5em; text-align: center;
}.wide-notification-center.k-notification { width: 750px; height: 70px; font-size: 1.5em; text-align: center;
} Blazor Page <TelerikNotification @ref="@NotificationRefWide" Class="wide-notification-center" HorizontalPosition="@NotificationHorizontalPosition.Center" AnimationDuration="3000"> </TelerikNotification> C# page code (server side) public TelerikNotification NotificationRefWide { get; set; }

NotificationRefWide.Show( new NotificationModel()
{
Text="Warning: " + message,
ThemeColor=ThemeConstants.Notification.ThemeColor.Warning,
Closable=true,
CloseAfter=duration,
Icon=FontIcon.WarningTriangle,
ShowIcon=true }); Any changes I make in the Site.css have ZERO impact on the display of the notification (see attached image). In fact, I can remove the class definitions from CSS and still get the same results. It's as if Telerik Notification is completely ignoring the class reference? Any suggestions? Rob.

### Response

**Rob** commented on 20 May 2025

UPDATE: If I move the style .wide-notification-center.k-notification { width: 750px; height: 70px; font-size: 1.5em; text-align: center;
} to the Blazor Page <style>.disabled-row { pointer-events: none; color: gray;
}.disabled-row button { opacity: 0.6;
}.bookingCellFormat { color: blue;
}.warningText { color: red;
}.wide-notification-center.k-notification { width: 750px; height: 70px; font-size: 1.5em; text-align: center;
}
</style> It works as expected. The issue seems to be that the Sites.css is being ignored? I don't understand why? It's referenced in my _Host.cshtml file. On a side note, I am using TailwindCss but that generates the styles.css completely separate. Unless, there is some sort of incompatibility between TailwindCSS and Telerik? Thoughts?

## Answer

**Rob** answered on 21 May 2025

Thanks for response Dimo. The issue was actually a cache problem. Ctrl + F5 on the client resolved it. Since telling our users to Ctrl + F5 to clear the cache is support intensive, I used the following approach to ensure on a per deployment basis, the user cache will be "refreshed": _Host.cshtml <link asp-href-include="css/site.css" rel="stylesheet" /> <header> <script asp-src-include="~/lib/jquery/dist/jquery.min.js"> </script> <script asp-src-include="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"> </script> <script asp-src-include="~/js/site.js"> </script> </header> Program.cs: using Microsoft.AspNetCore.Mvc.Rendering;

builder.Services.AddSingleton<ITagHelperInitializer<ScriptTagHelper>, AppendVersionTagHelperInitializer>();
builder.Services.AddSingleton<ITagHelperInitializer<LinkTagHelper>, AppendVersionTagHelperInitializer>();
builder.Services.AddSingleton<ITagHelperInitializer<ImageTagHelper>, AppendVersionTagHelperInitializer>(); public class AppendVersionTagHelperInitializer: ITagHelperInitializer <ScriptTagHelper>, ITagHelperInitializer <LinkTagHelper>, ITagHelperInitializer <ImageTagHelper>
{ private const bool DefaultValue=true; public void Initialize ( ScriptTagHelper helper, ViewContext context ) {
helper.AppendVersion=DefaultValue;
} public void Initialize ( LinkTagHelper helper, ViewContext context ) {
helper.AppendVersion=DefaultValue;
} public void Initialize ( ImageTagHelper helper, ViewContext context ) {
helper.AppendVersion=DefaultValue;
}
} Rob.

### Response

**Dimo** answered on 21 May 2025

Hello Rob, We are not setting Notification dimensions, so your styles should work no matter where they are. Show the Notification for a very long time and use the DOM inspector to see what other styles override the ones that don't work. Regards, Dimo Progress Telerik
