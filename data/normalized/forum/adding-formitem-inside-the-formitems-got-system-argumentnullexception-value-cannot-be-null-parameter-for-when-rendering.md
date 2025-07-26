# Adding FormItem inside the FormItems got System.ArgumentNullException: Value cannot be null. (Parameter 'For') when rendering

## Question

**Lui** asked on 26 Dec 2023

Adding FormItem inside the FormItems got System.ArgumentNullException: Value cannot be null. (Parameter 'For') when rendering This is my code of course the Model and EditContext will be different. <TelerikForm Model="FarsDetailSate.Model"@ref="FormReference" EditContext="FarsDetailSate.EditContext" Size="@ThemeConstants.Form.Size.Medium" Columns="1"ColumnSpacing="40px" Orientation="FormOrientation.Vertical" Class="mb-3 px-3"> <FormValidation> <FluentValidationValidatorValidator="@Validator"> </FluentValidationValidator> <TelerikValidationSummary/> </FormValidation> <FormItems> <FormItem Field="@nameof(Vehicle.MotorCarrierIdentificationNumber)" LabelText="Carrier: " Enabled="FarsDetailSate.HasEditPermission" Class="col-sm-12 col-md-6 col-lg-4"> </FormItem> </FormItems> <FormButtons></FormButtons> </TelerikForm>

### Response

**Hristian Stefanov** commented on 27 Dec 2023

Hi Luis, Thank you for sharing the details of the error you're encountering. To delve deeper into the issue, I attempted to replicate the problem by configuring an example with the same Form configuration. On my end, it appears that the Form operates without any errors, and the validation works as expected. I've prepared a sample for your reference, which you can access via this REPL link. Feel free to compare it with your actual application. Should the problem persist, please modify the provided REPL sample to showcase the specific issue in a self-contained, runnable manner. This will help a more comprehensive investigation on my part, allowing me to observe the error directly. I eagerly await hearing an update from you. Kind Regards, Hristian

### Response

**Luis** commented on 27 Dec 2023

Hi Hristian, Sorry I didn't add all the details, in this case the MotorCarrierIdentificationNumber can be nullable string, since sometime is added, the issue is using the FormItem as a string. Can you test it again using string instead of an int ? Regards, Luis

### Response

**Luis** commented on 28 Dec 2023

Hi Hristian, I was able to replicate my issue, see the FormItem Address.City, I got the error, of course if I do the Template it works fine but it is not binding correctly since it is taking only the first letter of the string I'm typing on the Textbox. See below the code to reproduce, I even use the REPL and got the same error <TelerikForm Model="@person" OnValidSubmit="ValidHandler"> <FormValidation> <DataAnnotationsValidator></DataAnnotationsValidator> </FormValidation> <FormItems> <FormItem Field="@nameof(Person.Id)" Enabled="false" LabelText="Id"></FormItem> <FormItem Field="@nameof(Person.FirstName)" LabelText="First name" Hint="Enter your first name"></FormItem> <FormItem Field="@nameof(Person.LastName)" LabelText="Last name" Hint="Enter your last name" ColSpan="2"></FormItem> <FormItem Field="@nameof(Person.DOB)" LabelText="Date of birth" Hint="Enter your Date of Birth"></FormItem> <FormItem Field="@nameof(Address.Address1)" LabelText="Address 1"> <Template> <label for="address1-input" class="k-label k-form-label"> Address1: </label> <div class="d-flex flex-row"> <TelerikTextBox Id="address1-input" @bind -Value="@person.Addresses[0].Address1" DebounceDelay="300" Enabled="true"></TelerikTextBox> </div> <TelerikValidationMessage For="@(()=> person.Addresses[0].Address1)"></TelerikValidationMessage> </Template> </FormItem> <FormItem Field="@nameof(Address.Address2)" FieldType="typeof(string)" LabelText="Address 2"> <Template> <label for="address2-input" class="k-label k-form-label"> Address2: </label> <div class="d-flex flex-row"> <TelerikTextBox Id="address2-input" @bind -Value="@person.Addresses[0].Address2" DebounceDelay="300" Enabled="true"></TelerikTextBox> </div> <TelerikValidationMessage For="@(()=> person.Addresses[0].Address2)"></TelerikValidationMessage> </Template> </FormItem> <FormItem Field="@nameof(Address.City)" FieldType="typeof(string)" LabelText="City"></FormItem> </FormItems> </TelerikForm> @code { public Person person=new Person(); protected override void OnInitialized() { Address address=new Address(); person.Addresses.Add(address); base.OnInitialized(); } private void ValidHandler() { var seePerson=person; } public class Person { public int Id { get; set; }=10; public string FirstName { get; set; } public string LastName { get; set; } public DateTime DOB { get; set; } public List <Address> Addresses { get; set; }=new(); } public class Address { public string Address1 { get; set; } public string Address2 { get; set; } public string City { get; set; } public string State { get; set; } public string Zip { get; set; } } }

