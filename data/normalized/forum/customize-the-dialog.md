# Customize the dialog

## Question

**Dav** asked on 30 Mar 2021

How can we customize the dialogs? Specifically the color of the buttons and the text of the buttons in the confirmation dialog.

## Answer

**Matthias** answered on 06 Apr 2021

you can see all in the developer-tools of your browser. for example: .k-dialog{ min-height: 200x!important; color: black; background-image: none; } .k-dialog .k-window-content { min-height: 100px; margin: 5px; } .k-dialog-buttongroup .k-button { margin: 0px; background-image: none; background-color: var(--parat-bg-color)!important; color: white!important; font-size: 12px; border: 1px solid white; }

### Response

**Matthias** answered on 06 Apr 2021

and... to change the text of the button, go to [https://docs.telerik.com/blazor-ui/globalization/localization](https://docs.telerik.com/blazor-ui/globalization/localization)
