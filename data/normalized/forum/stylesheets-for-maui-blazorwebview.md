# Stylesheets for MAUI BlazorWebView

## Question

**Mat** asked on 19 Feb 2024

Hi, since jQuery has Telerik styles via SASS, is it SASS also available for Blazor? If so, is there direct support for XAML mixins and syntax changes for MAUI clients? Since we want to build Razor pages and WASM for MAUI client with existing Telerik theme which would make consistent appearance within existing jQuery applications ... Kind regards.

## Answer

**Svetoslav Dimitrov** answered on 21 Feb 2024

Hello Matěj, The themes for Telerik UI for Blazor are also based on SASS and are the same as in Kendo jQuery, admittedly we have fewer themes. Regarding the XAML mixins, I should say that I am not aware of this concept, however, if it is supported in SASS we must support it as well. If you use the same theme in Blazor and jQuery the look of the components must be consistent. On the topic of syntax changes, I believe that you would like to customize the built-in themes to exactly match your business needs. If you want to to compile themes from their source code, then refer to: Themes Documentation in the Telerik Design System (linked from the repo wiki ) Compiling Themes at repo wiki - to get a better understanding, check all pages in the wiki's right column. The packages / [theme name] / docs folder for each theme in the repo, for example here is the one for the Default theme Out of curiosity can you point me to a resource where I can get acquainted with the concept of XAML mixins? Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Matěj** commented on 21 Feb 2024

Well I've read, that it is possible to use the same CSS of SASS for WinUI, just that it needs to adapt to XAML scheme - where some attributes are the same, but some need specified changes. I do not remember for the moment, but differences are like there is no border-left style, but thickness instead. That is what I am asking for - MAUI support of SASS. But since you answered well to me, making WinUI mixins would be somewhat easy since there are direct SASS styles for Blazor from Telerik. Kind regards!
