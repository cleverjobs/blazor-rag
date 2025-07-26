# Form using FluentValidation not validating

## Question

**Eri** asked on 02 May 2022

Hey, I am following the example from you site about how to use FluentValidation, but I am running into a problem where the validation doesn't appear to be firing or being captured by the form when submitted. I have a break point on my validation code, it is executes when the object is initiated, but not when submitted. The only different between my code and the example is that i am binding to a MODEL vs the example, which uses EDITCONTEXT. Could that be impacting the functionality? If no, would be possible to get a simple example of a page using FluentValidation, butbound to model. Thanks in advance.

### Response

**Eric** commented on 02 May 2022

Just to add to this, i took the example code as is and copied it into a page on my project. The same behavior occurred where the validation was not fired. @page "/test1" @using Microsoft.AspNetCore.Components.Forms
@using FluentValidation

<div class="mt-4" style="margin: 0 auto;">
<TelerikForm EditContext="@EditContext">
<FormValidation>
<FluentValidationValidator Validator="@Validator"></FluentValidationValidator>
</FormValidation>
</TelerikForm>
</div>

@code { public EditContext EditContext { get; set; } public Customer MyModel { get; set; }=new Customer(); public CustomerValidator Validator { get; set; }=new CustomerValidator(); protected override void OnInitialized ( ) {
EditContext=new EditContext(MyModel); base.OnInitialized();
} public class Customer { public string FirstName { get; set; } public string LastName { get; set; }
} public class CustomerValidator: AbstractValidator <Customer>
{ public CustomerValidator ( ) {
RuleFor(customer=> customer.FirstName).NotEmpty().MaximumLength( 50 );
RuleFor(customer=> customer.LastName).NotEmpty().MaximumLength( 50 );
}
}
}

## Answer

**Hristian Stefanov** answered on 03 May 2022

Hi Eric, The Form can work with both - Model and EditContext. I can confirm that a change from EditContext to Model should not impact the functionality. I have prepared for you an example in the attached project that shows Model use. You can run and test the project to see the result. Here is one more example with regular EditForm to use as a reference - FluentValidation with Model. Regards, Hristian Stefanov Progress Telerik
