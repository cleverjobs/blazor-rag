# Is ThemeBuilder CSS up to date with new UI for Blazor 3.0.0?

## Question

**Ada** asked on 19 Jan 2022

Hi I have just updated an application to UI for Blazor 3.0.0 - upgraded the nuget packages fine. I then used the ThemeBuilder to update my css - but when i run the application is looks like there are issues with the CSS e.g. unstyled input boxes etc. If i use href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" then things look right again, however they are not to my custom theme - are the ThemeBuilder outputs not up to date with the new release?

## Answer

**Dimo** answered on 20 Jan 2022

Hello Adam, Indeed, the ThemeBuilder currently produces themes for 2.30. We are fixing some last-minute issues and ideally, we will update it in the following hours. Please excuse us about this delay. Regards, Dimo

### Response

**Adam** commented on 23 Jan 2022

Thanks Dimo - it doesn't look like this has been sorted yet. Any update on timescales?

### Response

**Dimo** commented on 24 Jan 2022

Hi Adam, the ThemeBuilder update is now live. We recommend clearing the browser cache when running it.

### Response

**Adam** commented on 25 Jan 2022

Thanks Dimo - working fine now

### Response

**Wim** answered on 25 Jan 2022

Hello I minify the css file of the ThemeBuilder, but that gives errors. Is there still something wrong with the file? Error 0: Unexpected token, found ';' (1, 13935) Error 0: Expected expression, found ';' (1, 13935) Error 0: Unexpected token, found ';' (1, 13939) Error 0: Expected expression, found ';' (1, 13939)

### Response

**Dimo** commented on 26 Jan 2022

Hi Wim, The new ThemeBuilder version is live, so this must be a different issue. I did some research and suggest you the following: See if your custom theme contains the following CSS code: .k-input-spinner.k-spinner-increase.k-icon { bottom: -; }.k-input-spinner.k-spinner-decrease.k-icon { top: -; } If you find such code, replace "-" with "auto" and try using the CSS file again. If there is no such code, or if the change does not fix the problem, then validate the CSS file and fix any parse errors that the validator reports. For example, change or remove any offending style values. You can ignore complaints about aspect-ratio: 1 - this should not be an issue. Let me know what you found out, so that I can log a bug report if necessary. If none of the above helps, please open a new forum thread and attach your custom theme ZIP there.

### Response

**Wim** commented on 26 Jan 2022

Thanks Dimo, it did contain the css from your previous comment. After replacing "-" with the "auto" value the minification works.

### Response

**Dimo** commented on 26 Jan 2022

Good, here is the pull request for the fix on our side. Thanks for your cooperation!
