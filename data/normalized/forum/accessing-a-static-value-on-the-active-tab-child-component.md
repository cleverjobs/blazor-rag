# Accessing a static value on the active tab child component?

## Question

**Jst** asked on 01 Nov 2021

I have a Tabstrip control on a Blazor page. Each tab is represented by a component. In each component's code I have a static value i.e. string staticValue="Page1Value" On the parent page I would like to access the "staticValue" value for the currently active tab/child component. It seems that there should be a simple way to do this. I'm finding lots of commentary on pushing parent values to the child and pushing a changed value to the parent via events. But nothing about a parent retrieving a simple static value from a child.

### Response

**Dimo** commented on 04 Nov 2021

Hi John, This sounds like a generic Blazor development task. You can take a look at the Microsoft documentation about parent-child parameter binding.
