# Selecting first item in DropDownList for grid add/insert

## Question

**imw** asked on 05 Jan 2022

We have a grid with editor templates for a few types that are tied to a dropdownlist that is tied to a datasource. When user clicks new/add they get an empty form (we are using popup) but we would like the drowdowns to be preselected with the first values in the datasource. How do we do this? Is there some SelectedIndex property or similar available? We are currently doing something like this but it does not seem to nice even though it works. Also, what is the best way to differentiate between add and update in the EditorTemplate, ie how do we know what is what? <EditorTemplate> @{
EditingCorporateCustomer=context as CorporateCustomerDto;

if (EditingCorporateCustomer.CompanyTypeId==0)
{
EditingCorporateCustomer.CompanyTypeId=CompanyTypes[0].Id;

} <TelerikDropDownList Data="@CompanyTypes" @bind-Value="@EditingCorporateCustomer.CompanyTypeId" Width="95%" TextField="Name" ValueField="Id"> </TelerikDropDownList> } </EditorTemplate>

## Answer

**Marin Bratanov** answered on 08 Jan 2022

Hello, You have three approaches you can take: have a default value in the model provide an instance through the OnModelInit event use a custom command button instead of the built-in Add command button, and use the grid state to predefine the model you will be inserting with to have that default value. You can find an example of this here, see the "Initiate Editing or Inserting of an Item" section. Regards, Marin Bratanov
