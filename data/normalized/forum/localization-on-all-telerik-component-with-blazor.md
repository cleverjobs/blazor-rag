# Localization on all Telerik component with Blazor

## Question

**Gle** asked on 14 Mar 2024

I implemented the Localization on my project, and I got almost all of them. But the Column Menus and some drop downs aren't translating. How can I achieve that? Implementation Program.cs // register a custom localizer for the Telerik components, after registering the Telerik services
builder.Services.AddSingleton<ITelerikStringLocalizer, TelerikLocalizer>();
builder.Services.AddLocalization(); TelerikLocalizer.cs public class TelerikLocalizer : ITelerikStringLocalizer
{
private readonly IStringLocalizer <Resources> globalLocalizer;

public TelerikLocalizer(IStringLocalizer <Resources> globalLocalizer)
{
this.globalLocalizer=globalLocalizer;
}

public string this[string name]=> GetStringFromResource(name);

public string GetStringFromResource(string key)
{
var localString=Resources.ResourceManager.GetString(key, Resources.Culture);
if (string.IsNullOrWhiteSpace(localString))
{
return globalLocalizer.GetString(key);
}
return localString;
}
} I have a list of about 19 languages Source: [https://github.com/telerik/blazor-ui/tree/master/common/localization](https://github.com/telerik/blazor-ui/tree/master/common/localization)

## Answer

**Hristian Stefanov** answered on 19 Mar 2024

Hi Glendys, From the provided information, it seems that the reason for the problem is that the following keys are missing (or empty) from the.resx resource files because the sample you are referring to does not use a column menu: ColumnMenu_Apply ColumnMenu_ColumnMenu ColumnMenu_Columns ColumnMenu_GroupColumn ColumnMenu_Lock ColumnMenu_ReorderNext ColumnMenu_ReorderPrevious ColumnMenu_Reset ColumnMenu_SetColumnPosition ColumnMenu_SortAscending ColumnMenu_SortDescending ColumnMenu_UngroupColumn ColumnMenu_Unlock Therefore, ensure to add these keys to the.resx file of each language along with their corresponding translations. Additionally, for reference, there are two places to obtain localization files: The offline version of our demo site - is maintained by us and contains a limited number of localization files, just as an example of how to implement them. Unfortunately, we are not language experts, so the resx files contain all the localization keys, but we don't vouch that the translations are perfect. The blazor-ui-messages GitHub repository - is maintained by the community. There are more localization files at different levels of "up-to-date-ness", so some localization keys may be missing. Regards, Hristian Stefanov Progress Telerik
