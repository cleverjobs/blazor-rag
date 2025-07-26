# Sass Theme Builder

## Question

**Mat** asked on 28 Jun 2021

Hi is the only possibility to import my theme in Sass Theme Builder a json-file? Up to the last version I used the scss-variables. Or do i miss something? Thank you!

### Response

**Matthias** commented on 28 Jun 2021

documentation still expects a sass file: [https://docs.telerik.com/blazor-ui/themes/custom-theme#import-custom-theme](https://docs.telerik.com/blazor-ui/themes/custom-theme#import-custom-theme)

## Answer

**Dimo** answered on 29 Jun 2021

Hello Matthias, Indeed, the Theme Builder now requires a JSON file import. The documentation update will go live soon, together with a new Knowledge Base article. It explains how to create the JSON file from the SCSS file that you have. You can preview all the information immediately in the docs site GitHub source: [https://github.com/telerik/blazor-docs/blob/master/knowledge-base/common-themebuilder-json-from-scss.md](https://github.com/telerik/blazor-docs/blob/master/knowledge-base/common-themebuilder-json-from-scss.md) EDIT: The article is now live: [https://docs.telerik.com/blazor-ui/knowledge-base/common-themebuilder-json-from-scss](https://docs.telerik.com/blazor-ui/knowledge-base/common-themebuilder-json-from-scss) Regards, Dimo

### Response

**Matthias** commented on 29 Jun 2021

Thank you for the information. I already did/tried this. But the older SASS file is different - For example I have the attribute $accent, which I can't find in the json file. It would be great, to have a "mapping" between the attributes. I do not know - for example -how to assign "$accent" color ... so it is trial and error to figure out which attribute should be assigned to the old values. Will this be included in the documentation? I'm pretty sure a lot of developers will save time... thank you

### Response

**Dimo** commented on 29 Jun 2021

$accent has been deprecated in favor of $primary: [https://github.com/telerik/kendo-themes/blob/develop/packages/default/docs/customization-color-system.md](https://github.com/telerik/kendo-themes/blob/develop/packages/default/docs/customization-color-system.md) If your custom theme is a few product versions old, it may be best to recreate it from scratch. The ThemeBuilder is compatible with the latest themes.

### Response

**Matthias** commented on 29 Jun 2021

Ah ok - this helps me I will create a new theme as soon I will have the time for this Thanks
