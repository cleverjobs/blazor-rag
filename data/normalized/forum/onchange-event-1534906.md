# OnChange Event

## Question

**BobBob** asked on 09 Sep 2021

Is there any way to have the OnChange event get called when they click enter but NOT when the textbox loses focus? My textbox is in a modal and it performs a data search when Enter is clicked in the textbox, but the problem is when I click the Cancel button in my modal window it fires the event if I am still focussed on the textbox and it interferes with the closing of the modal.

## Answer

**Marin Bratanov** answered on 09 Sep 2021

Hello Bob, You can capture the Enter key as shown here: [https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events](https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events) Regards, Marin Bratanov
