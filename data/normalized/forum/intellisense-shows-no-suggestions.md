# Intellisense shows "No Suggestions"

## Question

**Ste** asked on 18 Jun 2020

I installed UI for Blazor into an existing Blazor Server project. I have confirmed that the Telerik control for Blazor are functioning with my pages. However, when using the controls on a Razor page I am not getting any Intellisense suggestions. If I do CTRL + Space Intellisense displays "No Suggestions". Have I missed a setup step or something? Thanks.

## Answer

**Marin Bratanov** answered on 18 Jun 2020

Hi Steve, There is no extra step needed to get intellisense running - it should happen automatically and Visual Studio should take care of it for you - none of us really has control over that. Maybe a restart/update/repair on VS will help too. What else I can suggest you look into is: make sure that the components are used in a Razor Component (.razor file) and not a Razor Page (.cshtml file) check if enabling/reinstalling/installing/removing the "Visual Studio IntelliCode" extension makes a difference as it has to do with intellisense check if disabling other intellisense related tools (such as ReSharper maybe) makes a difference Regards, Marin Bratanov

### Response

**Steve** answered on 18 Jun 2020

Double checked usage per your suggestions and restarted Visual Studio 2019. Intellisense showed up after the restart. Thanks.

### Response

**Marin Bratanov** answered on 18 Jun 2020

Great! Regards, Marin Bratanov
