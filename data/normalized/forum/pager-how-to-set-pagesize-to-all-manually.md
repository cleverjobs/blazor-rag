# Pager: How to set PageSize to "All" manually

## Question

**And** asked on 26 Jul 2022

I am using a Pager and set the PageSizes to { null, 25, 50, 100 } where null means "All" according to documentation. When the user sets a PageSize, I save that number in the local storage of the browser. When the user returns to that page later, I will get that stored value and set the PageSize parameter accordingly. When the user sets the PageSize to "All", I save the total amount of entries to local storage, because that's what I get from the PageSizeChanged handler. When restoring that value later, of course the selected value in PageSize dropdown is empty, because I set the PageSize parameter to the total amount of entries. Since this number is not present in the dropdown list, it will simply show nothing. I would like the PageSizes dropdown to show "All" when PageSize is equal to the total amount of items. Is there a way to do this? In fact, I can't even set PageSize to null, since it is not nullable.

## Answer

**Dimo** answered on 28 Jul 2022

Hello Andre, You can do two things: Check if the saved page size is a member of the PageSizes collection. Then, apply it only if this is true. Set the PageSize to the total item count to achieve the initial "All" scenario. Regards, Dimo

### Response

**Andre** commented on 28 Jul 2022

Hello Demo, thanks for the response. So if I get this correctly, there is no way of setting the selected value in the PageSizes dropdown to "All" by code? I would probably need to build some workaroung with JavaScript, right? Is there any chance that this feature will be implemented in the future? It's just a small thing, but most of our users will see it as a bug when the dropdown is just empty. Regards, Andre

### Response

**Dimo** commented on 28 Jul 2022

There should be no need to use JavaScript - set the PageSize parameter to the total number of items in the data. On the other hand, I confirm we have no plans to change this behavior.

### Response

**Andre** commented on 01 Aug 2022

Thanks. It works now. But the order on which you set the parameters seems to be important. You need to set Total before you set PageSize. It didn't work the other way around.
