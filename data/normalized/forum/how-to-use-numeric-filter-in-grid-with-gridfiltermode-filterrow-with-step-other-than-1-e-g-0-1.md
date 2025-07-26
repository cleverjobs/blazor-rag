# How to use numeric filter in grid with GridFilterMode.FilterRow with step other than 1 (e.g. 0.1)?

## Question

**Kla** asked on 27 Apr 2021

In a grid with FilterMode=GridFilterMode.FilterRow the step size for the up/down controls of a numeric field is 1. How can I change this to 0.1 (like Step="0.1" in TelerikNumericTextBox)? Everything else (resetting filter, selecting filter operator,...) should work as in the standard implementation.

## Answer

**Marin Bratanov** answered on 27 Apr 2021

Hi Klaus, You can use the filter row template to define your own UI and UX (say, define a small Step, Min, Max or other settings) to a numeric textbox. You can find examples of doing something similar in its documentation article: [https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-row-template.](https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-row-template.) Regards, Marin Bratanov Progress Telerik

### Response

**Klaus** answered on 28 Apr 2021

Hi Marin, Thank you for your prompt reply. I managed to get the changed step size and the 'reset filter button' (A). It works like a charm. Is there also an example how to implement the 'select filter operator button' (B)? Regrads, Klaus

### Response

**Marin Bratanov** commented on 28 Apr 2021

You can use a dropdownlist, the following article shows how you can bind it to an enum: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-kb-bind-to-enum,](https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-kb-bind-to-enum,) The FilterOperators list is the collection you need, and you may want to filter it out according to the column type (for example, StartsWith or Contains filter is not suitable for a number).

### Response

**Klaus** commented on 28 Apr 2021

Binding an enum to a dropdownlist (like in your example) works fine. Now I'm looking for a (filter) button that opens the list, just like in your filter implementation - s.a. (B). I found your example for a split button. But in that example both controls (button and dropdownlist) are visible and pressing the button with the star icon does not open or close the list. Is there an example that matches the control(s) marked with (B)?

### Response

**Marin Bratanov** commented on 28 Apr 2021

I'm afraid we don't have exaclty such an example. You can use CSS to hide additional elements from the dropdown that you don't want, and you can override with CSS the icon from the current downarrow to the filter icon the grid uses out-of-the-box.

### Response

**Klaus** commented on 28 Apr 2021

Thank you for your support. As I did not manage to get the standard UI with step size 0.1, I changed my approach and used OnStateChanged to simualte a step size other than 1. It was a bit complicated but now that it's done it should be ok. Are there any plans to include something like a 'button with an attached menu' in your Blazor package in the future?

### Response

**Marin Bratanov** commented on 29 Apr 2021

Maybe through this: [https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning](https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning) - I don't know exactly how the API will look like but it should be more customizable than a dropdownlist. Something else you can consider is the context menu that you can show on any event (such as onclick): [https://docs.telerik.com/blazor-ui/components/contextmenu/integration](https://docs.telerik.com/blazor-ui/components/contextmenu/integration)
