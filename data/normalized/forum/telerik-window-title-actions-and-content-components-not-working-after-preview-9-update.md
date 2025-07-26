# Telerik Window Title, Actions, and Content components not working after preview 9 update

## Question

**Jar** asked on 05 Sep 2019

I've updated to .net preview 9 today and i'm running into an issue with the window components. the TelerikWindow component appears to not have an error, its the child components that appear to be having issues. TelerikWindowTitle TelerikWindowActions TelerikWindowContents I believe the issue is caused by the following change in preview 9. "Replace Microsoft.AspNetCore.Components.UIEventArgs with System.EventArgs and remove the “UI” prefix from all EventArgs derived types (UIChangeEventArgs -> ChangeEventArgs, etc.)." Any idea on when the Telerik Blazor components will be updated to support preview 9?

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hello Jaron, We just shipped the 1.7.0 release that is compatible with Preview 9 (less than a business day after the framework release dropped). Please upgrade to it and things should work :) If not, send me a message. If you are using the CDN for our JS Interop file, don't forget to update its URL too. Regards, Marin Bratanov
