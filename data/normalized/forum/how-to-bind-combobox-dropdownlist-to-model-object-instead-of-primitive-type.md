# How to bind ComboBox/DropDownList to model (object) instead of primitive type

## Question

**Dou** asked on 27 Apr 2021

The combo box data binding documentation discusses the ability to bind to a model, however in the example the bind-Value is set to an integer property. If I set the bind-Value to a property that is an object type I get an invalid cast exception. Is there a way to bind such that the selected value is an object instead of a primitive type? I know I can use a primitive type as the selected value and then fetch the object out of the list in my view model but it would be cleaner to bind directly to the object itself.

## Answer

**Hristian Stefanov** answered on 29 Apr 2021

Hi Doug, The ComboBox/DropDownList provides a primitive Value so that the validation can work, and so that other data source operations (such as filtering) can work. The Value and Text cannot be classes (models) because that would prevent validation from working, and filtering/comparing entire classes is an operation that is not defined. Your way is the best and the easiest possible to achieve the desired result. Using the unique identifier provided from the component (the Value) and fetching the selected object out of the list. You can find examples of doing that in the following article: Get model from dropodwn Regards, Hristian Stefanov

### Response

**Doug** commented on 11 Oct 2021

Hristian, I might suggest you take a look at Chris Sainty's Blazored Typeahead control. It allows @bind-Value to be a non-primitive type and yet validation still works. It works a little differently than the Telerik drop down controls but to me it's more intuitive so I just want to throw it out there as food for thought. [https://github.com/Blazored/Typeahead](https://github.com/Blazored/Typeahead)

### Response

**Hristian Stefanov** commented on 14 Oct 2021

Hi Doug, Thank you for sharing with us your thoughts on this case. We highly value the feedback we receive for the behavior of our components. Regards, Hristian Stefanov Progress Telerik
