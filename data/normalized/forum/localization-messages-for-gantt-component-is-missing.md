# Localization messages for Gantt component is missing

## Question

**Iva** asked on 09 Nov 2021

By default anything is ok But with enable localization all lables is empty The TelerikMessages resource file does not contain pointers to the properties of the Gantt component, and has not been updated in over a year!!

## Answer

**Dimo** answered on 11 Nov 2021

Hi Ivan, Where do you take the localization file from? The most up-to-date one is located in the offline demo site that is included in the UI for Blazor installer. On the other hand, the blazor-ui-messages repo is maintained by the community. The blazor-ui localization examples focus on the configuration itself. Regards, Dimo

### Response

**Ivan** answered on 12 Nov 2021

I have searched in the GitHub repository [https://github.com/telerik/blazor-ui-messages/tree/main/Messages](https://github.com/telerik/blazor-ui-messages/tree/main/Messages) [https://github.com/telerik/blazor-ui/tree/master/common/localization/ServerLocalizationResx/Resources](https://github.com/telerik/blazor-ui/tree/master/common/localization/ServerLocalizationResx/Resources) Thanks for the hint, found in local examples. Without a hint, this information is not obvious.

### Response

**Ivan** answered on 22 Oct 2022

Hello! How to localize the follow tooltip (showing while drag task on timeline) Need to localize "Start" and "End" words did not find matching properties in the resource file and is it possible to redefine the template of this tooltip?

### Response

**Dimo** commented on 24 Oct 2022

Hi Ivan, The localization properties are Gantt_Editor_Start and Gantt_Editor_End. Currently they apply for the Gantt edit form, but will also start working for the Gantt tooltip in version 3.7, which is due in November.

### Response

**Ivan** commented on 23 Nov 2022

Hi Dimo! In version 3.7 this localization messages still not applying for timeline's dragging tooltip

### Response

**Dimo** commented on 23 Nov 2022

Oops. Yes, we fixed the main task tooltip, but missed the resizer tooltip. This is now OK as well and changes will take effect in 3.8.0 in two weeks. Sorry about that.
