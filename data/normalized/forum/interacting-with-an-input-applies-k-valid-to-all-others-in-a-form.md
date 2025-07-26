# Interacting with an input applies k-valid to all others in a form

## Question

**Mik** asked on 22 Mar 2024

I just updated our .NET 8 Blazor webapp from Telerik 5.0.1 to 5.1.1. Now, interacting with any input in a form applies validation classes to all other inputs in the form. I hope this behavior is unintentional as it could lead to user confusion. I believe this was introduced in the 5.0.1 update which was supposed to fix the issue of validation classes being present on initial render. I could find no other documentation or discussion regarding this. This behavior can be seen in the Form - Validation demo... Blazor Form Demos - Validation | Telerik UI for Blazor Type valid input in the Graduate Grade field and all other fields turn green even though they don't have valid input... Clicking Submit to show that those fields are not valid.

## Answer

**Hristian Stefanov** answered on 25 Mar 2024

Hi Mike, Thank you for the provided screenshot and the detailed explanation of the behavior you are experiencing. I confirm that our components automatically inherit the green border feature due to one of the latest updates in our themes. After a recent discussion with the team responsible for the themes, I can confirm that this feature will be reverted to obtain the proper behavior and will be addressed in the next official release. In the meantime, to override the green color in the form, add the following CSS: <style>.k-input-solid.k-valid,.k-picker-solid.k-valid { border-color: rgba ( 0, 0, 0, 0.08 );
} </style> Let me know if you are facing difficulties with the provided CSS solution. Regards, Hristian Stefanov Progress Telerik

### Response

**Mike** commented on 25 Mar 2024

Thank you for the information. It seemed there was no way to prevent .k-valid being applied so I used a similar CSS fix.

### Response

**Stuart** commented on 25 Jun 2024

Hi Support, I had the same issue after upgrading to 6.0.2 it no longer has the green border for invalid components but also doesn't have the green border for valid components (as expected from above). I was wondering why the k-valid class is added to unvalidated components and if a fix to only add k-valid or k-invalid to the component that changed would be better solution than removing the green border css. No green is better than broken green though :)

### Response

**Hristian Stefanov** commented on 25 Jun 2024

Hi Stuart, I confirm that previously, the green border appeared only for valid inputs. However, after evaluation, and considering feedback, we removed the green border in the latest versions as it seemed unnecessary for most customers. Currently, we add the "k-valid" class to valid inputs and "k-invalid" to invalid ones, with no green border applied. For your reference, here is our demo: REPL link. That said, I’m not entirely sure what you mean by saying " why the k-valid class is added to unvalidated components " and " No green is better than broken green " as this doesn’t seem to match the current behavior. Could you please clarify the specific issue you are encountering? I eagerly anticipate hearing back from you. Kind Regards, Hristian

### Response

**Stuart** commented on 26 Jun 2024

Hi Hristian, So in 5.1.1 when you edit any field all fields in the form now have a green border applied (no border on initial load) even though there are fields that don't meet their validations (it appears they have not yet been validated). This would cause considerable confusion as to why the form said it was good but then on submit it failed. In 6.0.2 this is hidden by the fact that there is no longer a green border but the k-valid class is still being added to each element. My guess is that there is a css provider added that checks if the field has an error message (which it won't until the field has been validated) and adds either valid or invalid based on this check. It should check if the field has been modified before checking the fields validity. If k-valid is only added to fields that have been validated you coiuld re-add the green border and it will only add the border as you change the fields or submit the form. I was able to reproduce the issue in your REPL link the steps to reproduce are: Run the solution Inspect fields to see classes Observe the wrappper spans have multiple classes but k-valid and k-invalid is not one of them Edit any field (e.g. name field) Inspect fields and see all fields span wrappers now all have k-valid class added Submit form most fields fail validation and go red I also have an issue that is still present in 6.0.2 that appears linked to this. One of my fields is programitically changed when a different field is changed (i.e. based on dropdown A's value dropdown B's list is generated and first element selected). If I submit the form it validates all fields and both are invalid. Then I set field A which validates as valid but field B while now valid is still showing as invalid until I change that field manually to something else or submit the form again. Note I am using fluentValidations for validations. Steps to reproduce: Have a form with 2 fields where when 1 is changed the other is programatically changed to first value in the dataset and has a validation that it requires a value Submit the form Observe both fields invalid Set the field A to a value Observe field A is now valid Observe field B is changed programatically Observe field B is still marked as invalid Change field Bs value or submit from Observe field B is not valid

