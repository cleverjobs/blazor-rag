# Custom Image Icon in GridCommand

## Question

**Moh** asked on 15 Jan 2025

Hello I need to use something like Image Button in Grid that redirects the user to another page by clicking on it. I used the following code but I can't change its icon and put my own icon. <GridCommandColumn> <GridCommandButton Command="MyOwnCommand" Icon="@SvgIcon.InfoCircle" ThemeColor="@ThemeConstants.Button.ThemeColor.Tertiary" OnClick="@MyCustomCommandOnClickHandler"> click Me </GridCommandButton> </GridCommandColumn> Grid is dynamic and is set with ExpandoObject. Please help. Thanks

## Answer

**Dimo** answered on 16 Jan 2025

Hello Mohamad Javad, One option is to create custom SVG icons that you use in the same way as the built-in ones. Another option is to simply render the desired custom image inside the Button, together with the text. Regards, Dimo Progress Telerik
