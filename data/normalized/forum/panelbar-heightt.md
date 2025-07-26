# PanelBar Heightt

## Question

**Pau** asked on 03 Feb 2022

Is it possible to set the height of the TelerikPanelBar in UI for Blazor? Specifically, I would like to have the "Header" items always visible and the "Content" items scroll if needed. Not seeing a way to do this.

## Answer

**Matthias** answered on 04 Feb 2022

Hi Paul, I'm not quite sure if this is what you mean - test it out. You might have to adjust it a bit. But maybe there is a good "starting point" .k-content { height: 100px;
}.k-state-selected { height: 80px;
}.k-panelbar-content { overflow: auto;
}.k-link { height: 80px;
} regards Matthias

### Response

**Paul** commented on 07 Feb 2022

Matthias, Thanks. That got me going in the right direction. Couple tweaks and it should look like I want.