### Response

**Hristian Stefanov** commented on 28 Jun 2024

Hi Stuart, I'm still in the process of reviewing the provided feedback as it taking me a little more time than expected. I will get back to you very shortly with an update. Your patience is highly valued. Kind Regards, Hristian

### Response

**Stuart** commented on 30 Jun 2024

Hi Hristian, No problem, thank you for the update :)

### Response

**Hristian Stefanov** commented on 03 Jul 2024

Hi Stuart, Thank you for your continued patience. I discussed the topic with our development team and I'm ready to provide an update. Upon reviewing our conversation, I realized my initial response regarding the "k-valid" and "k-invalid" classes wasn't entirely accurate. Let me clarify. The "k-valid" and "k-invalid" classes have been part of our component styling for a long time. At one point, an update to the themes caused components with the "k-valid" class to inherit a green border. This wasn't intentional, so we removed it. Our UX design team is considering adding a green border in the future, but its purpose will be to explicitly confirm specific field requirements, such as password strength or credit card validity, rather than indicating that all fields are valid. In general, these CSS classes are meant for styling and component HTML, not for validating input states. If these classes are causing any specific issues, please let me know, and I will share your use case with our team. Kind Regards, Hristian

### Response

**Stuart** commented on 03 Jul 2024

Hi Hristian, Thank you for looking into this for me, the k-invalid is used to style the field with a red border. The k-invalid is as far as I can see directly linked to the fields validation (e.g. on validation if invalid error message shown and class k-invlaid is added). I would assume that the k-valid class was the other side of this where on validation if there are no validation error it would be added otherwise it wouldn't have k-valid or k-invalid. E.g. if I don't have validation on the form the fields never get a k-valid or k-invalid class when the inputs change. If only the vields that have been validated got the k-valid / k-invalid you green border would have been working as I see it correctly. I can accept that valid fields look the same and unvalidated fields but it feels like this is hiding the fact that the k-valid class is added when it shouldn't be. Updating the logic to only add k-valid to validated fields would mean you could add the green border back. My big issue though is my second point that programatically changed fields are not re-validated. This causes an issue where if I submit the form and the programtically changed field is invalid it goes red, then when that field is programitically changed even though it is now valid it is still showing the error message and red border. If you could look into this updating the logic that fields changed in code get revalidated that would be greatly appreciated.

### Response

**Radko** commented on 08 Jul 2024

Hi Stuart, When programmatically modifying the fields bound to a form, you should also programmatically invoke the appropriate method to indicate that the component should re-validate its state. For example, you can invoke IsValid, which attempts to validate the form and returns its validation state. I have prepared a rather simple example where this can be observed: Run [https://blazorrepl.telerik.com/cIkraikX04fcOSPm14](https://blazorrepl.telerik.com/cIkraikX04fcOSPm14) Enter a value of length greater than 5 (e.g. "foobar") - user input triggers validation and the input should receive an invalid state Click on the Change Value button - this will update the value to a valid one, "foo", and will also trigger validation, which will update the state of the input. I hope the above helps with your implementation.

### Response

**Stuart** commented on 09 Jul 2024

Hi Radko, Thankyou for the advise, I had Experimented while waiting for your advise and come up with basically the same solution. I was about to post it here for reference when I saw your response. Instead of using the isvalid method I added a ref to the TelerikForm then run the NotifyFieldChanged method used by fluent validator to only check the programatically changed field. E.g. the below method was added to my wrapped form component that could be used by the parent component. Razor: <TelerikForm @ref="@Form"....Other properties /> Razor.cs: private TelerikForm Form { get; set; } public void ValidateField ( string fieldIdentifier ) {
Form.EditContext.NotifyFieldChanged( new FieldIdentifier(Model, fieldIdentifier));
}

### Response

**Hristian Stefanov** commented on 11 Jul 2024

Hi Stuart, Thank you for updating us on how things turned out. I'm glad to hear that the matter is resolved now. Kind Regards, Hristian
