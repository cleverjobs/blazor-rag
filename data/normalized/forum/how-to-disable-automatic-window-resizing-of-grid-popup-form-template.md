# How to disable automatic window resizing of Grid Popup Form Template

## Question

**Val** asked on 16 Jun 2023

How to disable window resizing (by default, the Window is resizable) of Popup Form Template (GridPopupEditSettings) (similar to the Resizable="false" property for the TelerikWindow component). [https://demos.telerik.com/blazor-ui/grid/popup-edit-form-template](https://demos.telerik.com/blazor-ui/grid/popup-edit-form-template) Thank you for the help.

## Answer

**Radko** answered on 19 Jun 2023

Hi Valeriy, Currently there is no built-in way to control most individual Window parameters. However, you can disable the resizing through CSS, with a selector similar to the following: <style>.popup-class.k-resize-handle { pointer-events: none;
}
</style> Note in the above CSS rule, the.popup-class is taken from the linked example - a different setup might require a different rule. Regards, Radko

### Response

**Valeriy** commented on 19 Jun 2023

Thanks for the answer.
