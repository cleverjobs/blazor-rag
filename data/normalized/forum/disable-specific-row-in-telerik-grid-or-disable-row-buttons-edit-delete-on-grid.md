# Disable specific row in Telerik grid (or) Disable row buttons (Edit & Delete) on grid

## Question

**Lak** asked on 06 Jul 2021

Hi, I wanted to disable the particular row in Telerik grid (or) disable the particular row buttons on grid. Please help me out ASAP. Thank you, LakshmiPathi K

## Answer

**Matthias** answered on 06 Jul 2021

just style the css for the cmd-btn code (example!): <GridCommandButton Command="Delete" Icon="delete" Class="cmdBtnNoClick">&nbsp;</GridCommandButton> style: .cmdBtnNoClick { pointer-events: none; cursor: not-allowed; } depending on what you want, change the class for example to .cmdAllowClick{ ...... }
