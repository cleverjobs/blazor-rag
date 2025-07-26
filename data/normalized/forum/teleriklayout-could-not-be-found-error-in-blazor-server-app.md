# TelerikLayout could not be found error in Blazor server app

## Question

**Chr** asked on 24 May 2023

I just installed the Blazor UI components following this article: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) I added "@layout TelerikLayout" to MainLayout.razor and I get a build error: Error CS0246 The type or namespace name 'TelerikLayout' could not be
found (are you missing a using directive or an assembly reference?) The source is Shared_MainLayout_razor.g.cs. I've tried the typical 'clean & rebuild' as well as restarting VS. Any suggestions?

## Answer

**Luis Michel Silva** answered on 25 May 2023

Based on step 6 mentioned in the article you referenced, it instructs you to add a Razor component called TelerikLayout.razor with specific content. However, you mentioned that you received an error stating that the 'TelerikLayout' type or namespace could not be found. The issue might be that you haven't added the TelerikLayout.razor component as instructed in step 6. Make sure you have created the TelerikLayout.razor file and added it to the appropriate location in your project. To resolve the error, follow these steps: Right-click on the "Shared" folder in your Blazor project. Select "Add" and then "New Item" from the context menu. In the "Add New Item" dialog, choose "Razor Component" from the list of templates. Name the file as "TelerikLayout.razor" and click the "Add" button. Replace the default content of the TelerikLayout.razor file with the specific content mentioned in the article you followed. After adding the TelerikLayout.razor file with the correct content, rebuild your project to see if the error is resolved. Remember to import the necessary namespace in your MainLayout.razor file by adding @using Telerik.Blazor.Layouts at the top. If you continue to experience issues, ensure that you have followed all the steps in the article correctly and that you have the necessary dependencies and packages installed.

### Response

**Chris** commented on 26 May 2023

Well that was dumb of me LOL. Thanks for the assistance.

### Response

**Nicolaas** commented on 02 Nov 2023

there is no step 6 in reference article? oh its step 4.6

### Response

**Chris** answered on 26 May 2023

See Luis' comment.
