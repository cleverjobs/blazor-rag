# Requesting old themes color palette files (scss or .json)

## Question

**Bla** asked on 12 Nov 2021

Will there be a possibility to get the .scss or .json files with the color palette of the old themes like Vintage, Metro, Urban, Moonlight, Office 365, Powder Blue, Uniform and others? Since they are not available in the new Sass Builder, my idea is to rearm them. It would be great not to have to do it from scratch. I guess you must have that info available somewhere. Regards.

## Answer

**Dimo** answered on 17 Nov 2021

Hi Blazorist, We intend to provide JSON files for the legacy LESS themes by early 2022. They will be compatible with the SASS ThemeBuilder. In the meantime, all color values for the LESS themes are available in the kendo-ui-core public repo. Look inside the kendo.[theme_name].less files. The variable structure is a bit different, but you will be able to obtain the colors and use them to create a custom SASS theme. Regards, Dimo Progress Telerik

### Response

**Eric** commented on 04 Jun 2022

is this still on the list to be delivered?

### Response

**Dimo** commented on 06 Jun 2022

@Eric - yes, see [https://github.com/telerik/kendo-themes/tree/develop/packages/classic/lib/swatches](https://github.com/telerik/kendo-themes/tree/develop/packages/classic/lib/swatches) or [https://unpkg.com/browse/@progress/kendo-theme-classic@5.4.1/lib/swatches/](https://unpkg.com/browse/@progress/kendo-theme-classic@5.4.1/lib/swatches/) The same links work if you replace "classic" with "default", "bootstrap" and "material". I expect more JSON files and documentation to be added for the Kendo/MVC/Core R3 release in September. Keep in mind that the LESS themes were never shipped with UI for Blazor. So the documentation on how to migrate from LESS to SASS themes will only be added for the products, which need it. Also check the LESS to SASS theme mappings.

### Response

**Blazorist** answered on 22 Nov 2021

That enough for me. I'll take a look to the values of the variables in order to regenerate the old legacy themes. Thank you very much DImo. Blazorist.
