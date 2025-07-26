# How to hide border for selected tab?

## Question

**Iva** asked on 22 Mar 2022

Can't find css class for hide this border Border displayed after click on tab content.

## Answer

**Ecofip** answered on 23 Mar 2022

Hello Ivan, I think this behavior is not really wanted by anyone, and I've found a workaround. You have to select these classes with the :focus pseudo selector. Classes are : k-tabstrip-content and k-content. Just add "outline-style: none;" and it should do the trick. I think this behavior is not really wanted by anyone, and I've found a workaround. Good luck, Dylan

### Response

**Thang** commented on 29 Aug 2022

Doesn't work for me. Pseudo focus und active set on "outline:none" doesn't have any effect. Do you have another hint?

### Response

**Dimo** answered on 01 Sep 2022

To anyone who visits this thread in the future, here are 3 things to keep in mind: The active (selected) TabStrip tabs use a box-shadow style. The focused TabStrip content uses an outline style. Both styles exist to improve accessibility and usability with keyboard navigation, and we don't encourage removing them. If you still want to do it, here is a runnable test page that shows how. You can follow a similar approach to change the styles instead of removing them. On a side note, check this KB article for tips about CSS theme customizations. Regards, Dimo Progress Telerik

### Response

**Phuc** answered on 21 Sep 2022

Hi Ivan, Can add style remove outline. .k-tabstrip-content.k-focus, .k-tabstrip-content.k-state-focused, .k-tabstrip-content:focus, .k-tabstrip> .k-content.k-focus, .k-tabstrip> .k-content.k-state-focused, .k-tabstrip> .k-content:focus { outline: none !important; } In here, i use!important for style so you can think about more.
