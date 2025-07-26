# Assigning an ID to a dropdownlist results in an exception

## Question

**Edw** asked on 05 Feb 2020

If I add an ID attribute to a dropdownlist, I get the following exception: Object of type 'Telerik.Blazor.Components.TelerikDropDownList`2[[<name-of-my-object>],[System.String, System.Private.CoreLib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]' has a property matching the name 'ID', but it does not have [ParameterAttribute] or [CascadingParameterAttribute] applied. Is it because the object that serves as "TModel" has a property named Id? The reason I need an Id to begin with, is so that I can manipulate the value from javascript. Help on doing that would be great!

## Answer

**Marin Bratanov** answered on 06 Feb 2020

Hi Edward, The error indicates that the Telerik component does not have a parameter called ID, which is, indeed, the case. We are working on adding that parameter to all input type components so you can add it to them, and it would render as the id attribute on their <input> DOM elements. In the meantime, you can wrap the component in a label, something like that: <label> label text <TelerikDropDownList /> </label> You can also Vote for and Follow the implementation of a built-in Label like the one of the textbox component here: [https://feedback.telerik.com/blazor/1447949-be-able-to-add-a-label-to-all-components-datepicker-datetimepicker](https://feedback.telerik.com/blazor/1447949-be-able-to-add-a-label-to-all-components-datepicker-datetimepicker) On a side note - I strongly advise that you do not modify the DOM of the components with JavaScript. This is not the Blazor way of interacting with components and can result in errors, wrong behavior, or simply can get wiped by a re-render. If you need to alter something in a component, you should use razor syntax. If you will be doing things with JS, you should avoid touching the same portion of the page with both razor and js. For example, if you have some JS functionality that needs to set the value of the dropdownlist, you should use the JS Interop to call a C# method that will alter the view-model accordingly. Regards, Marin Bratanov
