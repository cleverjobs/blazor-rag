# Change Title of TelerikGrid (Groupable)

## Question

**duk** asked on 22 Jun 2023

Hi, I need to change the standard text of " Drag a column header and drop it here to group by that column". How can I change the Title of this? Thanks in advance! Best Regards Paul

## Answer

**Hristian Stefanov** answered on 26 Jun 2023

Hi Paul, I confirm that the desired result is easily achievable through localization. The Telerik UI for Blazor components use a set of keys that a localization service resolves to the strings that will be rendered in the UI. The Telerik NuGet package carries a ".resx " file (as a resource), out of the box, with the default (English) strings. The " Drag a column header and drop it here to group by that column " text is a default English string. That said, changing keys in Telerik components (like Grid), requires customizing the desired keys in the ".resx " file (resource). In the current case, search for the " Group_Empty " key in the " TelerikMessages.resx " file and change it. I hope you find the above information helpful. If we can assist with further guidance, I'm at your disposal. Regards, Hristian Stefanov
