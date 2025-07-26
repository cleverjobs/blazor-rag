# so does all the window markup have to be defined in your main page that wants to show it?

## Question

**Dav** asked on 03 Jun 2021

I want to make a separate razor page to to hold the markup & code for the window component. Then display it modally on the man page. Can that be done?

## Answer

**Nadezhda Tacheva** answered on 08 Jun 2021

Hi David, Yes, you can create a separate component to hold the markup and code for the TelerikWindow. Then on the main page you can get a reference to this component and use that to toggle the field that is bound to the Visible parameter of the Window. To better illustrate how to achieve the described scenario, I have created this knowledge base article - Open a Window from another component. I hope you will find it useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva Progress Telerik

### Response

**David** answered on 08 Jun 2021

Thanks I have it working now as a sperate component with a mulitselect in it.
