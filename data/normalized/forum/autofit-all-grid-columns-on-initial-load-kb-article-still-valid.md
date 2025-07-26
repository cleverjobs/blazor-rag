# Autofit all Grid columns on initial load kb article still valid?

## Question

**Mar** asked on 29 Jul 2022

Hi: Is the approached discussed in the kb article Autofit all Grid columns on initial load still valid given that the Blazor controls are on version 3.4.0 and .NET 5+ supports JavaScript Isolation? Thanks -marc

## Answer

**Dimo** answered on 03 Aug 2022

Hello Marc, Yes, the approach is still valid. The KB article basically shows how to use a MutationObserver to detect when a specific Grid has populated and it HTML markup has changed. We do not require specific architecture with regard to the JavaScript code, so you are free to change it if you like. Regards, Dimo Progress Telerik
