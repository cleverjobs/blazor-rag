# form validation > template > does not show inline message

## Question

**Ale** asked on 25 Apr 2023

<TelerikForm Model="@Service.DataModel" Width="1000px" Columns="1" ColumnSpacing="20px" ValidationMessageType="FormValidationMessageType.Inline" OnValidSubmit="@OnSubmitClick"> <FormValidation> <FluentValidationValidator Validator="@FormValidator" DisableAssemblyScanning="@true"> </FluentValidationValidator> </FormValidation> <FormItems> <FormGroup Columns="3" ColumnSpacing="10px"> <FormItem Class="k-form-input-field" LabelText="Source File:" Field="@nameof(Service.DataModel.OriginalFileName)" Enabled="false" /> <FormItem Class="k-form-input-field" LabelText="Document Name:" Field="@nameof(Service.DataModel.Name)" Enabled="@Service.IsAddMode" /> <FormItem Class="k-form-input-field w290" LabelText="Version:" Field="@nameof(Service.DataModel.Version)" Enabled="false"> <Template> <label for="type" class="k-label k-form-label"> Version: </label> <label> @(Service.DataModel.Version.HasValue ? DateTime.FromBinary(Service.DataModel.Version.Value).ToString("G") : "") </label> </Template> </FormItem> </FormGroup> <FormGroup Columns="3" ColumnSpacing="10px"> <FormItem Field="@nameof(Service.DataModel.Type)" Enabled="@Service.IsAddMode"> <Template> <label for="type" class="k-label k-form-label"> Type: </label> <TelerikDropDownList id="type" Data="@Service.Types" @bind-Value="@Service.DataModel.Type.Key" OnChange="@Service.TypeChanged" ValueField="@nameof(GlossaryItem<string, string>.Key)" TextField="@nameof(GlossaryItem<string, string>.Value)" DefaultText="Select..." Width="290px" /> </Template> </FormItem> <FormItem Field="@nameof(Service.DataModel.Status)"> <Template> <label for="status" class="k-label k-form-label"> Status: </label> <TelerikDropDownList id="status" Data="@Service.Statuses" @bind-Value="@Service.DataModel.Status.Key" ValueField="@nameof(GlossaryItem<string, string>.Key)" TextField="@nameof(GlossaryItem<string, string>.Value)" DefaultText="Select..." Width="290px" Enabled="@(!string.IsNullOrEmpty(Service.DataModel.Type.Key))" /> </Template> </FormItem> <FormItem Field="@nameof(Service.DataModel.IsActive)"> <Template> <label for="IsActive" class="k-label k-form-label"> Active: </label> <TelerikCheckBox id="IsActive" @bind-Value="@Service.DataModel.IsActive"> </TelerikCheckBox> </Template> </FormItem> </FormGroup> <FormGroup Columns="1" ColumnSpacing="10px"> <FormItem Field="@nameof(Service.DataModel.Agencies)"> <Template> <label for="jurisdiction" class="k-label k-form-label"> Agency / Authority: </label> <TelerikMultiSelect id="jurisdiction" Data="@Service.Agencies" @bind-Value="@Service.SelectedAgencies" TextField="Value" ValueField="Key" ScrollMode="@DropDownScrollMode.Virtual" PageSize="10" ItemHeight="35" Filterable="true" TValue="int" TItem="GlossaryItem<int, string>" /> <TelerikValidationMessage For="@(()=> Service.Agencies)" /> </Template> </FormItem> public class DocumentEditFormValidator : AbstractValidator <DocumentModel> {
public DocumentEditFormValidator()
{
RuleFor(x=> x.Name)
.NotEmpty()
.WithMessage("Document name can't be empty");
RuleFor(x=> x.Type.Key)
.NotEmpty()
.WithMessage("Type must be set");
RuleFor(x=> x.Status.Key)
.NotEmpty()
.WithMessage("Status must be set");
RuleFor(x=> x.Agencies)
.NotEmpty()
.When(_=> _.Type.Key !="DD")
.WithMessage("Agency / Authority can't be empty");
}
}

### Response

**Aleksandr** commented on 25 Apr 2023

so, multy & dll behaves differently, dll has red border, multi does not, but both do not show validation message

## Answer

**Dimo** answered on 28 Apr 2023

Hi Aleksandr, When using FormItem Template, the built-in validation messages from the Form do not render and this is expected. Instead, you can use the Telerik Validation Tools to provide validation messages. Regards, Dimo Progress Telerik

### Response

**Aleksandr** commented on 28 Apr 2023

I do use , but it does not work <TelerikValidationMessage For="@(()=> Service.Agencies)" />

### Response

**Dimo** commented on 28 Apr 2023

In this case, double-check the validator configuration. In addition, validating Service.Agencies makes no sense - this is the data, not the value. This example works. @using Microsoft.AspNetCore.Components.Forms @using Blazored.FluentValidation @using FluentValidation

<TelerikForm Model="@MyModel"> <FormValidation> <FluentValidationValidator Validator="@Validator" /> </FormValidation> <FormItems> <FormItem> <Template> First Name: <TelerikTextBox @bind-Value="@MyModel.FirstName" Width="200px" /> <TelerikValidationMessage For="@( ()=> MyModel.FirstName)" /> </Template> </FormItem> <FormItem> <Template> Last Name: <TelerikTextBox @bind-Value="@MyModel.LastName" Width="200px" /> <TelerikValidationMessage For="@( ()=> MyModel.LastName)" /> </Template> </FormItem> </FormItems> </TelerikForm> @code { public Customer MyModel { get; set; }=new Customer(); public CustomerValidator Validator { get; set; }=new CustomerValidator(); public class Customer { public string FirstName { get; set; } public string LastName { get; set; }
} public class CustomerValidator: AbstractValidator <Customer> { public CustomerValidator ( ) {
RuleFor( customer=> customer.FirstName).NotEmpty().MaximumLength( 50 );
RuleFor( customer=> customer.LastName).NotEmpty().MaximumLength( 50 );
}
}
}

### Response

**Aleksandr** commented on 28 Apr 2023

got you, if there data is the collection, should it look like Service.Agencies.Any() or something like that?

### Response

**Aleksandr** commented on 01 May 2023

@Dimo i dont need any examples how to validate simple properties, the work out of the box, what would be better is to have example how to validate collection

### Response

**Aleksandr** commented on 01 May 2023

so works fine with ddl, does not with multi select, because we need to valudate collection instead of simple property
