# Blazor Grid - Hide group footer when group is collapsed

## Question

**DanDan** asked on 20 Apr 2022

is there a way to hide a group footer when the group is collapsed?

## Answer

**Joana** answered on 25 Apr 2022

Hello Dan, I have logged a feature request on your behalf to be able to configure the footer visibility. You can track the progress of the request below: [https://feedback.telerik.com/blazor/1562710](https://feedback.telerik.com/blazor/1562710) Currently, there is no sustainable workaround to hide the group footer because of the need of hacks to understand which group row element is expanded and which footer to hide. Moreover, we rely on the row indices for the keyboard navigation and the navigation would be affected if we hide rows with css. Regards, Joana Progress Telerik
