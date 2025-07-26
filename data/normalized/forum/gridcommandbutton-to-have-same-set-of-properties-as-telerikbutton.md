# GridCommandButton to have same set of properties as TelerikButton

## Question

**Ale** asked on 11 Oct 2021

like Hidden (but not just Enabled)

### Response

**Dimo** commented on 14 Oct 2021

Hi Aleksandr, Can you describe some use cases that require a Hidden attribute for the Grid command buttons? That is, cases in which Enabled="false" is not a suitable option. I assume that you know that you can render command buttons with a conditional code block, e.g. <GridCommandColumn> @if (!(context as Product).Discontinued)
{ <GridCommandButton Command="Edit" Icon="edit"> Edit </GridCommandButton> } </GridCommandColumn>

### Response

**Aleksandr** commented on 14 Oct 2021

Hello Dimo, Yes, I know that I can use conditions to render, but having such property for GridCommandColumn, TelerikButton makes the code/approach more similar, let say having this sugar will be appreciated :-) Thx Alex

### Response

**Dimo** commented on 15 Oct 2021

Hey Alex, I double-checked the Button documentation and the source code. The Hidden property is intended for internal use and that is why it is not documented on purpose. Blazor requires component Parameters to be public, that is why the property is accessible for use. In other words, you may rely on it if you like, but we still recommend conditional rendering instead, for better future proof-ness.
