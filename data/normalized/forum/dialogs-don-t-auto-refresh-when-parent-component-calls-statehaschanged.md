# Dialogs don't auto refresh when parent component calls StateHasChanged

## Question

**Pin** asked on 20 Dec 2021

So, I have a TelerikDialog inside a parent component. The dialog title and content have data that may change. When this data should change, I call StateHasChanged() in the parent, but nothing updates. Stepping through the code shows that the values themselves have changed, but no content changes in the browser. I noticed that TelerikDialog's have a Refresh method you can call, and calling this instead of calling StateHasChanged in the parent does bring in the changes, so its a solved problem... However I wanted to ask why this is? Am I going mad, or would calling StateHasChanged usually work when calling from the parent like that? (Imagine passing in a string variable inside a H4 tag as the dialog title, changing the string variable and calling StateHasChanged). If that would normally work, I am interested in why we need to call Refresh instead in this instance, what was done to cause this and for what reason? (Its plain curiosity, not an problem or issue at all). As an example to illustrate, I created a simple repl with 2 dialogs. Each contains a button which will change the title, but the method to change the title attempts to update in different ways. The first calls StateHasChanged (which I thought at first would work), whereas the second calls Refresh on the Dialog ref, which is what does work. The repl can be found here: [https://blazorrepl.telerik.com/cvlmwuOR02RX8uFh46](https://blazorrepl.telerik.com/cvlmwuOR02RX8uFh46) Thanks.

## Answer

**Apostolos** answered on 21 Dec 2021

Hi Matthew, StateHasChanged() re-renders the current Razor component only. In this specific case, the Dialog is rendered as a child of the TelerikRootComponent (which normally resides in the MainLayout ). This ensures correct Dialog positioning on the page, and over all the other content. This is why StateHasChanged does not update the Dialog content. Actually, all our popups have the same behavior, thus we will expose a Refresh method for other components for such scenarios. I hope the provided information is sufficient. Regards, Apostolos

### Response

**Pingu** commented on 21 Dec 2021

Ahh that makes total sense. Wasn't imagining that it rendered outside of the parent component like that, but makes sense now. Thanks. :)
