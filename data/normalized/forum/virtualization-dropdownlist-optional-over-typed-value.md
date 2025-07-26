# Virtualization DropDownList Optional Over-Typed Value

## Question

**Jer** asked on 14 Apr 2022

Does virtualization DropDownList support a user providing a value not in the list? Scenario: There's a list of currently active work items that would be a query to a data source that populates the DropDownList. There's a chance that the user would want to override this list and provide a value not provided in the DropDownList. Can the virtualization drop down list provide the normal behavior but be able to over-type the selected value in the situation it doesn't match the needed value?

## Answer

**Dimo** answered on 19 Apr 2022

Hello Jerdobi, The DropDownList value should belong to the current list of items. For your scenario, consider a ComboBox with AllowCustom="true". Alternatively, provide a mechanism for the user to add an item to the DropDownList datasource, and then select it as a second step. Regards, Dimo
