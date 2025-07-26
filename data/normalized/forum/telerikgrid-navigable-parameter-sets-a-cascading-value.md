# TelerikGrid Navigable parameter sets a cascading value

## Question

**Joh** asked on 12 Sep 2022

Updating Telerik UI for Blazor to 3.5 introduced an issue for us where a CascadingParameter was being set unintentionally. We found that setting the Navigable parameter on a TelerikGrid to true is being cascaded to our parameter. REPL demonstrating the issue: Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor. Note that the switch in the grid toolbar is disabled only when the Navigable parameter is set to true. Is this a bug or something that needs to be taken into consideration when using grids now?

## Answer

**Dimo** answered on 13 Sep 2022

Hi John, Use named cascading parameters to have better control over your app. Regards, Dimo
