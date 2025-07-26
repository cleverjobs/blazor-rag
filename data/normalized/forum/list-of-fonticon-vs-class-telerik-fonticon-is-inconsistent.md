# List of FontIcon vs class Telerik.FontIcon is inconsistent

## Question

**Pet** asked on 15 Jun 2023

I have written a small application where our service employees can set icons themselves. I thought it would be quite simple: Here is a list of the icons I found on Teleriks Site: [https://www.telerik.com/design-system/docs/foundation/iconography/icon-list/](https://www.telerik.com/design-system/docs/foundation/iconography/icon-list/) And I have written a guide on how to convert the names to camel case so that ...Enum.TryParse(typeof(FontIcon), function.FontIcon, out font_icon); works. In function.FontIcon, the corresponding string is stored. And now a message came back saying: non-recurrence -> NonRecurrence is not being displayed. I have checked and indeed, it is not present in the Telerik.FontIcon class. Is there another source that could be referenced where the icon representation and the text are consistent? Yes I could write a small Page to create a list of all components. But I think it is worth mentioning this issue here. :-) Maybe you could fix the page on the documentation. I ran in this "problem" using ContextMenuItem

## Answer

**Radko** answered on 16 Jun 2023

Hi Peter, The provided list from our Design System website should be up to date and all icons are expected to render correctly. However, please note said list refers to the latest state of the product, meaning if you are to use an older version, you might have to upgrade to get all available icons. The NonRecurrence icon in particular, has been added rather recently, and is expected to work with version 4.3.0 (latest) and beyond. Here is a REPL link where it can be seen: [https://blazorrepl.telerik.com/wdaAlqFK52fv93A534.](https://blazorrepl.telerik.com/wdaAlqFK52fv93A534.) Not sure if it would be of any help for your application, but the source code of the packages containing the meta data of the icons is public, and this exact enumeration is available here: [https://github.com/telerik/kendo-icons/blob/develop/packages/font-icons/src-cs/Telerik.FontIcons/Icons/FontIcon.cs](https://github.com/telerik/kendo-icons/blob/develop/packages/font-icons/src-cs/Telerik.FontIcons/Icons/FontIcon.cs) Regards, Radko

### Response

**Peter** commented on 16 Jun 2023

Ah, OK, that's the explanation. Sometimes a information which version is targeted by your good documentation were helpful. :-) In a project, you can't change the version of a Lib without permission of your boss. And so all links to the telerik documentation changed and you need to access the "old" Version, which is compatible with your used lib. e.g. like MS does it with their docs. Maybe an idea for an improvement. (I know we all hate to administer documentation) :-) Just kidding. Thanks for the response, please close this ticket. BTW: maybe someone has the needs a list of all icons: @page "/Helper/Fonts" <div> <h1>l ist of all icons </h1> @foreach (var icon in Enum.GetValues(typeof(Telerik.FontIcons.FontIcon)))
{ <p> <TelerikButton Icon="@icon" Size="lg"> @icon.ToString() </TelerikButton> @icon.ToString() <TelerikFontIcon Icon=@((Telerik.FontIcons.FontIcon)icon) Size="lg"> </TelerikFontIcon> </p> } </div> A dirty page with all icons available.

### Response

**Radko** answered on 18 Jun 2023

Hi Peter, Thanks so much for the feedback and I am glad this is now resolved. In regards to having documentation versioning - this is actually something that has been brought up before and is certainly something we are looking into. Regards, Radko
