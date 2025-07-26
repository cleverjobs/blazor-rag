# Form validation with <TelerikForm>

## Question

**Ale** asked on 25 Sep 2023

I've run into an issue and searched results have yielded a little, but not quite enough information. My project is in blazor server. I am using telerik form components and fluent validation. Is there a global way to prevent the inputs from submitting as you type? I can use the ValidateOn parameter which is fine but when using a <FormItem> component without a <Template> there is no way to do such. Also, i would like the textboxes and other inputs to not bind at all until onblur to prevent excess server calls. In those instances, i can work around it using the DebounceDelay parameter of the textbox but that seems the wrong approach. Finally, with the debounce delay, is it executed on the server or client? Meaning, if i use the DebounceDelay approach is a c# Timer still running and the component still communicating with the server as you type? Thank you in advance for any help or feedback!

### Response

**Hristian Stefanov** commented on 28 Sep 2023

Hi Alex, After carefully reviewing the information you've provided, I still have some uncertainties regarding the core objective. Specifically, it is a little hard for me to understand the meaning of 'prevent the inputs from submitting as you type.' Is the aim to restrict users from entering certain values at a given time? In essence, the validation process hinges on values bound to components, assessing their validity. Based on your description, it seems that you are referring to customizations within the Form. For such customizations, the use of templates is indeed necessary. I look forward to receiving further details from you, perhaps accompanied by a runnable configuration for more clarity. Please feel free to specify any aspects of your inquiry that I might not have fully grasped. Kind Regards, Hristian

### Response

**Alex** commented on 28 Sep 2023

Submit as you type is referring to the inputs ValueChanged event being bound to the oninput event. I would rather the inputs be bound to the onchange event, or at least have that be an option. It does seem that i have to use form item templates but that still doesn't solve the oninput vs onchange issue.

### Response

**Hristian Stefanov** commented on 02 Oct 2023

Hi Alex, Thank you for sharing additional insights, which have certainly helped me gain a better grasp of your intent. Upon closer examination of your latest message, I realized that your goal is to update the value within the OnChange event, as opposed to updating it with every keystroke via ValueChanged. To achieve this, remove the two-way binding from the input element and manage the value directly within the OnChange event handler. I've crafted an illustrative example for your reference below. You can put it to the test by entering at least three characters into the first input and then pressing the 'Enter' key, which will trigger the OnChange event and subsequently initiate the validation process. @using Microsoft.AspNetCore.Components.Forms
@using FluentValidation
@using Blazored.FluentValidation <div class="mt-4" style="margin: 0 auto;"> <TelerikForm EditContext="@EditContext"> <FormValidation> <FluentValidationValidator Validator="@Validator"> </FluentValidationValidator> </FormValidation> <FormItems> <FormItem> <Template> <label for="visited"> First name: </label> <TelerikTextBox DebounceDelay="0" Value="@MyModel.FirstName" OnChange="@MyOnChangeHandler" ValueExpression="@(()=> MyModel.FirstName)"> </TelerikTextBox> </Template> </FormItem> <FormItem Field="@nameof(Customer.LastName)" LabelText="Last name" /> </FormItems> </TelerikForm> </div> @code {
public EditContext EditContext {get; set; }
public Customer MyModel { get; set; }=new Customer();
public CustomerValidator Validator { get; set; }=new CustomerValidator();

private void MyOnChangeHandler(object theUserInput)
{
MyModel.FirstName=theUserInput.ToString();
}

protected override void OnInitialized()
{
EditContext=new EditContext(MyModel);
base.OnInitialized();
}

public class Customer
{
public string FirstName { get; set; }
public string LastName { get; set; }
}

public class CustomerValidator : AbstractValidator <Customer> {
public CustomerValidator()
{
RuleFor(customer=> customer.FirstName).MaximumLength(2);
RuleFor(customer=> customer.LastName).MaximumLength(2);
}
}
} Let me know if this aligns with your intended outcome. Kind Regards, Hristian
