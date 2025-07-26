# DropdownList Not opening when Filterable is Enabled

## Question

**TimTim** asked on 27 Jun 2022

Hi, I have an issue with some dropdown lists not opening when Filterable is enabled. This only occurs when displaying dropdowns in a modal popover when using Blazored Modal; [https://github.com/Blazored/Modal.](https://github.com/Blazored/Modal.) If Filterable is disabled, the dropdowns open. Every other component work fine, but the dropdown list. Does anyone know why this is happening?

## Answer

**Tsvetomir** answered on 30 Jun 2022

Hi Tim, Based on the provided information, I am not completely sure what might be preventing the DropDownList from rendering. I have created an example where a filterable DropDownList is inside a BlazoredWindow and it appears that the component is opened correctly. As a comparison, I added a TelerikWindow with Modal="true" for reference. Regards, Tsvetomir
