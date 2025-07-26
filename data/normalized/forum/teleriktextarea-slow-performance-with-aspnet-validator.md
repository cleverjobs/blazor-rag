# TelerikTextArea slow performance with Aspnet Validator

## Question

**Mat** asked on 01 Jul 2021

Hi, I have a Blazor WASM project that uses TelerikTextArea components in its pages, and I noticed it took a massive performance hit when we added a <DataAnnotationsValidator /> to the EditForms on these pages. To verify if this was just our project or not, I created a new Wasm Blazor app and added: A new Razor Component with an EditForm a class with 4 strings, 2 with [Required} annotations, set to be the model of the editform 4 TelerikTextAreas in the form for each of the strings in the model a <DataAnnotationsValidator /> Without the <DataAnnotationsValidator /> I did not see any performance issues filling out these textboxes, but with it added to the form there is an obvious stutter when typing in these textareas. If I increase the number of text areas the stutter gets worse, freezing up the page for 10-15 seconds at the worst. I cloned this Component and changed all of the TelerikTextAreas to InputTextAreas and the performance issues are gone. I recorded the performance of the page with the Chrome dev tools and noticed that Event: keypress Handler takes far longer to resolve than if the <DataAnnotationsValidator /> is removed or InputTextAreas are used. The stutter is mildly inconvenient on this test page I created, but in a larger existing component adding validation to the forms has rendered these Telerik components just about useless. Has anyone else encountered these serious performance issues?

## Answer

**Nadezhda Tacheva** answered on 05 Jul 2021

Hi Matthew, Indeed, this behavior is observed in Blazor WASM applications when you use a Telerik TextArea and a validation component such as DataAnnotationsValidator or ObjectGraphDataAnnotationsValidator. We currently have an opened bug report for that scenario in our public feedback portal - Possible TextArea performance issue related to validation components - DataAnnotationsValidator and ObjectGraphDataAnnotationsValidator. I have added a vote on your behalf to increase its popularity as we are prioritizing the bug fixes based on the community interest and demand. You can also click the Follow button to subscribe and receive email notifications when its status changes. This is the best way to keep in track with the progress of the bug fix as once we know which release will contain this fix, we will update its status in the feedback portal and you will be notified via email right away. The bug report is currently in our parking lot and by the time it is fixed a you can try one of the following workarounds: Avoid Validation When Typing and validate in the OnChange As we have chosen to fire validation with the ValueChanged event in order to achieve a more fluid user experience, you may also try changing the default behavior and use the OnChange event of the TextArea to fire validation. This will provide a better performance at this stage. An example for such a setup is available in this knowledge base article. It demonstrates the described approach with a TextBox, however, it is also applicable for a TextArea. We also have this feature request in our public portal - Inputs to Validate only in the OnChange event, not on every keystroke. In case you find it interesting and useful for your scenario, you can vote for it and subscribe to keep in track with its status. Use InputTextAreas Since you mentioned no performance hit is observed when using InputTextAreas, if you don't consider the above mentioned approach a good fit for your application, you may try switching Telerik TextAreas with InputTextAreas until the fix is available. I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva Progress Telerik

### Response

**Bob** commented on 11 Aug 2021

Hello, In my findings, this issue goes beyond TelerikTextAreas. I've seen unbearable performance issues with TelerikTextBox, TelerikMaskedTextBox and also TelerikDatePicker. At times it can take up to 30 seconds for a key press to be reflected on the page. This is after implementing the work around to validate OnChange rather than the default of key press. I have isolated the issue to validation. If I remove DataAnnotationsValidator and ValidationSummary from my page, the Telerik controls behave as expected. Also, If I use InputText and InputDate in combination with DataAnnotationsValidator and ValidationSummary, no performance issues. I checked the related bug for this issue and see it's "unplanned". Unfortunately this is a show stropper for us.

### Response

**Nadezhda Tacheva** commented on 16 Aug 2021

Hi Bob, Could you please send us an isolated runnable reproduction of the issue you are experiencing with the listed editors after implementing validation in the OnChange? Thus, we will be able to debug and find out what is causing it. Thank you in advance! I will be looking forward to receiving your response!

### Response

**Bob** commented on 20 Aug 2021

Hi Nadezhda, Thanks for the reply. If you've acknowledged the issue with TelerikTextArea, it should be easy for you to reproduce with TelerikTextBox, TelerikMaskedTextBox and also TelerikDatePicker. I've abandoned those Telerik controls and have had to find alternatives. If you can't reproduce and can point me towards the project used to reproduce the issue with TelerikTextArea, I could modify it for the other 3. Thanks. Bob

### Response

**Nadezhda Tacheva** commented on 24 Aug 2021

Hi Bob, Attached you will find a project that I used for testing of the Telerik inputs. Indeed, this behavior occurs when using MaskedTextBox and DatePickers. However, I was not able to reproduce it with the TextBox. You can try modifying the attached project to reproduce the issue you are experiencing with the TextBox and send it back to us for testing. In addition, I also tested how the Autocomplete and ComboBox components behave in such scenario since they also include inputs. However, they don't seem to be affected by the issue. For ease of access and testing in the example project I separated the different components in three pages - Text inputs, Date/Time inputs, Dropdowns. Regards, Nadezhda Tacheva