## Answer

**Radko** answered on 01 Jan 2024

Hi Luis, Thank you for sending the repro code! As for what is causing the issue - in general, nested model properties require certain additional work: - the DataAnnotationsValidator only validates top-level properties of the model bound to the form that aren't collection- or complex-type properties. Instead, you can use ObjectGraphDataAnnotationsValidator. You can read more about this here: Validating nested models, collection types, and complex types. We also have a docs page on our own that can be found here: Validate a Complex Model. Note this is not specific to our own Form component, rather than to Blazor itself. - the configuration itself needs to be amended, notably the nameof declarations for the FormItems related to the nested objects are incorrect. What I mean is that the Form itself is bound to a specific object, in this case the model Person, and referring to a property with a syntax such as nameof(Address.City) is bound to yield no result - this model and its corresponding property is not the model the Form is bound to. Instead, use the correct nameof syntax or altermatively don't use nameof() at all. Lastly, here is the amended code. Note you will have to install the following package in order to get access to the object graph validator: Microsoft.AspNetCore.Components.DataAnnotations.Validation Nuget. @using System.ComponentModel.DataAnnotations

<TelerikForm Model="@person" OnValidSubmit="ValidHandler">
<FormValidation>
<ObjectGraphDataAnnotationsValidator></ObjectGraphDataAnnotationsValidator>
</FormValidation>
<FormItems>
<FormItem Field="@nameof(Person.Id)" Enabled="false" LabelText="Id"></FormItem>
<FormItem Field="@nameof(Person.FirstName)" LabelText="First name" Hint="Enter your first name"></FormItem>
<FormItem Field="@nameof(Person.LastName)" LabelText="Last name" Hint="Enter your last name" ColSpan="2"></FormItem>
<FormItem Field="@nameof(Person.DOB)" LabelText="Date of birth" Hint="Enter your Date of Birth"></FormItem>
<FormItem LabelText="Address 1">
<Template>
<label for="address1-input" class="k-label k-form-label">Address1: </label>
<div class="d-flex flex-row">
<TelerikTextBox Id="address1-input" @bind-Value="@person.Addresses[0].Address1" DebounceDelay="300" Enabled="true"></TelerikTextBox>
</div>
<TelerikValidationMessage For="@(()=> person.Addresses[0].Address1)"></TelerikValidationMessage>
</Template>
</FormItem>
<FormItem LabelText="Address 2">
<Template>
<label for="address2-input" class="k-label k-form-label">Address2: </label>
<div class="d-flex flex-row">
<TelerikTextBox Id="address2-input" @bind-Value="@person.Addresses[0].Address2" DebounceDelay="300" Enabled="true"></TelerikTextBox>
</div>
<TelerikValidationMessage For="@(()=> person.Addresses[0].Address2)"></TelerikValidationMessage>
</Template>
</FormItem>
<FormItem LabelText="City">
<Template>
<label for="address-city" class="k-label k-form-label">City: </label>
<div class="d-flex flex-row">
<TelerikTextBox Id="address-city" @bind-Value="@person.Addresses[0].City" DebounceDelay="300" Enabled="true"></TelerikTextBox>
</div>
<TelerikValidationMessage For="@(()=> person.Addresses[0].City)"></TelerikValidationMessage>
</Template>
</FormItem>
</FormItems>
</TelerikForm>
@code { public Person person=new Person(); protected override void OnInitialized ( ) {
Address address=new Address();
person.Addresses.Add(address); base.OnInitialized();
} private void ValidHandler ( ) { var seePerson=person;
} public class Person { public int Id { get; set; }=10; public string FirstName { get; set; } public string LastName { get; set; } public DateTime DOB { get; set; }

[ ValidateComplexType ] public List<Address> Addresses { get; set; }=new ();
} public class Address { public string Address1 { get; set; } public string Address2 { get; set; } public string City { get; set; } public string State { get; set; } public string Zip { get; set; }
}
} I hope the above helps. Regards, Radko Progress Telerik
