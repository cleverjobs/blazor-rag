# Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined)

## Question

**Ale** asked on 07 Jul 2021

I receive from other developer workable application with Blazor and Telerik UI. I have installed Telerik UI successfully to my machine, then install package Telerik.UI.for.Blazor.Trial. Site successfully compiled and started. But Blazor UI don't working.

## Answer

**Matthias** answered on 07 Jul 2021

have a look at this comments [https://www.telerik.com/forums/could-not-find-%27telerikblazor-getlocationhost%27-(%27telerikblazor%27-was-undefined)](https://www.telerik.com/forums/could-not-find-%27telerikblazor-getlocationhost%27-(%27telerikblazor%27-was-undefined)) this should help you

### Response

**Alex** commented on 07 Jul 2021

Thank you, @Mattias But I don't update anything, I only read project without ant changing from Azure. I must continue developing from after previous programmer in the same .NET Core version, the same Telerik UI version.

### Response

**Matthias** answered on 08 Jul 2021

Hi Alex - this is not only about updates - there are some tips about the location of the JS and the defer attribute. I had the same problem while I was testing with a slow connection. You can read a little bit more there: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors?_ga=2.214987024.621073099.1625649572-1693785563.1625649572](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors?_ga=2.214987024.621073099.1625649572-1693785563.1625649572) Following steps could help you: remove the defer attribute move the telerik script above other scripts empty browser cache have a nice day regards Matthias
