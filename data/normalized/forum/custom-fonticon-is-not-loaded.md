# Custom FontIcon is not loaded

## Question

**BenBen** asked on 12 Oct 2023

Hi, I'm upgrading my Telerik version to 4.6.0 and when I want to use custom FontIcon the icon is not displayed. I see in the HTML that my icon content is defined the same in both situations. It work with the FontIcon.FilterClear but not with the custom: <TelerikButton Icon="@FontIcon.FilterClear"> Font Icon Button <TelerikButton /> <TelerikButton Icon="@(" k-icon k-i-filter-clear") "> Custon Font Icon Button <TelerikButton />

## Answer

**Dimo** answered on 13 Oct 2023

Hi Ben, Please refer to: Rendering changes in the icons in UI for Blazor 4.6.0 KB Article: Font Icons not rendering How Font Icons Work Regards, Dimo Progress Telerik
