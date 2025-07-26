# Loader : unable to find a reference for ThemeConstants

## Question

**Joh** asked on 04 Feb 2022

Hi, While developing my app, I have a grid and I'd like to run the TelerikLoader while loading page or data... I follow the example (I.E: [https://demos.telerik.com/blazor-ui/grid/loading-animation](https://demos.telerik.com/blazor-ui/grid/loading-animation) ) but when I add the code, the VS2002 compiler says: "The name 'ThemeConstants' does not exist in the current context " I try to add the full namespace: Telerik.Blazor.ThemeConstants and it's still the same.... does anyone has a clue.

### Response

**Matthias** commented on 04 Feb 2022

Hi John, this is too little information. Try this first: Create a new project with the desired behavior and test it. If the error still occurs, post it here and I can take a look.

## Answer

**Dimo** answered on 08 Feb 2022

John - Upgrade to version 3.0 or use the old LoaderSize enum for Size. See the before/after example in the Breaking Changes article. Regards, Dimo Progress Telerik
