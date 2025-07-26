# Set UI Focus in Net5.0

## Question

**Gra** asked on 02 Dec 2020

Will Telerik Blazor components support this new functionality in the future? [https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.elementreferenceextensions.focusasync?view=aspnetcore-5.0#Microsoft_AspNetCore_Components_ElementReferenceExtensions_FocusAsync_Microsoft_AspNetCore_Components_ElementReference_](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.elementreferenceextensions.focusasync?view=aspnetcore-5.0#Microsoft_AspNetCore_Components_ElementReferenceExtensions_FocusAsync_Microsoft_AspNetCore_Components_ElementReference_) Set UI focus in Blazor apps Blazor now has a FocusAsync convenience method on ElementReference for setting the UI focus on that element. <button @onclick="()=> textInput.FocusAsync()">Set focus</button><input @ref="textInput"/>

## Answer

**Svetoslav Dimitrov** answered on 04 Dec 2020

Hello Graham, The main difference between the references to our components and the default ElementReference that comes from the framework is that ours are classes, whereas the ElementReference is a struct. The class cannot inherit a struct and that is the reason why ours do not support the FocusAsync method of the ElementReference straight away. Another reason why we do not currently support this is that not all of our components are focusable by default, for example, the Grid container is not focusable, so its reference should not support this feature (the grid cells are, but not the main container). There is no defined list of focusable HTML elements, but I could offer a list of elements that are known to be. Focusable elements HTMLInputElement (comparable to all our inputs - TextBox, NumericTextBox, DateInput, etc.) HTMLSelectElement (comparable to the DropDownList) HTMLTextAreElement (comparable to the TextArea component) HTMLAnchorElement - focusable if they have a href or tabindex attributes HTMLButtonElement (comparable to the TelerikButton) HTMLAreaElement - focusable if it has the tabindex attribute That being said, I have opened a new Feature Request on our public Feedback Portal, which you could see from this link. I have added your Vote for it, and since I opened it on your behalf you are automatically subscribed for email notification on status updates. Regards, Svetoslav Dimitrov
