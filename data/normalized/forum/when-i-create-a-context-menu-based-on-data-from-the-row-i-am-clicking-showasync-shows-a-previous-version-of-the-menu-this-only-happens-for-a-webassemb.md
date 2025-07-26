# When I create a context menu based on data from the row I am clicking, ShowAsync shows a previous version of the menu. This only happens for a WebAssembly project

## Question

**Kur** asked on 22 Sep 2021

I have a project with a grid and a context menu. When I right click on a grid cell, I create a contextual menu based on the name in the grid row. Then when I run the await ContextMenuRef.ShowAsync(mouseEventArgs.ClientX, mouseEventArgs.ClientY); command, the menu is from the previous right click and previous row. The actions performed based on the menu choice happen for the right row but the menu itself, it shows previous values. I have included my mock project for your perusal. Click on Invoices to get to the page with the problem.

## Answer

**Radko** answered on 24 Sep 2021

Hi Kurt, Thank you for the detailed explanation of the behavior, as well as for the runnable application. Indeed this is rather peculiar and is something we would need to investigate further. I have created a Bug Request on our feedback portal on your behalf, and have already added your vote there. I have also updated your Telerik Points as a gesture of appreciation. It does look like a timing issue as either making MakeMenuItems() async and calling Task.Yield() within it, or simply adding Task.Delay(1) after the call seems to resolve the issue and is a plausible workaround you can use for the time being. Here are the two approaches: async Task MakeMenuItems ( ) {
MenuItems=new List<MenuItem>()
{ ... }; await Task.Yield(); } or MakeMenuItems(); await Task.Delay( 1 ); await ContextMenuRef.ShowAsync(mouseEventArgs.ClientX, mouseEventArgs.ClientY); Regards, Radko Stanev Progress Telerik
